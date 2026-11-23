# Phase 4 — GPT: build a Transformer, a tokenizer, and GPT-2 (~37.5 h)

**What you'll build:**
1. A GPT (Transformer) from scratch that writes Shakespeare-like text.
2. A tokenizer like the ones GPT-4 and Claude-style models use.
3. A reproduction of GPT-2 (124M) code, trained in reduced form on your Mac.
4. A tiny ChatGPT-style model trained end to end on your Mac with Karpathy's **nanochat**.

**The resources:** Karpathy's *Zero to Hero* lectures 7–9:
- ["Let's build GPT: from scratch, in code, spelled out."](https://www.youtube.com/watch?v=kCc8FmEb1nY), about 1 h 56 min. Code: [ng-video-lecture](https://github.com/karpathy/ng-video-lecture).
- ["Let's build the GPT Tokenizer"](https://www.youtube.com/watch?v=zduSFxRajkE), about 2 h 13 min. Code: [minbpe](https://github.com/karpathy/minbpe).
- ["Let's reproduce GPT-2 (124M)"](https://www.youtube.com/watch?v=l8pRSuU81PU), about 4 h. Code: [build-nanogpt](https://github.com/karpathy/build-nanogpt), one commit per step.

You'll also use [nanochat](https://github.com/karpathy/nanochat). **Note:** the
[nanoGPT](https://github.com/karpathy/nanoGPT) README now says nanoGPT is "very old and deprecated" and
points to nanochat instead. This guide follows that advice. (Checked 2026-11-23.)

**Optional companion book:** Sebastian Raschka, [*Build a Large Language Model (From Scratch)*](https://www.manning.com/books/build-a-large-language-model-from-scratch) (paid), with free code at [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch). It covers the same ground in writing (tokenization, attention, GPT, pretraining, fine-tuning). Use it if you learn better from text, or to re-read a session's topic another way. Engineers on Hacker News repeatedly recommend it (see the README's "Evidence" section).

**Device:** from now on, use your Mac's GPU: `device = "mps" if torch.backends.mps.is_available() else "cpu"`.
Karpathy trains on NVIDIA A100/H100 GPUs, so expect your runs to take longer. When a run would take
hours, shrink the model (fewer layers, smaller `n_embd`, shorter context). The ideas are identical.

---

### Session 4.1 — Data, tokens, and a bigram baseline (~2 h)
- [ ] Done
**Goal:** set up the Shakespeare dataset, a character tokenizer, and batching, then a bigram baseline.
**Resource:** "Let's build GPT" **00:00:00–00:34:53**.
**Do:**
1. Download [tiny Shakespeare](https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt) (about 1.1 MB) into `~/ai-learning/gpt/`.
2. Code along: the character vocabulary, `encode`/`decode`, a 90/10 train/val split, and `get_batch` with `block_size` and `batch_size`.
3. Build the `BigramLanguageModel` as an `nn.Module` with `generate()`.
**Done when:** `decode(encode("hii there")) == "hii there"`, `get_batch` returns shapes `(B, T)`, and your untrained bigram model generates random characters.
**Knowledge check:**
- What do `x` and `y` in a batch look like, and why is `y` just `x` shifted by one?
- Why does one chunk of length `block_size` hold `block_size` training examples?
- What is the expected starting loss for a 65-character vocabulary?

### Session 4.2 — Training the baseline and the "averaging" trick (~2 h)
- [ ] Done
**Goal:** train the bigram model, then learn the matrix trick at the heart of attention.
**Resource:** "Let's build GPT" **00:34:53–01:00:18**.
**Do:**
1. Train the bigram model with AdamW, then move it to a script, `bigram.py`, using `device = "mps"`.
2. Code versions 1–3 of "average the past context": for loops, then a lower-triangular matrix multiply, then a masked softmax.
3. Check that all three versions give the same result with `torch.allclose`.
**Done when:** your bigram val loss reaches about 2.5, and all three averaging versions match.
**Knowledge check:**
- Why does multiplying by a lower-triangular matrix of averages "look only at the past"?
- Why fill masked positions with `-inf` before the softmax?
- What's the weakness of giving every past token equal weight?

### Session 4.3 — Self-attention (~2 h)
- [ ] Done
**Goal:** implement self-attention: queries, keys, values, and the scaled dot product. This is the crux of the Transformer.
**Resource:** "Let's build GPT" **01:00:18–01:19:11**.
**Do:**
0. Optional but recommended for building intuition first: watch 3Blue1Brown's ["Attention in transformers, step-by-step"](https://www.youtube.com/watch?v=eMlx5fFNoYc) (about 26 min). It shows visually what you're about to code.
1. Add positional embeddings.
2. Implement a single attention `Head`: `q = query(x)`, `k = key(x)`, `wei = q @ k.transpose(-2, -1) * head_size**-0.5`, then mask, softmax, and `@ v`.
3. Pause on each of notes 1–6 and write a one-line summary of each.
4. Note his correction in the description: normalize by `head_size`, not `C`.
**Done when:** your `Head` produces output of shape `(B, T, head_size)`, and you can explain why it divides by `sqrt(head_size)`.
**Knowledge check:**
- In your own words, what do the query, key, and value represent? Connect this to dot products as similarity (Session 1.8).
- Why does attention need positional embeddings at all?
- What makes it "self"-attention versus cross-attention?

### Session 4.4 — The Transformer block (~2 h)
- [ ] Done
**Goal:** assemble a full Transformer block: multi-head attention, feedforward, residual connections, and LayerNorm.
**Resource:** "Let's build GPT" **01:19:11–01:37:49**.
**Do:**
1. Plug a single head into the model and train. Then add `MultiHeadAttention`.
2. Add the feedforward layer, then stack blocks into `Block`.
3. Add residual connections and projections, then LayerNorm (pre-norm).
4. After each addition, retrain briefly and write down the val loss.
**Done when:** you have a table of val losses for each step, and adding residuals plus LayerNorm visibly helps.
**Knowledge check:**
- Why do residual connections make deep networks trainable?
- How does LayerNorm differ from the BatchNorm you built in Session 3.11?
- What does attention do, compared with the feedforward layer? (Karpathy: "communication" vs. "computation".)

### Session 4.5 — Scale it up on your GPU (~2 h)
- [ ] Done
**Goal:** scale up the model, add dropout, train on MPS, and connect it to how ChatGPT is made.
**Resource:** "Let's build GPT" **01:37:49–end**.
**Do:**
1. Add dropout and the hyperparameter variables.
2. Train the scaled-up model on `mps`. If it's too slow, cut `n_layer`/`n_head` from 6 to 4 and `n_embd` from 384 to 256.
3. Generate 500 characters.
4. Watch the encoder/decoder, nanoGPT walkthrough, and "pretraining vs. finetuning, RLHF" sections. Write down the 3 stages of making ChatGPT.
**Done when:** your val loss falls clearly below the bigram's 2.5 (his full-size run reaches about 1.48), and your samples look like Shakespeare-ish English.
**Sticking points:** If you see an MPS error about an unsupported operation, set `PYTORCH_ENABLE_MPS_FALLBACK=1` before running. That op will then run on the CPU. Use `torch.manual_seed` for repeatable runs.
**Knowledge check:**
- Which parameters most affect model size, and how do you count them?
- What is dropout, and why does it reduce overfitting?
- What are the stages from a pretrained GPT to an assistant like ChatGPT or Claude?

### Session 4.6 — Exercise: all heads in parallel (~2 h)
- [ ] Done
**Goal:** master n-dimensional tensors by rewriting multi-head attention so that all heads run at once.
**Resource:** the "Suggested exercises" in the [video description](https://www.youtube.com/watch?v=kCc8FmEb1nY), **EX1**.
**Do:**
1. Without looking at nanoGPT, merge `Head` and `MultiHeadAttention` into one `CausalSelfAttention` class. Use a single linear layer for q, k, v, and treat heads as an extra batch dimension: shape `(B, nh, T, hs)`.
2. Check that it gives the same outputs as your old version when given the same weights. Call `model.eval()` first so dropout is off. To copy weights: stack each old head's `query`, `key`, and `value` weight matrices into the right rows of your single `c_attn` layer (all heads' q, then all k, then all v), matching the order your `.view()` splits them.
3. Then compare your code with the `CausalSelfAttention` class in [build-nanogpt](https://github.com/karpathy/build-nanogpt) `train_gpt2.py`.
4. Replace the manual attention with `F.scaled_dot_product_attention(q, k, v, is_causal=True)`, and check that the output still matches.
**Done when:** your batched version matches the original to about 1e-6, and so does the `scaled_dot_product_attention` version.
**Knowledge check:**
- What do `.view()` and `.transpose(1, 2)` do to get the heads into their own dimension?
- Why is the batched version faster on a GPU?
- What does `is_causal=True` replace in your code?

### Session 4.7 — Tokenization: Unicode and BPE (~2 h)
- [ ] Done
**Goal:** understand why LLMs use tokens instead of characters, and how Byte Pair Encoding works.
**Resource:** "Let's build the GPT Tokenizer" **00:00:00–00:39:20**; the [tiktokenizer web app](https://tiktokenizer.vercel.app/).
**Do:**
1. Play with tiktokenizer: try English, code, numbers, and another language. Note the token counts.
2. Code along: `ord()`, UTF-8 bytes, counting pairs, merging the most common pair.
3. Add the training loop and compute the compression ratio.
**Done when:** your BPE trainer runs on a paragraph of text, and you can report its compression ratio for a vocabulary of 276 (256 bytes + 20 merges).
**Knowledge check:**
- Why do tokenizers work on UTF-8 bytes rather than Unicode code points?
- What does one BPE merge step do?
- Why does a model count "tokens", and why does that matter for cost and context length (for example, in the tools you use every day)?

### Session 4.8 — Encode and decode (~2 h)
- [ ] Done
**Goal:** finish a working tokenizer that turns text into tokens and back.
**Resource:** "Let's build the GPT Tokenizer" **00:39:20–00:57:36**.
**Do:**
1. Draw the tokenizer/LLM diagram from the video. The tokenizer is a separate stage, trained on its own data.
2. Implement `decode(ids)`, and handle invalid UTF-8 with `errors="replace"`.
3. Implement `encode(text)` by applying merges in the order they were learned.
**Done when:** `decode(encode(s)) == s` holds for 10 different strings, including emoji and non-English text.
**Knowledge check:**
- Why can decoding an arbitrary list of tokens produce invalid UTF-8?
- Why must `encode` apply merges in training order?
- Why might a tokenizer trained mostly on English be worse for other languages?

### Session 4.9 — Regex splitting, tiktoken, and special tokens (~2 h)
- [ ] Done
**Goal:** understand how real tokenizers (GPT-2, GPT-4) differ from the basic version.
**Resource:** "Let's build the GPT Tokenizer" **00:57:36–01:25:28**; [tiktoken](https://github.com/openai/tiktoken).
**Do:**
1. Study the GPT-2 split regex and try it with `regex.findall` on sample text (`uv pip install regex`).
2. `uv pip install tiktoken`, then compare GPT-2 and GPT-4 (`cl100k_base`) token counts on a Python code snippet.
3. Look at special tokens such as `<|endoftext|>`.
**Done when:** you can show, with an example, why GPT-4's tokenizer uses fewer tokens on code with lots of whitespace.
**Knowledge check:**
- Why split text with a regex before BPE?
- What is a special token, and how is it used?
- What does `cl100k_base`'s vocabulary size mean for the model's embedding table?

### Session 4.10 — Exercise: build your own GPT-4 tokenizer (~2.5 h)
- [ ] Done
**Goal:** implement a full tokenizer, step by step, following Karpathy's exercise.
**Resource:** [minbpe `exercise.md`](https://github.com/karpathy/minbpe/blob/master/exercise.md).
**Do:**
1. Follow `exercise.md` steps 1–4 in your own repo: `BasicTokenizer`, then `RegexTokenizer`, then the GPT-4 equivalence check, then special tokens.
2. Only look at the minbpe code once you're stuck for more than 20 minutes on a step.
**Done when:** your `RegexTokenizer` with GPT-4's merges encodes test strings to **exactly** the same ids as `tiktoken.get_encoding("cl100k_base")`.
**Knowledge check:**
- What was the trickiest difference between your implementation and tiktoken?
- How does training on different text change the merges you learn?
- Why is tokenization behind so many odd LLM behaviors (spelling, arithmetic, trailing spaces)?

### Session 4.11 — SentencePiece, vocab size, and tokenizer quirks (~2 h)
- [ ] Done
**Goal:** see how vocabulary size trades off, and why tokenization explains many odd LLM behaviors.
**Resource:** "Let's build the GPT Tokenizer" **01:25:28–end** (skim the SentencePiece configuration part).
**Do:**
1. Watch the vocab size and "new tokens" sections. Note where the vocab size shows up in your `gpt.py`.
2. Watch "quirks of LLM tokenization". For 3 of them, reproduce the tokenization in tiktokenizer and explain the quirk.
**Done when:** you have written explanations of 3 quirks with token-level evidence.
**Knowledge check:**
- What are the costs of a very large vocabulary? And of a very small one?
- Why do LLMs struggle to reverse or spell words?
- What is "SolidGoldMagikarp", and what does it say about tokenizer and model training data?

### Session 4.12 — GPT-2: the model and loading OpenAI's weights (~2 h)
- [ ] Done
**Goal:** write the GPT-2 model class and load the real OpenAI GPT-2 (124M) weights into it.
**Resource:** "Let's reproduce GPT-2 (124M)" **00:00:00–00:41:47**; [build-nanogpt](https://github.com/karpathy/build-nanogpt) commit history.
**Do:**
1. `uv pip install transformers tiktoken`.
2. Explore the Hugging Face GPT-2 checkpoint (parameter names and shapes).
3. Write `GPT`, `Block`, `MLP`, and `CausalSelfAttention` in `train_gpt2.py` (reuse your Session 4.6 class).
4. Implement `from_pretrained`, then the sampling loop.
**Done when:** your own model class, with OpenAI's weights, completes "Hello, I'm a language model," with coherent English on your Mac.
**Sticking points:** Some weights in the checkpoint are stored transposed (they come from `Conv1D`). He handles this explicitly. If your outputs are gibberish, check this first.
**Knowledge check:**
- How many layers, heads, and embedding dimensions does GPT-2 small have?
- How does your Session 4.4 block differ from GPT-2's block?
- What does top-k sampling do?

### Session 4.13 — GPT-2: training from scratch (~2 h)
- [ ] Done
**Goal:** train GPT-2 from random weights: device detection, loss, data loader, weight tying, and initialization.
**Resource:** "Let's reproduce GPT-2 (124M)" **00:41:47–01:22:18**.
**Do:**
1. Add device auto-detection (he includes MPS).
2. Compute the cross-entropy loss and check the initial loss is about `−ln(1/50257) ≈ 10.8`.
3. Overfit a single batch, then write `DataLoaderLite` using tiny Shakespeare.
4. Tie `wte` and `lm_head` weights, and add GPT-2 initialization (std 0.02, scaled residual init).
5. Train a few hundred steps on MPS with small `B` and `T` (for example `B=4, T=256`).
**Done when:** your initial loss is about 10.8, the loss decreases steadily on MPS, and you can explain weight tying.
**Sticking points:** Karpathy's code is written for NVIDIA GPUs. On your Mac, replace every `torch.cuda.synchronize()` with `torch.mps.synchronize()` (otherwise you'll get "Torch not compiled with CUDA enabled"). The `fused=True` AdamW option and the bfloat16 autocast branch only apply on CUDA, so leave them off locally. You'll turn them on in Phase 5 on a real NVIDIA GPU.
**Knowledge check:**
- Why is the initial loss about 10.8?
- What does weight tying share, and how many parameters does it save?
- Why scale down the init of residual projections by `1/sqrt(2 × n_layer)`?

### Session 4.14 — Making it fast (watch and take notes) (~2 h)
- [ ] Done
**Goal:** understand the GPU speedups for training (precision, `torch.compile`, FlashAttention). This is your bridge to Phase 5.
**Resource:** "Let's reproduce GPT-2 (124M)" **01:22:18–02:14:55**.
**Do:**
1. Watch the whole section and note each speedup with its time per step (1000 ms → 333 → 300 → 130 → 96 → 93 ms).
2. For each, write one line on *why* it's faster: less memory traffic, Tensor Cores, fewer Python launches, kernel fusion, or "nice" numbers.
3. On your Mac, time your training step before and after switching to `F.scaled_dot_product_attention`, and padding the vocab to 50304. Call `torch.mps.synchronize()` before reading the timer. GPU work is asynchronous, so without it you only measure how long it took to *launch* the work. (Phase 5 Session 5.1 explains why.)
**Done when:** you have a table of each speedup with its reason, and your own before/after timing on MPS.
**Sticking points:** TF32, bfloat16 autocast, and `torch.compile` behave differently on MPS than on CUDA, and some may not help. That's expected. Phase 5 runs them on a real NVIDIA GPU.
**Knowledge check:**
- Why does lowering precision speed up training even when you aren't compute-bound?
- What does kernel fusion save?
- Why is 50304 a "nicer" number than 50257?

### Session 4.15 — Optimization, scaling, and evaluation (~2.5 h)
- [ ] Done
**Goal:** learn the training recipe for real LLMs: AdamW, gradient clipping, learning-rate schedule, gradient accumulation, distributed training, datasets, and evaluation.
**Resource:** "Let's reproduce GPT-2 (124M)" **02:14:55–end**.
**Do:**
1. Implement gradient clipping, warmup + cosine decay, and weight decay in your `train_gpt2.py`.
2. Implement gradient accumulation to simulate a bigger batch on your Mac.
3. Watch the DDP, FineWeb, and HellaSwag sections without running them. Write a paragraph on how training is split across 8 GPUs.
4. Watch the results section.
**Done when:** your script has a working LR schedule (plot it) and gradient accumulation, and training with `grad_accum_steps=4` gives a loss close to the same run with a 4× bigger batch.
**Knowledge check:**
- Why warm up the learning rate at the start?
- How does gradient accumulation give the same result as a bigger batch?
- What does DDP do with gradients after each backward pass? (Compare with replicating state across CDN nodes.)

### Session 4.16 — From GPT to assistant: how LLMs like Claude are made (~1.5 h)
- [ ] Done
**Goal:** the big picture of pretraining, fine-tuning, and RLHF, so you can place your GPT next to a real assistant.
**Resource:** Karpathy ["[1hr Talk] Intro to Large Language Models"](https://www.youtube.com/watch?v=zjkBMFhNj_g).
**Do:**
1. Watch the talk.
2. Draw a diagram with 3 stages (pretraining → supervised fine-tuning → RLHF) and label which parts you've now built yourself.
3. Write down what an "agent" with tools (like Claude Code) adds on top of the model.
**Done when:** your diagram is complete, and you can explain to a colleague how Claude Code differs from your Shakespeare GPT.
**Knowledge check:**
- What does pretraining produce, and why isn't it an assistant yet?
- What is RLHF trying to change about the model?
- What are the main security risks of LLMs mentioned in the talk?

### Session 4.17 — Deep dive into LLMs (optional) (~2.5 h)
- [ ] Done
**Goal:** a longer, more detailed tour of the whole LLM pipeline, including RL and reasoning models.
**Resource:** Karpathy ["Deep Dive into LLMs like ChatGPT"](https://www.youtube.com/watch?v=7xTGNNLPyMI) (about 3.5 h; split it across days).
**Do:**
1. Watch in chunks and add details to your Session 4.16 diagram.
**Done when:** your diagram includes the reinforcement-learning stage and how "thinking" models are trained.
**Knowledge check:**
- What is a "base model" vs. an "instruct model"?
- Why do LLMs hallucinate, and what are mitigations?
- How does reinforcement learning on verifiable problems (math, code) differ from RLHF?

### Session 4.18 — Train a tiny ChatGPT on your Mac with nanochat (~2.5 h)
- [ ] Done
**Goal:** run the *whole* pipeline (tokenizer → pretraining → fine-tuning → chat) end to end on your own machine.
**Resource:** [nanochat](https://github.com/karpathy/nanochat) README section "Running on CPU / MPS", and [`runs/runcpu.sh`](https://github.com/karpathy/nanochat/blob/master/runs/runcpu.sh).
**Do:**
1. `git clone https://github.com/karpathy/nanochat ~/ai-learning/nanochat`, then read `runs/runcpu.sh` top to bottom first.
2. `cd ~/ai-learning/nanochat`, deactivate your guide venv (`deactivate`), then run the script's setup block first: `export NANOCHAT_BASE_DIR="$HOME/.cache/nanochat"`, `uv venv`, `uv sync --extra cpu`, `source .venv/bin/activate`. This creates a separate environment just for nanochat. That's expected, so don't install nanochat into `~/ai-learning/.venv`.
3. Then run the remaining commands **one at a time** as the script suggests: dataset download, tokenizer training, `base_train` (tuned for about 30 min on an M3 Max), then `chat_sft` (about 10 min).
4. Chat with it using `python -m scripts.chat_cli -p "What is the capital of France?"`.
5. While it trains, open `nanochat/gpt.py` and find each piece you built yourself: attention, MLP, embeddings.
**Done when:** your model answers a chat prompt (badly is fine), and you've matched at least 5 pieces of nanochat's model code to code you wrote earlier.
**Sticking points:** The script downloads several data shards and uses disk space under `~/.cache/nanochat`, so check your free space first. The script itself says not to expect strong results on a laptop. The point is seeing the whole pipeline work.
**Knowledge check:**
- Which stage took the most compute, and why?
- What changed in the model's behavior between `base_train` and `chat_sft`?
- What would you need to make it actually good? (Look at the README's GPU speedrun section.)

### Session 4.19 — Project: your own GPT, your own data (~2.5 h)
- [ ] Done
**Goal:** without a video, train a GPT on data you chose, with your own BPE tokenizer.
**Resource:** your code from this phase; Karpathy's EX2 in the ["Let's build GPT" description](https://www.youtube.com/watch?v=kCc8FmEb1nY) for ideas.
**Do:** pick **one**:
- **A. Your own corpus.** Gather at least 1 MB of text you care about (for example, a public-domain author you like, or documentation in a field you know). Train your Session 4.10 tokenizer on it with vocab around 1,000–4,000, then train your GPT with it on MPS.
- **B. Addition (EX2).** Train a GPT to do `a+b=c` with reversed digits and loss masking (`ignore_index`), and measure accuracy on held-out problems.

For either option, write `RESULTS.md`: your data, tokenizer, model size, training curve plot, final val loss (or accuracy), samples, and the 3 things you'd try next.
**Done when:** (A) the val loss is clearly below a bigram baseline on the same tokens and the samples resemble your data; or (B) held-out accuracy is above 90% on 2-digit addition. In both cases, `RESULTS.md` is complete.
**Knowledge check:**
- How did your tokenizer's vocabulary size affect the model and the loss?
- What was the biggest bottleneck in training time, and how do you know?
- What does this project tell you about the importance of data vs. model size?
