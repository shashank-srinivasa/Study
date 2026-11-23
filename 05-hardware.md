# Phase 5 — Where hardware meets software: GPUs, kernels, profiling (~30 h)

**What this phase answers:** *why* is one model fast and another slow? Why did Karpathy's GPT-2
step time drop from 1000 ms to 93 ms in Session 4.14? You'll learn to reason about GPUs from first
principles (compute, memory bandwidth, overhead). Then you'll write real GPU kernels in CUDA and
Triton, and profile your own GPT.

**The resources:**
- Horace He, ["Making Deep Learning Go Brrrr From First Principles"](https://horace.io/brrr_intro.html). Widely recommended as the best short introduction.
- Selected [GPU MODE](https://www.youtube.com/@GPUMODE) lectures. GPU MODE is a large community for learning GPU programming; materials are in [gpu-mode/lectures](https://github.com/gpu-mode/lectures).
- Simon Boehm, ["How to Optimize a CUDA Matmul Kernel for cuBLAS-like Performance"](https://siboehm.com/articles/22/CUDA-MMM), with code in [SGEMM_CUDA](https://github.com/siboehm/SGEMM_CUDA).
- The official [Triton tutorials](https://triton-lang.org/main/getting-started/tutorials/index.html).

**Optional reference text:** [*Programming Massively Parallel Processors*](https://shop.elsevier.com/books/programming-massively-parallel-processors/hwu/978-0-323-91231-0) (Hwu, Kirk, El Hajj; paid), the standard CUDA textbook. GPU MODE's early lectures follow it. Look things up in it when a session's explanation isn't enough, for example on memory coalescing or shared-memory tiling.

**Hardware for this phase:**
- **Your Mac** for Sessions 5.1–5.2 (concepts and micro-benchmarks).
- **An NVIDIA GPU in the cloud** for everything with CUDA or Triton. Your Mac can't run those.
  - **Free:** [Google Colab](https://colab.research.google.com/signup) with a T4 GPU. Good for Sessions 5.3–5.4. Some newer Triton features may not support the T4's older architecture.
  - **Recommended for 5.5 onwards:** a [RunPod](https://www.runpod.io/pricing) RTX 4090, listed at **$0.34/hour** (community cloud; secure cloud is $0.89) and billed per second. Prices checked 2026-11-23; they change. Pick a PyTorch template so CUDA, `nvcc`, and Triton are already installed.
  - **Expected total cost:** about 25 GPU hours across the phase, roughly **$10** at the community rate.
  - **⚠️ Terminate the pod when you finish a session.** A forgotten running pod keeps billing. A merely *stopped* pod still bills for its disk, and on community cloud its GPU can be taken by someone else while it's stopped. So treat pods as disposable.
  - **Keep your code on your Mac, in git.** Moving files to and from a pod: `scp -P <port> train_gpt2.py input.txt root@<pod-ip>:/workspace/` going up, and the same with the paths swapped coming back (traces, `PROFILE.md`). RunPod shows the exact SSH command on the pod's "Connect" panel. The pod's Jupyter upload/download buttons work too.
  - **If RunPod has no capacity:** use [Lambda](https://lambda.ai/pricing) or [Vast.ai](https://vast.ai/pricing). Any single NVIDIA GPU from the RTX 30-series or newer, or an A100/H100, works for this phase. Check the current hourly price before starting.

---

### Session 5.1 — Compute, bandwidth, overhead (~2 h)
- [ ] Done
**Goal:** the three things that determine how fast any GPU code runs, and how to tell which one is your bottleneck.
**Resource:** Horace He, ["Making Deep Learning Go Brrrr From First Principles"](https://horace.io/brrr_intro.html) (all sections: Compute, Bandwidth, Overhead).
**Do:**
1. Read the whole post. Summarize each of the three components in 2 lines.
2. On your Mac (`device = "mps"`), time `x * 2` (elementwise) and `A @ B` (matmul) for sizes 1024, 2048, and 4096. Call `torch.mps.synchronize()` before stopping the timer, otherwise you only time the launch.
3. For each case, compute the achieved GB/s (elementwise: bytes read plus bytes written, divided by time) and TFLOPS (matmul: `2·N³` divided by time).
4. Time 1,000 tiny ops (for example `x + 1` on a 10-element tensor) in a loop, and estimate the per-op overhead.
**Done when:** you have a small table showing elementwise ops are limited by bandwidth (low FLOPS), big matmuls are limited by compute (high FLOPS), and tiny ops are limited by overhead.
**Sticking points:** Without `torch.mps.synchronize()`, your timings will be meaninglessly fast, because GPU work runs asynchronously. This is the most common benchmarking mistake. The CUDA equivalent is `torch.cuda.synchronize()`.
**Knowledge check:**
- What is "arithmetic intensity", and why does it decide whether an op is limited by compute or by memory?
- Why does fusing `x.cos().cos()` into one kernel make it about twice as fast?
- How would you tell if your training is overhead-bound?

### Session 5.2 — GPU architecture and memory hierarchy (~2 h)
- [ ] Done
**Goal:** a mental model of a GPU: streaming multiprocessors, threads/blocks/warps, and the memory hierarchy.
**Resource:** GPU MODE ["Lecture 4 Compute and Memory Basics"](https://www.youtube.com/watch?v=lTmYrKwjSOU); slides in [gpu-mode/lectures `lecture_004`](https://github.com/gpu-mode/lectures).
**Do:**
1. Watch the lecture. Draw the GPU memory hierarchy (registers → shared memory/L1 → L2 → global HBM) with rough sizes and speeds.
2. Draw a *roofline* plot by hand for an RTX 4090. Look up its peak FP32 TFLOPS and memory bandwidth from NVIDIA's published specs. Place elementwise add and a large matmul on it.
3. Compare with the CDN world: where is the "cache hierarchy" analogy accurate, and where does it break?
**Done when:** you have your memory-hierarchy drawing and your roofline plot with two ops placed correctly.
**Knowledge check:**
- What is a warp, and why do threads in a warp want to do the same thing?
- What lives in shared memory, and who can see it?
- On a roofline plot, what does the "ridge point" mean?

### Session 5.3 — Getting started with CUDA (~2 h)
- [ ] Done
**Goal:** write your first CUDA kernels, called from Python.
**Resource:** GPU MODE ["Lecture 3: Getting Started With CUDA for Python Programmers"](https://www.youtube.com/watch?v=4sgKnKbR-WE) (Jeremy Howard), with its Colab notebook linked from the [gpu-mode/lectures README](https://github.com/gpu-mode/lectures) ("Lecture 3").
**Do:**
1. Open the lecture's Colab notebook and switch the runtime to a T4 GPU.
2. Code along: the RGB→grayscale kernel, then matrix multiplication as a CUDA kernel via `load_inline`.
3. Compare your kernel's output and speed against PyTorch.
**Done when:** your grayscale and matmul kernels give the same results as PyTorch (`torch.allclose`), and you've timed both.
**Sticking points:** The first `load_inline` compile is slow (a minute or more). That's normal. If compilation fails, read the *first* compiler error, not the last.
**Knowledge check:**
- How do `blockIdx`, `blockDim`, and `threadIdx` combine to give each thread its element?
- Why do you need an `if (i < n)` guard in the kernel?
- Why is your naive matmul kernel much slower than `torch.matmul`?

### Session 5.4 — CUDA C without Python (~2 h)
- [ ] Done
**Goal:** understand plain CUDA C: memory allocation, launching kernels, and synchronization.
**Resource:** NVIDIA, ["An Even Easier Introduction to CUDA"](https://developer.nvidia.com/blog/even-easier-introduction-cuda/).
**Do:**
1. In Colab (T4), use `%%writefile add.cu` and `!nvcc add.cu -o add` to follow the tutorial: CPU version, then 1 thread, then 256 threads, then many blocks.
2. Time each version with `nvprof` or `nsys`, whichever the tutorial and Colab support. Record the speedups.
3. Write a SAXPY kernel (`y = a·x + y`) from scratch, and compute its achieved bandwidth.
**Done when:** your table shows the speedup from 1 thread to many blocks, and your SAXPY reaches a reasonable fraction of the T4's memory bandwidth (published at 320 GB/s).
**Knowledge check:**
- What does unified memory (`cudaMallocManaged`) do?
- Why must you call `cudaDeviceSynchronize()` before reading results?
- Is SAXPY compute-bound or memory-bound, and why?

### Session 5.5 — Optimizing matmul, part 1: coalescing and shared memory (~2.5 h)
- [ ] Done
**Goal:** see why memory access patterns matter by optimizing matrix multiplication step by step.
**Resource:** Simon Boehm's article, sections **Kernel 1 (Naive)**, **Kernel 2 (Global Memory Coalescing)**, **Kernel 3 (Shared Memory Cache-Blocking)**; code in [SGEMM_CUDA](https://github.com/siboehm/SGEMM_CUDA).
**Do:**
1. Start a RunPod RTX 4090 pod with a PyTorch template.
2. Clone SGEMM_CUDA, then build and run it following its README.
3. Read Kernel 1, run it, and record GFLOPS.
4. Read Kernel 2. **Before running it,** predict the speedup. Then run it.
5. Read Kernel 3, run it, and record GFLOPS.
6. **Stop the pod.**
**Done when:** you have GFLOPS for kernels 1–3 on your GPU, and can explain why kernel 2 beats kernel 1. (On his RTX A6000: 309 → 1,987 → 2,980 GFLOPS. Your absolute numbers will differ; compare the ratios.)
**Sticking points:** If the build fails, check that `nvcc --version` works and that you're on an NVIDIA pod. Adjust the CUDA architecture flag in the build config to match your GPU (the 4090 is `sm_89`).
**Knowledge check:**
- What is memory coalescing, and why does thread ordering change speed?
- How does shared memory cache-blocking reduce global memory traffic?
- Why is the naive kernel memory-bound even though matmul has high arithmetic intensity?

### Session 5.6 — Optimizing matmul, part 2: tiling and vectorization (~2.5 h)
- [ ] Done
**Goal:** see how computing more results per thread raises arithmetic intensity and approaches cuBLAS.
**Resource:** Boehm's article, **Kernel 4 (1D Blocktiling)**, **Kernel 5 (2D Blocktiling)**, **Kernel 6 (Vectorized memory access)**.
**Do:**
1. Start your pod. Read and run kernels 4, 5, and 6, recording GFLOPS for each.
2. Run cuBLAS (kernel 0) and compute each kernel as a percentage of cuBLAS.
3. Plot GFLOPS for kernels 0–6 as a bar chart.
4. **Stop the pod.**
**Done when:** your bar chart shows the climb toward cuBLAS (Boehm reports 36.5%, 68.7%, and 78.4% for kernels 4–6), and you can explain what each kernel changed.
**Knowledge check:**
- Why does 2D blocktiling raise arithmetic intensity?
- What does vectorized loading (`float4`) save?
- Why does cuBLAS still win? What's left to optimize?

### Session 5.7 — Matmul: autotuning and warptiling (optional) (~2 h)
- [ ] Done
**Goal:** see the final steps to about 94% of cuBLAS.
**Resource:** Boehm's article, **Kernel 9 (Autotuning)**, **Kernel 10 (Warptiling)**, and the work-in-progress notes.
**Do:**
1. Read both sections. Optionally run them on your pod (and stop it after).
**Done when:** you can explain warptiling in one paragraph.
**Knowledge check:**
- What does autotuning search over?
- What does warptiling add on top of blocktiling?
- What does Boehm list as remaining ideas?

### Session 5.8 — Profiling PyTorch and your GPT (~2 h)
- [ ] Done
**Goal:** find out where your own model's time goes, using a real profiler.
**Resource:** GPU MODE ["Lecture 1 How to profile CUDA kernels in PyTorch"](https://www.youtube.com/watch?v=LuhJEEJQgUM); the [PyTorch profiler recipe](https://docs.pytorch.org/tutorials/recipes/recipes/profiler_recipe.html).
**Do:**
1. Watch the lecture.
2. Copy your `train_gpt2.py` (Session 4.15) to the pod. Run 20 training steps inside `torch.profiler.profile(activities=[CPU, CUDA])`.
3. Print `key_averages().table(sort_by="cuda_time_total", row_limit=15)`. Export a Chrome trace and open it in [Perfetto](https://ui.perfetto.dev/).
4. In `~/ai-learning/PROFILE.md`, write down the top 5 kernels by GPU time and which part of your model each comes from.
5. **Stop the pod.**
**Done when:** `PROFILE.md` names the top 5 kernels, maps each to your model code, and says whether each is compute- or memory-bound.
**Knowledge check:**
- In the trace, where are the gaps where the GPU is idle, and what causes them?
- What fraction of time is matmul vs. everything else?
- What would you optimize first, based on the profile?

### Session 5.9 — The GPT-2 speedups, for real (~2 h)
- [ ] Done
**Goal:** apply the Session 4.14 speedups on a real NVIDIA GPU, and measure each one.
**Resource:** "Let's reproduce GPT-2 (124M)", [01:22:18–02:14:55](https://www.youtube.com/watch?v=l8pRSuU81PU) (rewatch sections as needed); [build-nanogpt](https://github.com/karpathy/build-nanogpt) commits.
**Do:** first, set up a fair baseline on your pod:
- In a copy of your `train_gpt2.py`, switch back to the manual attention (not `scaled_dot_product_attention`) and set the vocab back to 50257. Alternatively, check out the matching early commit of [build-nanogpt](https://github.com/karpathy/build-nanogpt).
- Use `B=16, T=1024`, which fits a 24 GB RTX 4090 in float32. Drop to `B=8` if you run out of memory.
- Set gradient accumulation to 1.
- Record ms/step.

Then add one change at a time, recording ms/step and tokens/sec after each:
1. TF32: `torch.set_float32_matmul_precision("high")`.
2. bfloat16 autocast.
3. `torch.compile(model)`.
4. `F.scaled_dot_product_attention` (FlashAttention).
5. Vocab padded to 50304.
6. Re-profile with the final version and compare with Session 5.8. **Stop the pod.**
**Done when:** your table shows the cumulative speedup on your GPU, and you've added the before/after profile comparison to `PROFILE.md`.
**Knowledge check:**
- Which change gave the biggest speedup on your GPU, and why?
- What did `torch.compile` change in the profiler trace?
- Why does FlashAttention help memory as well as speed?

### Session 5.10 — Triton: your first kernels (~2 h)
- [ ] Done
**Goal:** write GPU kernels in Python with Triton, and see kernel fusion pay off.
**Resource:** Triton tutorials ["Vector Addition"](https://triton-lang.org/main/getting-started/tutorials/01-vector-add.html) and ["Fused Softmax"](https://triton-lang.org/main/getting-started/tutorials/02-fused-softmax.html).
**Do:**
1. On your pod, run `python -c "import triton; print(triton.__version__)"`. PyTorch templates include Triton.
2. Type the vector-add tutorial and run its benchmark.
3. Type the fused-softmax tutorial and run its benchmark against `torch.softmax` and the naive version.
4. **Stop the pod.**
**Done when:** both tutorials run, your vector add matches PyTorch's speed, and your fused softmax clearly beats the naive PyTorch softmax in the benchmark plot.
**Knowledge check:**
- In Triton, what does one "program" handle, compared with one CUDA thread?
- What does `tl.load(..., mask=...)` protect against?
- Why is the fused softmax faster than the naive one? (Count the memory reads and writes.)

### Session 5.11 — Triton, in practice (~2 h)
- [ ] Done
**Goal:** a practitioner's view of Triton: debugging, how its blocks map to the GPU, and common patterns.
**Resource:** GPU MODE ["Lecture 14: Practitioners Guide to Triton"](https://www.youtube.com/watch?v=DdTsX6DQk24); notebook `lecture_014/A_Practitioners_Guide_to_Triton.ipynb` in [gpu-mode/lectures](https://github.com/gpu-mode/lectures).
**Do:**
1. Watch the lecture, and run the notebook on your pod alongside it.
2. Try the interpreter/debug mode the lecture shows, to step through a kernel.
3. **Stop the pod.**
**Done when:** you've run the notebook's examples and used the debug mode at least once.
**Knowledge check:**
- How do you debug a Triton kernel?
- When should you reach for Triton instead of CUDA?
- What does `tl.constexpr` mean for a parameter?

### Session 5.12 — Triton matmul (~2 h)
- [ ] Done
**Goal:** write a high-performance matmul in Triton, and compare it with your CUDA journey.
**Resource:** Triton tutorial ["Matrix Multiplication"](https://triton-lang.org/main/getting-started/tutorials/03-matrix-multiplication.html).
**Do:**
1. Type and run the tutorial on your pod, including its benchmark against cuBLAS.
2. Find in the code where it does the blocktiling you learned from Boehm, and the "grouped ordering" for L2 cache reuse.
3. **Stop the pod.**
**Done when:** your Triton matmul runs and benchmarks within reach of cuBLAS, and you've annotated where tiling and L2 grouping happen.
**Knowledge check:**
- What does Triton handle for you that you did by hand in CUDA?
- Why does grouped ordering improve L2 hit rate?
- How many lines was the Triton matmul, compared with Boehm's best kernel?

### Session 5.13 — FlashAttention (~2 h)
- [ ] Done
**Goal:** understand FlashAttention, the classic example of redesigning an algorithm around the memory hierarchy.
**Resource:** GPU MODE ["Lecture 12: Flash Attention"](https://www.youtube.com/watch?v=zEuwuCTEf_0).
**Do:**
1. Watch the lecture.
2. On paper, compute how many bytes standard attention reads and writes for `T = 4096`, `d = 64` in fp16 (counting the `T×T` score matrix), compared with FlashAttention, which never stores it.
3. Explain the "online softmax" trick in your own words, and check it with a small NumPy implementation that computes a softmax in chunks.
**Done when:** your chunked-softmax NumPy code matches the regular softmax to about 1e-6, and you can explain why FlashAttention is faster even though it does *more* computation.
**Knowledge check:**
- What memory does FlashAttention save, and why is that the bottleneck?
- How does the online softmax combine chunks correctly?
- Connect this to Horace He's post: which of the three components does FlashAttention attack?

### Session 5.14 — CUDA performance checklist (optional) (~1.5 h)
- [ ] Done
**Goal:** a checklist of the standard CUDA optimizations.
**Resource:** GPU MODE ["Lecture 8: CUDA Performance Checklist"](https://www.youtube.com/watch?v=SGhfUhlowB4).
**Do:**
1. Watch it. Map each checklist item to something you saw in Boehm's kernels or the Triton tutorials.
**Done when:** you have a written checklist with an example from your own work next to each item.
**Knowledge check:**
- What is occupancy, and is higher always better?
- What is thread coarsening?
- What is a bank conflict?

### Session 5.15 — Project: a fused kernel for your GPT, part 1 (~2.5 h)
- [ ] Done
**Goal:** without a tutorial, write a Triton kernel for one operation in your GPT and prove it's correct.
**Resource:** [Triton language reference](https://triton-lang.org/main/python-api/triton.language.html) (reference only); your `PROFILE.md`.
**Do:**
1. Using your profile, pick an op that is memory-bound and isn't a matmul. Good candidates are LayerNorm (forward) or the GELU in the MLP. Explain your choice in `PROFILE.md`.
2. Write the Triton kernel in `~/ai-learning/kernels/fused_<op>.py`.
3. Write `test_fused_<op>.py` with pytest. Compare against the PyTorch op with `torch.testing.assert_close` for several shapes, including shapes that aren't multiples of your block size.
4. **Stop the pod.**
**Done when:** all correctness tests pass, including the odd shapes.
**Knowledge check:**
- Why did you choose this op, based on your profile?
- How did you handle shapes that don't divide evenly by the block size?
- What tolerance did you use, and why is the result not bit-exact?

### Session 5.16 — Project: a fused kernel for your GPT, part 2 (~2.5 h)
- [ ] Done
**Goal:** benchmark your kernel, plug it into your GPT, and measure the end-to-end effect.
**Resource:** [`triton.testing.do_bench`](https://triton-lang.org/main/python-api/generated/triton.testing.do_bench.html) (reference only).
**Do:**
1. Benchmark your kernel against PyTorch eager *and* `torch.compile` across sizes, and plot the results.
2. Replace the PyTorch op in your GPT's forward pass with your kernel. (Forward-only is fine for inference; if you're training, keep PyTorch's version for backward, or write a backward kernel as a stretch goal.)
3. Measure ms per forward pass before and after, and re-profile.
4. Finish `PROFILE.md`: the problem, your kernel, correctness evidence, micro-benchmark, end-to-end result, and an honest conclusion. It's fine if `torch.compile` beats you, as long as you explain why.
5. **Stop the pod.**
**Done when:** `PROFILE.md` is complete with numbers, plots, and your explanation, and your GPT still generates correct text with your kernel in place.
**Knowledge check:**
- Did your kernel beat PyTorch eager? `torch.compile`? Why or why not?
- How big was the end-to-end gain compared with the micro-benchmark gain, and why do they differ?
- What would you optimize next?
