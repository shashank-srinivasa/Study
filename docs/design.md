# Design: "How AI Actually Works" — a granular 3–4 month learning guide

Date: 2026-11-23

## Intent and why

The learner is a working software engineer on a CDN (Edge) service. They use AI tools daily
(Claude, opencode) but have no understanding of how they work internally. They want to learn
this genuinely — for understanding and to eventually build something with real impact (they
cited Tesla FSD as inspiration) — **not** for job hunting or credentials.

They asked for a guide they can follow "at utmost granularity" that is "well tested", which
they defined as: **made of things other people at their level have tried and found helpful.**

## Goals

- A single, ordered guide that takes the learner from zero to:
  1. Enough math (linear algebra, calculus, probability, optimization) to read and derive what
     the code does.
  2. Having built neural networks and a GPT-style language model **from scratch**, and trained
     one locally.
  3. A first real working understanding of the hardware/software layer: GPU architecture,
     memory hierarchy / roofline, writing and profiling kernels, why models run fast or slow.
- Granularity: the learner should never have to decide "what do I do next?"
- Target duration: **3–4 months** of steady effort (assume ~8–12 h/week ≈ 120–160 hours).
- Ends with a "where to go next" branch section (FSD/vision/robotics; ML systems; LLMs).

## Non-goals

- Not career-oriented: no interview prep, resume, certificates, or "AI jobs" content.
- Not a deep specialization in vision, RL, or robotics within the 3–4 months (those are
  pointers in the "next" section only).
- Not a set of original lessons that replace the proven resources. The guide is the glue,
  sequencing, and checkpoints around them.
- No custom autograder/test-suite repo (learner explicitly defined "tested" as proven-by-others,
  not automated tests).

## Anti-goals (would be a failure even if "complete")

- Including unproven, obscure, or AI-invented resources. Every primary resource must be widely
  used and widely recommended among self-learning engineers.
- Fabricating testimonials or claims about who used a resource.
- Steps so large or vague that the learner has to plan on their own ("learn linear algebra").
- A broad survey that touches everything shallowly (approach C was explicitly rejected).
- Stale instructions (dead links, renamed repos, deprecated setup commands).

## Constraints

- Hardware: Apple M4 Max, 64 GB unified memory, macOS (arm64). Python 3.14 and `uv` installed.
  No local NVIDIA GPU.
  - Everything except CUDA/Triton must run locally on the Mac (PyTorch MPS backend, and/or MLX).
  - CUDA/Triton sections use a rented/free cloud GPU (e.g. Google Colab free tier, RunPod,
    Modal, Lambda). Note approximate cost.
- The learner will decide their weekly schedule later, so steps are **sessions**, not calendar days.
- Prerequisite assumed: solid general programming; Python familiarity likely but not assumed deep.

## Approaches considered

- **A. Bottom-up, from scratch (CHOSEN).** Math intuition → Karpathy *Neural Networks: Zero to
  Hero* (micrograd → makemore → GPT) → train a small GPT locally → intro to the hardware layer
  (Horace He's "Making Deep Learning Go Brrrr", Simon Boehm's CUDA matmul post, Triton on a
  cloud GPU, profiling own GPT). Chosen because it directly serves the learner's two stated
  interests (how it works under the hood; the hardware/software layer) and is the most commonly
  cited "this made it click" path for engineers.
- **B. Top-down (fast.ai first).** Faster early wins, but weaker on internals and doesn't reach
  hardware in the timeframe. Rejected as primary spine.
- **C. Broad survey.** Touches LLMs, vision, RL, FSD, GPUs; rejected — too shallow for 3–4 months.

## Decided parts of the how

