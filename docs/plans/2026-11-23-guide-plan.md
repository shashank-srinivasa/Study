# "How AI Actually Works" Guide — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Produce a session-by-session markdown learning guide (about 140 hours) that takes a
software engineer with a 10-year math gap from zero to building their own GPT and writing and
profiling a GPU kernel, using only widely proven resources.

**Architecture:** One markdown file per phase plus a README, all following a strict session
format. A small Python checker enforces the format, the per-phase and total hours, and that
every link resolves. That checker is the "test suite" for the guide. Each content task
verifies its resources live (WebFetch) before writing, then runs the checker.

**Tech Stack:** Markdown; Python 3.12+ checker using only the standard library (`re`,
`urllib`, `argparse`) plus `pytest` (run via `uv run --with pytest`); `git` for local history.

**Spec:** `~/ai-learning-guide/docs/design.md`

## Global Constraints

- Root: `~/ai-learning-guide/`. Local git repo only; never push anywhere.
- Every primary resource must be widely used and recommended. No invented testimonials.
  "Proven" is stated plainly as "widely used and recommended."
- Every URL, repo, and command must be verified against the live source (WebFetch, or by
  running the command) before inclusion. If it can't be verified, leave it out.
- Timestamps only where verified against the video's chapters or description; otherwise use
  video titles and section names.
- Sessions are about 1.5–2 h (allowed range 1.0–2.5 h). Core total is 120–160 h.
- Learner hardware: Apple M4 Max, 64 GB, macOS arm64. Local work on CPU/MPS (and MLX where
  useful). CUDA/Triton only on a cloud GPU, with cost noted.
- Python: a dedicated `uv` venv pinned to a PyTorch-supported version (verify; likely 3.12);
  never the system Python 3.14.
- Math assumes a 10-year gap: refreshers first, mostly intuition, plus exactly four anchor
  derivations (simple derivative; chain rule on an expression graph; single-neuron gradient;
  softmax + cross-entropy gradient), each done on paper and checked numerically.
- Hour split (approximate): math 15–20%, Zero to Hero + GPT about 55%, hardware 20–25%,
  wrap-up about 5%.
- No career, interview, or certificate content.

## Session format (fixed; the checker enforces it)

```markdown
### Session 2.3 — Backprop through a neuron (~2 h)
- [ ] Done
**Goal:** one line
**Resource:** [Title](https://...) — exact part
**Do:**
1. concrete action
**Done when:** observable, self-checkable result
**Sticking points:** (optional)
**Go deeper:** (optional)
**Knowledge check:**
- question 1 (3–5 questions, each answerable from the session's resource)
```

Every phase file 01–05 ends with a `### Session N.P — Project: <name> (~X h)` session. The
project is done without a video, has a clear spec and acceptance criteria, and may span
multiple sessions. Its "Resource" field points only to docs/references, not walkthroughs.
The README has a "Community" section with verified links.

Optional sessions put `(optional)` in the title before the hours. Their hours count toward
`optional`, not `core`.

## File Structure

| File | Responsibility | Core hours |
|---|---|---|
| `tools/check_guide.py` | parse sessions, validate fields, sum hours, check links | — |
| `tests/test_check_guide.py` + `tests/fixtures/*.md` | checker tests | — |
| `README.md` | what this is, how to use it, phase map, progress table, expected outcome | — |
| `00-setup.md` | Mac environment, uv venv, torch/MPS check, Jupyter | 2–4 |
| `01-math-foundations.md` | refreshers, 3B1B linear algebra and calculus, anchor derivation 1 | 20–26 |
| `02-micrograd.md` | Zero to Hero lecture 1, anchor derivations 2 and 3 | 10–14 |
| `03-makemore.md` | Zero to Hero makemore lectures (bigram → MLP → BatchNorm → backprop ninja → WaveNet), anchor derivation 4 | 26–34 |
| `04-gpt.md` | "Let's build GPT", the tokenizer lecture, training a small GPT on the M4 Max, GPT-2 reproduction (watch and partially run) | 30–40 |
| `05-hardware.md` | Horace He post, roofline, GPU architecture, CUDA matmul (Boehm), Triton tutorials, profiling own GPT | 26–34 |
| `06-capstone-and-next.md` | capstone, self-assessment, branch paths (FSD/robotics, ML systems, LLMs) | 4–8 |

---

### Task 1: Repo scaffold and guide checker

**Files:**
- Create: `tools/check_guide.py`, `tests/test_check_guide.py`, `tests/fixtures/good.md`,
  `tests/fixtures/missing_done_when.md`, `tests/fixtures/bad_hours.md`,
  `tests/fixtures/optional.md`, `.gitignore`

