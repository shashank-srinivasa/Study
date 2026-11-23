# How AI Actually Works — a step-by-step guide

A guide in the style of The Odin Project for a software engineer who uses AI tools every day and
wants to understand how they work underneath: the math, the models, and the hardware.

**This is for understanding, not credentials.** There is no interview prep or certificate content
here. The goal is to understand modern AI from the inside, well enough to build things with it
that matter.

## What you'll be able to do at the end

- **Built:** your own backprop engine (micrograd); character-level language models; a GPT from
  scratch; a GPT-4-compatible tokenizer; a GPT-2 (124M) reproduction; a tiny ChatGPT trained end
  to end on your Mac; CUDA and Triton kernels, including one plugged into your own GPT.
- **Understand:** how an LLM turns a prompt into a reply; what training actually does; why
  training breaks and how it's fixed; how pretraining, fine-tuning, and RLHF differ; and why models
  are fast or slow on real hardware.
- **Not yet:** frontier-scale training, research-level architecture design, or deep specialization
  in vision, RL, or robotics. Phase 6 helps you pick one of those for the next 3–6 months.

## Why these resources ("proven")

Every primary resource here is **widely used and widely recommended** among engineers teaching
themselves this material: 3Blue1Brown, Andrej Karpathy's *Neural Networks: Zero to Hero*, Horace
He's "Brrrr" post, Simon Boehm's CUDA matmul article, the official Triton tutorials, and the GPU MODE
lectures. "Proven" means exactly that: a strong track record of helping people at your level. It
doesn't mean any specific testimonial. What this guide adds is the order, the session breakdown,
what to do and type, the "done when" checks, the knowledge checks, and the projects.

All links, video titles, timestamps, prices, and repo statuses were checked on **2026-11-23**.
Timestamps come from each video's own chapter list. Prices change. If a link has died, search
for the resource's title.

## How to use this guide

Each phase is a file made of **sessions** of about 1.5–2.5 hours. Every session has the same parts:

| Part | What it means |
|---|---|
| **Goal** | What you'll understand or be able to do after the session |
| **Resource** | The exact video, article, or chapter, and which part of it |
| **Do** | Concrete steps: watch, type, run, or derive on paper |
| **Done when** | An observable check. Don't move on until it's true |
| **Sticking points** | Places people commonly get stuck, and how to get unstuck |
| **Knowledge check** | Questions you should be able to answer. If you can't, revisit the resource |

- Tick `- [ ] Done` → `- [x] Done` as you go. Your progress lives in these files. Commit them to
  a git repo if you like.
- Sessions marked **(optional)** don't count toward the core hours. Skip them freely.
- Every phase ends with a **Project** you do without a video. Don't skip these. They're where
  watching turns into knowing.
- **Type the code yourself.** Don't copy-paste. Typing it forces you to notice every line, and it's
  how Karpathy's lectures are designed to be followed: he builds everything live.
- Keep all your work in `~/ai-learning/` (set up in Phase 0).

## The phases

At about **10 hours a week**, the whole guide takes roughly **15 weeks (3.5 months)**.

| Phase | File | Core hours | Done by about (at 10 h/week) |
|---|---|---|---|
| 0. Setup | [00-setup.md](00-setup.md) | 3 | week 1 |
| 1. Math foundations | [01-math-foundations.md](01-math-foundations.md) | 25.5 | week 3 |
| 2. micrograd | [02-micrograd.md](02-micrograd.md) | 14 | week 5 |
| 3. makemore | [03-makemore.md](03-makemore.md) | 33.5 | week 8 |
| 4. GPT | [04-gpt.md](04-gpt.md) | 37.5 | week 12 |
| 5. Hardware & kernels | [05-hardware.md](05-hardware.md) | 30 | week 15 |
| 6. Capstone & next | [06-capstone-and-next.md](06-capstone-and-next.md) | 5.5 | week 15 |
| **Total** | | **149** | |

**Math:** you don't need to remember any math to start. Phase 1 starts from functions and slopes.
There are four *anchor derivations* (Sessions 1.5, 2.2, 2.3, 3.14) that you do on paper and
check in code. Everything else is intuition.

**Hardware:** your Mac (Apple Silicon) handles everything through Phase 4. Phase 5 uses a rented
NVIDIA GPU for CUDA and Triton, about $10 in total (free Colab covers part of it).

## Progress

| Phase | Started | Finished | Project done |
|---|---|---|---|
| 0. Setup | | | — |
| 1. Math | | | |
| 2. micrograd | | | |
| 3. makemore | | | |
| 4. GPT | | | |
| 5. Hardware | | | |
| 6. Capstone | | | — |

## When you're stuck

1. **Re-check the "Done when"** and the session's **Sticking points**.
2. **Compare with the reference code:** Karpathy's finished notebooks are in
   [nn-zero-to-hero](https://github.com/karpathy/nn-zero-to-hero). Compare *after* trying, not before.
3. **Read the video's YouTube comments** for that lecture. Common bugs are usually discussed there.
4. **Ask an AI assistant to explain, not to solve.** For example: "explain why my gradient shape is
   wrong", not "write this for me". Paste your code and the error.
5. **Ask the community** (below).
6. **Stuck for more than a day?** Write down what you tried, skip ahead one session, and come back.
   It often clicks later.

## Community

You don't have to do this alone. The learning communities for the core resources:
- **Neural Networks: Zero to Hero Discord:** [discord.gg/3zy8kqD9Cp](https://discord.gg/3zy8kqD9Cp), linked from Karpathy's lecture descriptions.
- **GPU MODE Discord:** [discord.gg/gpumode](https://discord.gg/gpumode), for CUDA, Triton, and performance (Phase 5).
- **nanochat:** the [GitHub Discussions](https://github.com/karpathy/nanochat/discussions) tab and a `#nanochat` channel on the Zero to Hero Discord.
- Karpathy's series page: [karpathy.ai/zero-to-hero](https://karpathy.ai/zero-to-hero.html).

## About this repo

- `docs/design.md` — the design behind this guide (goals, choices, constraints).
- `tools/check_guide.py` — checks every session's format, the hour budgets, and that all links are
  live: `python3 tools/check_guide.py 0*.md --total 120 160 --links`.