- **Spine of proven resources** (primary; builder must verify each is current):
  - Math intuition: 3Blue1Brown *Essence of Linear Algebra*, *Essence of Calculus*,
    *Neural Networks* series (incl. Transformers/attention chapters).
  - Math reference: *Mathematics for Machine Learning* (Deisenroth et al., free PDF) — used for
    targeted lookups, not cover-to-cover.
  - Probability support: StatQuest (targeted) and/or Harvard Stat 110 (targeted lectures only).
  - Core build: Andrej Karpathy *Neural Networks: Zero to Hero* (full series), then training
    a small GPT locally (nanoGPT or its current recommended successor — verify).
  - Hardware layer: Horace He "Making Deep Learning Go Brrrr From First Principles";
    Simon Boehm "How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance";
    official Triton tutorials; selected GPU MODE lectures; optionally selected Stanford CS149 /
    CMU 15-418 lectures; PyTorch profiler on own model.
  - "Next" section pointers: CS231n, openpilot, LeRobot, Sutton & Barto (FSD/robotics);
    CS149, *Programming Massively Parallel Processors*, vLLM, "How to Scale Your Model",
    MIT 6.5940 (systems/efficiency); Stanford CS336 (LLMs).
- **Structure:** Phases → Weeks (as pacing markers assuming ~10 h/week) → **Sessions of
  ~1.5–2 hours**. Each session contains:
  - Goal (one line)
  - Exact resource + exact part (video timestamps/chapter/section where useful)
  - What to do/type/build (concrete actions)
  - "You're done when…" checkpoint (observable, self-checkable)
  - Known sticking points and how to get past them (only well-known ones)
  - Optional "go deeper" pointer
- **Math starting point:** the learner hasn't done math in about 10 years. Assume high-school
  algebra is rusty and calculus is mostly forgotten. Start from zero and give gentle refreshers
  on functions, slopes, exponents/logs and summation notation before 3Blue1Brown.
- **Math depth (author's call, the learner can override):** mostly intuition and reading, plus
  a small set of **anchor derivations** done on paper and checked numerically in code:
  (1) derivative of a simple function, by hand and by finite differences; (2) the chain rule
  through a tiny expression graph, which is what micrograd does; (3) the gradient of a
  single neuron; (4) the softmax + cross-entropy gradient. These are the places where
  deriving it yourself pays off most. Everything else stays intuition-level.
- **Math share:** about 15–20% of the hours (around 25 h), front-loaded a little more than
  usual because of the gap, then just-in-time.
- **Math is interleaved** with building (just-in-time), not front-loaded, except the
  refresher and intuition block at the start.
- **Phase-end milestones:** a small artifact the learner builds per phase (e.g. own micrograd,
  own GPT trained on a dataset of their choice, a Triton kernel + profiler report on own GPT).
- **Progress tracking:** checkbox per session so the learner can mark progress.
- **Format and location:** Markdown in `~/ai-learning-guide/` (a `README.md` overview + one
  file per phase), plus a short setup file for the Mac environment. Plain markdown so it reads
  well in any editor/GitHub.
- **Honesty rule:** "proven" means widely used and recommended; the guide states this plainly
  and contains no invented testimonials.

## Verification policy (author's call)

- The builder has web access and must fetch every link, repo README, and setup command before
  including it. Anything that can't be verified is left out rather than written from memory.
- Granularity is anchored on things that can be verified: video titles, chapter and section
  names, and repo paths. Timestamps are included only where they were checked against the
  actual video description or chapters.
- Python environment: a dedicated `uv` virtual environment pinned to a Python version that
  PyTorch currently supports on macOS arm64 (likely 3.12 or 3.13; verify). The system
  Python 3.14 is not used.

## Left to the builder

- Exact session-by-session breakdown and the split of the ~120–160 hours across phases
  (rough guide: math refresher + intuition ~15–20%, Zero to Hero + GPT ~55%, hardware layer
  ~20–25%, wrap-up ~5%).
- Which specific GPU MODE / CS149 lectures to include.
- Whether to use PyTorch MPS, MLX, or both for local work (prefer whatever keeps Zero to Hero
  code working with minimal friction on Apple Silicon).
- Verifying every link, repo, and setup command is current as of writing, and choosing the
  current successor if a resource has been deprecated (e.g. nanoGPT status).
- Exact cloud GPU recommendation and cost estimate.