**Interfaces:**
- Produces:
  - `parse_sessions(text: str) -> list[Session]`, where `Session` is a dataclass with
    `id: str`, `title: str`, `hours: float`, `optional: bool`, `fields: dict[str, str]`,
    `has_checkbox: bool`, `line: int`
  - `validate(sessions) -> list[str]` (error messages)
  - `extract_urls(text: str) -> list[str]`
  - `check_url(url: str, timeout: float = 15) -> tuple[bool, str]` (GET with a browser-like
    User-Agent and generic client name, following redirects. 2xx/3xx is OK. 403/429 is a
    warning, not a failure.)
  - CLI: `python tools/check_guide.py FILE... [--hours MIN MAX] [--total MIN MAX] [--links]`.
    Exit code 0 means OK, 1 means errors. Prints `core=<h> optional=<h>` per file and a total.

- [ ] **Step 1:** `git init ~/ai-learning-guide`. Add `.gitignore` (`.venv/`, `__pycache__/`,
  `.ipynb_checkpoints/`).
- [ ] **Step 2: Write failing tests** in `tests/test_check_guide.py`:
  - `test_parses_good_fixture`: `good.md` has 2 sessions; ids `["1.1","1.2"]`; hours
    `[2.0, 1.5]`; both `has_checkbox`.
  - `test_missing_done_when_reported`: `validate` returns an error containing `"1.1"` and
    `"Done when"`.
  - `test_hours_out_of_range_reported`: a session marked `(~4 h)` gives an error containing
    `"hours"`.
  - `test_optional_hours_separate`: in `optional.md`, core=2.0 and optional=1.5.
  - `test_extract_urls`: finds markdown-link URLs and bare URLs, deduplicated.
  - `test_cli_hours_bounds`: running the CLI on `good.md --hours 10 20` exits 1.
  - `test_duplicate_session_id_reported`.
- [ ] **Step 3:** Run `uv run --with pytest pytest -q tests`. Expected: FAIL (module missing).
- [ ] **Step 4:** Implement `tools/check_guide.py`. The heading regex is
  `^### Session (\d+\.\d+) — (.+?) \((?:optional, )?~?([\d.]+) h\)$`, or detect
  `(optional)` in the title. The required fields are `Goal`, `Resource`, `Do`, `Done when`.
- [ ] **Step 5:** Run the tests. Expected: all PASS.
- [ ] **Step 6:** Commit with the message `"chore: guide checker"`.

### Tasks 2–8: Content chapters (one task per file, same step pattern)

Each content task follows these steps:

- [ ] **Step 1: Failing check:** run `python tools/check_guide.py <file> --hours MIN MAX`
  using the range from the File Structure table. Expected: FAIL (file missing).
- [ ] **Step 2: Verify resources live.** WebFetch every resource listed for the task. Record
  each one's current title, URL, structure (video list, chapters, sections) and status
  (current, deprecated, or replaced). Drop or replace anything that fails, and say so in the
  report.
