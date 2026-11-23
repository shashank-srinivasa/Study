# Phase 6 — Capstone and where to go next (~5.5 h)

You've built backprop, language models, a GPT, a tokenizer, a GPT-2 reproduction, a tiny ChatGPT,
and GPU kernels. This phase pulls it together, checks what you really know, and helps you choose
what to go deep on next.

---

### Session 6.1 — Read the Transformer paper (~2 h)
- [ ] Done
**Goal:** read the original Transformer paper and match it to code you wrote.
**Resource:** Vaswani et al., ["Attention Is All You Need"](https://arxiv.org/abs/1706.03762) (2017).
**Do:**
1. Read the paper with your Session 4.6 `CausalSelfAttention` and Session 4.12 `train_gpt2.py` open beside it.
2. For every equation and figure in Section 3, write down the file and line in your code that implements it.
3. List what GPT differs on: decoder-only, pre-norm, learned positional embeddings, GELU.
**Done when:** every part of Section 3 is mapped to your code or marked "GPT does this differently because…".
**Knowledge check:**
- What is Equation 1 of the paper, in your own words?
- Why did the original Transformer have an encoder *and* a decoder, while GPT has only a decoder?
- Which parts of the paper did you find you already understood without effort? (That's what the last 3 months bought.)

### Session 6.2 — Teach it: explain LLMs to your team (~2 h)
- [ ] Done
**Goal:** find any gaps in your understanding by explaining it, and share it with the people around you.
**Resource:** your notes, `RESULTS.md` files, and `PROFILE.md` from Phases 3–5.
**Do:**
1. Prepare a 20-minute talk: **"How an LLM actually works, from a CDN engineer's view"**. Cover tokens → embeddings → attention → next-token probabilities → sampling, then training, then why inference is limited by memory bandwidth.
2. Include one analogy from your field: KV cache vs. HTTP caching, request batching vs. dynamic batching, or HBM bandwidth vs. network egress.
3. Give the talk to teammates or a friend. Write down every question you couldn't answer well.
**Done when:** you've given the talk, and you have a list of questions you couldn't answer well, each with the guide session (or new resource) that would answer it.
**Knowledge check:**
- Which question from the audience surprised you most?
- Which analogy to CDN work held up, and which broke down?
- What would you change in the talk next time?

### Session 6.3 — Self-assessment and choosing your next path (~1.5 h)
- [ ] Done
**Goal:** check honestly what you can now do, and pick one direction for the next 3–6 months.
**Resource:** the checklist and paths below.
**Do:**
1. Go through the self-assessment checklist below and tick what's true. For anything unticked, note the session to revisit.
2. Read the three paths below and pick **one**. Write a one-page plan: why this path, the first 3 resources, and a project you'd like to build.
**Done when:** your checklist is filled in, and your one-page next-path plan exists.
**Knowledge check:**
- Which checklist items are you least confident about, and why?
- Why did you pick this path over the other two?
- What is the smallest version of your next project that would still teach you something?

---

## Self-assessment checklist

**I have built:**
- [ ] My own micrograd (autograd + MLP) trained on a new dataset (Session 2.7)
- [ ] A character-level language model on my own data, with RESULTS.md (Session 3.16)
- [ ] A GPT from scratch, trained on my Mac (Sessions 4.1–4.5)
- [ ] A BPE tokenizer that matches GPT-4's tokenizer exactly (Session 4.10)
- [ ] GPT-2 (124M) code that loads OpenAI's weights and trains from scratch (Sessions 4.12–4.15)
- [ ] A tiny ChatGPT trained end to end with nanochat (Session 4.18)
- [ ] A CUDA matmul progression and a Triton kernel benchmarked and plugged into my GPT (Sessions 5.5–5.16)
- [ ] All four anchor derivations, done on paper and checked in code (Sessions 1.5, 2.2, 2.3, 3.14)

**I can explain, without notes:**
- [ ] How an LLM turns my prompt into a response, step by step
- [ ] What training is: loss, gradients, backprop, optimizer
- [ ] Why training fails, and how initialization, normalization, and residuals help
- [ ] How pretraining, fine-tuning, and RLHF differ
- [ ] Why a given model is fast or slow: compute vs. memory vs. overhead, plus the roofline model
- [ ] What FlashAttention and kernel fusion do, and why they help

**I can now:**
- [ ] Read "Attention Is All You Need" and map it to code
- [ ] Read real model code (nanochat, Hugging Face models) and follow it
- [ ] Profile a PyTorch model and identify its bottleneck

## Where to go next — pick one path

### Path A: Autonomy, vision, robotics (toward FSD-style systems)
- [Stanford CS231n](https://cs231n.stanford.edu/) — Deep Learning for Computer Vision. The standard vision course.
- [Sutton & Barto, *Reinforcement Learning: An Introduction*](http://incompleteideas.net/book/the-book-2nd.html) (2nd ed., free online). The standard RL textbook.
- [Hugging Face LeRobot](https://github.com/huggingface/lerobot) — open-source imitation learning and robotics, with training code and datasets.
- [comma.ai openpilot](https://github.com/commaai/openpilot) — an open-source driver-assistance system running real end-to-end driving models. The closest open project to FSD-style software.
- *Project idea:* train an imitation-learning policy in simulation with LeRobot, or study openpilot's model inputs and outputs and write up how its driving model works.

### Path B: ML systems and performance (builds most directly on your CDN experience)
- [Stanford CS149 — Parallel Computing](https://gfxcourses.stanford.edu/cs149/fall25)
- [*Programming Massively Parallel Processors*](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) (Hwu, Kirk, El Hajj). The standard CUDA book. GPU MODE's early lectures follow it.
- ["How to Scale Your Model"](https://jax-ml.github.io/scaling-book/) — a free book on scaling LLM training and inference (TPUs, parallelism, rooflines).
- [MIT 6.5940 — TinyML and Efficient Deep Learning](https://hanlab.mit.edu/courses/2024-fall-65940) (Song Han). Quantization, pruning, and efficient inference.
- [vLLM](https://github.com/vllm-project/vllm) and [SGLang](https://github.com/sgl-project/sglang) — production LLM inference servers. Read how they schedule requests and manage the KV cache. It will feel familiar.
- [llm.c](https://github.com/karpathy/llm.c) — GPT-2 training in raw C/CUDA.
- *Project idea:* build a minimal LLM inference server for your nanochat model with continuous batching and a KV cache, and benchmark latency and throughput the way you would a CDN service.

### Path C: Language models, deeper
- [Stanford CS336 — Language Modeling from Scratch](https://stanford-cs336.github.io/). A rigorous, assignment-heavy follow-up to everything in Phase 4.
- [nanochat](https://github.com/karpathy/nanochat) — go beyond the CPU run. Try the GPU speedrun on a rented 8×H100 node, or contribute improvements.
- [Hugging Face LLM Course](https://huggingface.co/learn/llm-course) — working with real pretrained models, fine-tuning, and the ecosystem.
- *Project idea:* fine-tune a small open model on a task you care about, and measure it against a baseline.