- [ ] **Step 3: Write the chapter** in the session format. Each `Do:` list contains concrete
  actions (what to watch, type, run, or write on paper). Each `Done when:` is observable
  ("your loss after 1 epoch is below ~2.5", "you can derive X on paper and your numeric
  check agrees to 1e-6"). Sticking points come only from what the resource itself, its repo
  issues, or its README document.
- [ ] **Step 4:** Run `python tools/check_guide.py <file> --hours MIN MAX --links`.
  Expected: exit 0.
- [ ] **Step 5:** Commit with the message `"docs: <chapter>"`.

Task-specific content and checks:

**Task 2: `00-setup.md` (2–4 h)**
- Verify the latest PyTorch macOS arm64 Python support at pytorch.org/get-started. Pin the
  highest supported Python with `uv venv --python 3.X`.
- Actually run in a scratch venv outside the guide dir: install torch, numpy, matplotlib and
  jupyter, then run
  `python -c "import torch; print(torch.__version__, torch.backends.mps.is_available())"`.
  Record the real output in the guide as the expected result.
- Include a Colab account step for later; no spend yet.

**Task 3: `01-math-foundations.md` (20–26 h)**
- Resources to verify: Khan Academy (refreshers only: functions, exponents/logs, slope,
  Σ notation), 3B1B *Essence of Linear Algebra*, 3B1B *Essence of Calculus*, 3B1B
  *Neural Networks* chapters 1–4, StatQuest (probability basics, targeted), and the MML book
  PDF (reference).
- Must include anchor derivation 1: the derivative of `f(x)=3x²-4x+5` on paper, checked
  with a finite-difference snippet in Python. Note that this is the same function Karpathy
  uses in micrograd.
- The final session is a readiness check before Phase 2.

**Task 4: `02-micrograd.md` (10–14 h)**
- Resources to verify: Zero to Hero lecture 1 ("The spelled-out intro to neural networks and
  backpropagation: building micrograd") and the `karpathy/micrograd` repo.
- Split the ~2.5 h video across sessions, with coding along after each section. Anchor
  derivations 2 (chain rule on an expression graph) and 3 (single-neuron gradient), each
  checked against the learner's own `Value` class and PyTorch.
- Milestone: their own micrograd trains a small MLP on a toy dataset.

**Task 5: `03-makemore.md` (26–34 h)**
- Resources to verify: Zero to Hero makemore lectures parts 1–5 and the `karpathy/makemore`
  repo / `nn-zero-to-hero` notebooks.
- Anchor derivation 4 (softmax + cross-entropy gradient) goes alongside "Becoming a Backprop
  Ninja."
- The device note: use CPU for these small models (MPS overhead often outweighs any gain at
  this size).

**Task 6: `04-gpt.md` (30–40 h)**
- Resources to verify: "Let's build GPT: from scratch, in code, spelled out", "Let's build
  the GPT Tokenizer", "Let's reproduce GPT-2 (124M)", and the current status of
  `karpathy/nanoGPT` versus any successor named in its README (for example nanochat). Use
  whatever the README currently recommends.
- Milestone: their own GPT trained on MPS on a dataset of their choice. Include the real
  `device="mps"` adjustments. Set expectations that a full GPT-2 124M reproduction is not
  feasible locally: watch it, and run reduced-size steps.
- Include one session mapping the GPT to how Claude-like assistants differ (pretraining vs.
  post-training/RLHF), using the "Intro to Large Language Models" or "Deep Dive into LLMs"
  talk (verify which exists).

**Task 7: `05-hardware.md` (26–34 h)**
- Resources to verify: Horace He "Making Deep Learning Go Brrrr From First Principles", Simon
  Boehm "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance" (and its repo),
  the official Triton tutorials (vector add, fused softmax, matmul), the GPU MODE lecture
  list (pick 2–4 by title), the PyTorch profiler docs, and optionally Stanford CS149 lectures
  (pick specific ones).
- Cloud sessions name Colab (T4) as the default with a RunPod/Modal alternative, and give a
  verified approximate $/hour. Note that Boehm's numbers come from an A6000, so the
  learner's absolute numbers will differ; compare kernels relative to each other.
- Milestone: a profiling report on their own GPT (local, torch profiler) plus one Triton
  kernel benchmarked against PyTorch.

**Task 8: `06-capstone-and-next.md` (4–8 h) and `README.md`**
- The capstone gathers the milestones into one write-up plus a self-assessment checklist
  that mirrors the "expected result" list agreed with the learner.
- Branch paths (verify each): FSD/robotics (CS231n, openpilot, LeRobot, Sutton & Barto), ML
  systems (CS149, *PMPP*, vLLM, "How to Scale Your Model", MIT 6.5940), and LLMs (CS336).
- The README contains: purpose (understanding, not careers), how to use the session format,
  the phase table with core hours and a "~week N at 10 h/week" marker, the progress table,
  the expected outcome, an honesty note on "proven", and a "when stuck" section.

### Task 9: Whole-guide verification

- [ ] **Step 1:** Run `python tools/check_guide.py 0*.md --total 120 160 --links`.
  Expected: exit 0, with core total in range.
- [ ] **Step 2:** Run `uv run --with pytest pytest -q tests`. Expected: PASS.
- [ ] **Step 3:** Check that each phase's share of the hours matches the Global Constraints
  split. Adjust if not.
- [ ] **Step 4:** Read the guide end to end as the learner. Check that no session depends on
  something introduced later, that each of the 4 anchor derivations appears exactly once, and
  that no career content is present.
- [ ] **Step 5:** Commit with the message `"docs: guide v1 verified"`.

## Review Focus

1. **PyTorch vs. the system Python 3.14.** The learner runs `pip install torch` on the system
   Python and it fails or picks the wrong wheel. Expectation: setup forces the pinned uv venv
   and shows the verified import/MPS output. (Task 2 Step: run the real command and record
   its output.)
2. **Zero to Hero code on Apple Silicon.** Some notebook code assumes CUDA, or MPS turns out
   slower or missing an op. Expectation: each chapter states which device to use, and the
   GPT chapter shows the exact device changes. (Tasks 5 and 6 include the device notes.)
3. **The math gap stalls lecture 1.** The learner reaches micrograd without derivative
   intuition. Expectation: the Phase 1 readiness-check session blocks progression, with a
   clear "go back to session X" pointer. (Task 3: final session's `Done when`.)
4. **Cloud GPU friction.** No Colab GPU is available, or costs surprise the learner.
   Expectation: an alternative provider and a cost estimate are stated before any paid
   step. (Task 7 content check.)
5. **Link rot or deprecated repos** (for example nanoGPT superseded). Expectation: links are
   live-checked and the current recommended repo is used. (The `--links` flag on every
   chapter, plus Task 6's README verification.)
