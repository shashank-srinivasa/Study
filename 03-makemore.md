# Phase 3 — makemore: from counting to deep networks (~34 h)

**The resource:** Karpathy's *Zero to Hero* lectures 2–6, where you build "makemore", a model that
generates new names, character by character. Each lecture adds one idea that modern models use:
- Part 1: the bigram model, the loss function, and a first neural net.
- Part 2: embeddings and an MLP.
- Part 3: initialization and BatchNorm (why training breaks, and how to fix it).
- Part 4: doing backprop by hand on tensors.
- Part 5: a deeper, tree-shaped architecture.

Code: [karpathy/makemore](https://github.com/karpathy/makemore). Each lecture's finished notebook
is in [nn-zero-to-hero/lectures/makemore](https://github.com/karpathy/nn-zero-to-hero/tree/master/lectures/makemore).
The data file is `names.txt` from the makemore repo.

**This is the densest phase in the guide.** It's where training a neural network stops being
abstract and becomes something you can debug. Expect some sessions to run over. That's normal.

**Device:** use **CPU** for this whole phase (`device = "cpu"`, which is the default). These models
are tiny, and the overhead of moving data to your Mac's GPU usually makes them slower, not
faster. You'll switch to the GPU (`"mps"`) in Phase 4.

**How to work through it:** same rule as Phase 2. Type everything into your own notebook,
one notebook per lecture (`03-makemore-part1.ipynb` and so on). Timestamps come from each
video's own chapter list.

---

### Session 3.1 — Bigrams by counting (~2 h)
- [ ] Done
**Goal:** build the simplest language model: count which letter follows which.
**Resource:** ["The spelled-out intro to language modeling: building makemore"](https://www.youtube.com/watch?v=PaCmpygFfXo) **00:00:00–00:24:02**.
**Do:**
1. Download `names.txt` from [karpathy/makemore](https://github.com/karpathy/makemore) into `~/ai-learning/`.
2. Code along: read the dataset, count bigrams in a dict, then in a 27×27 `torch` tensor.
3. Recreate his bigram heatmap with matplotlib.
4. Switch to the single `.` start/end token.
**Done when:** your 27×27 count tensor's heatmap matches his, and `N[0].sum()` equals the number of names (32,033).
**Knowledge check:**
- What is a "bigram", in one sentence?
- Why does a single `.` token for start and end work as well as separate `<S>`/`<E>` tokens?
- What does row `a` of the count matrix tell you?

### Session 3.2 — Sampling and broadcasting (~2 h)
- [ ] Done
**Goal:** generate names from your bigram model, and learn tensor broadcasting, which you'll use for the rest of the guide.
**Resource:** makemore part 1 **00:24:02–00:50:14**.
**Do:**
1. Code the sampling loop with `torch.multinomial` and a seeded `torch.Generator`.
2. Normalize the rows with broadcasting: `P = N / N.sum(1, keepdim=True)`.
3. **Reproduce his bug** of leaving out `keepdim=True`. Check that the rows no longer sum to 1, then explain why.
**Done when:** with his seed (2147483647), you generate the same first few names as he does, and you can explain the `keepdim` bug.
**Sticking points:** Broadcasting rules are the most common confusion here. Pause the video and read [PyTorch's broadcasting semantics](https://docs.pytorch.org/docs/stable/notes/broadcasting.html). Then try small examples with shapes (27, 27) and (27, 1) versus (27,).
**Knowledge check:**
- What are the two broadcasting rules for aligning shapes?
- Why does `N.sum(1)` give shape `(27,)` but `N.sum(1, keepdim=True)` give `(27, 1)`?
- Why are the bigram model's names so bad?

### Session 3.3 — The loss function (~1.5 h)
- [ ] Done
**Goal:** measure how good a model is with negative log-likelihood, and see smoothing.
**Resource:** makemore part 1 **00:50:14–01:02:57**.
**Do:**
1. Compute the average negative log-likelihood of the whole dataset under your bigram model.
2. Find a name that gives infinite loss without smoothing (try "andrejq"), then add fake counts.
**Done when:** your average NLL is about **2.45**, and you can explain why smoothing removes `inf`.
**Knowledge check:**
- Why do you take the log of probabilities instead of multiplying them? (Remember Session 1.2.)
- Why is NLL the same thing as cross-entropy here?
- What would the loss be if every letter were equally likely? (Hint: `-log(1/27)`.)

### Session 3.4 — The same model as a neural net (~2 h)
- [ ] Done
**Goal:** replace counting with a one-layer neural network trained by gradient descent.
**Resource:** makemore part 1 **01:02:57–01:26:17**.
**Do:**
1. Build `(xs, ys)` training pairs.
2. Turn characters into one-hot vectors with `F.one_hot`.
3. Make a 27×27 weight matrix `W`, compute `logits = xenc @ W`, then softmax.
4. Write out what each step corresponds to in your Phase 1 toolkit (`matmul`, `softmax`).
**Done when:** you can run one forward pass and print a probability row that sums to 1.
**Knowledge check:**
- Why can't you feed the integer 5 straight into the network for the letter "e"?
- What do "logits" mean?
- Where in this code is your Phase 1 `softmax` function?

### Session 3.5 — Training it with PyTorch's autograd (~2 h)
- [ ] Done
**Goal:** train the neural bigram model with `loss.backward()` and match the counting model.
**Resource:** makemore part 1 **01:26:17–end**.
**Do:**
1. Vectorize the loss.
2. Set `W.requires_grad = True`, then run backward and update in a loop.
3. Train on the full dataset until the loss stops improving.
4. Note 1: check that `xenc @ W` for a one-hot `xenc` equals `W[ix]`.
5. Note 2: add the regularization term and see its effect.
6. Sample names from the neural net.
**Done when:** your loss settles near **2.45** (the same as counting), and the samples look like your counting model's.
**Knowledge check:**
- Why does the neural net end up at the same loss as counting?
- How is `loss.backward()` here the same as your micrograd `backward()`?
- How does the regularization term act like smoothing?

### Session 3.6 — Part 1 exercises (~2 h)
- [ ] Done
**Goal:** practice on your own with Karpathy's exercises.
**Resource:** the "Exercises" list in the [makemore part 1 video description](https://www.youtube.com/watch?v=PaCmpygFfXo) (E01–E05).
**Do:**
1. **E01:** train a trigram model (two characters in, the next one out). Does it beat 2.45?
2. **E02:** split the data 80/10/10 into train/dev/test, and evaluate on dev and test.
3. **E04:** replace `F.one_hot` with indexing into `W`.
4. **E05:** use `F.cross_entropy`, and check that you get the same loss.
5. E03 is optional.
**Done when:** your trigram's dev loss is below your bigram's dev loss, and E04 and E05 give the same loss as before.
**Knowledge check:**
- Why do you need a separate dev set, rather than judging on the training set?
- Why is `F.cross_entropy` preferred over writing softmax + log yourself?
- Your trigram is better. Why not use a 10-gram counting model?

### Session 3.7 — MLP: embeddings and the Bengio paper (~2 h)
- [ ] Done
**Goal:** understand the idea behind modern language models: learned **embeddings** (vectors for each token) fed to a neural net.
**Resource:** ["Building makemore Part 2: MLP"](https://www.youtube.com/watch?v=TCH_1BHY58I) **00:00:00–00:29:15**; [Bengio et al. 2003, "A Neural Probabilistic Language Model"](https://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf) (skim Section 1 and Figure 1).
**Do:**
1. Watch the paper walkthrough. Then skim the paper's Figure 1 yourself.
2. Rebuild the dataset with `block_size = 3`.
3. Make the embedding table `C`, with shape (27, 2), and index it with `C[X]`.
4. Build the hidden layer. Follow his digression on `.view()` and tensor storage.
**Done when:** `C[X].shape` is `(N, 3, 2)`, and you can explain what each dimension means.
**Knowledge check:**
- What is an embedding, and why is it better than a one-hot vector?
- Why does `.view()` cost nothing?
- How does a context of 3 characters fix the bigram model's main weakness?

### Session 3.8 — Training the MLP well (~2 h)
- [ ] Done
**Goal:** train the MLP with minibatches and a sensible learning rate.
**Resource:** makemore part 2 **00:29:15–00:53:20**.
**Do:**
1. Build the output layer and use `F.cross_entropy`.
2. Overfit one batch first. (This is an important debugging habit.)
3. Train with minibatches of 32.
4. Do his learning-rate sweep and plot loss against the exponent of the learning rate.
**Done when:** you can show a plot of your learning-rate sweep, and you trained with the learning rate you chose from it.
**Knowledge check:**
- Why "overfit a single batch" before training for real?
- What do you lose and gain with minibatches compared with the full dataset?
- What does a loss vs. learning-rate plot look like, and where should you pick?

### Session 3.9 — Splits, experiments, and part 2 exercises (~2.5 h)
- [ ] Done
**Goal:** proper train/val/test evaluation, and tuning the model yourself.
**Resource:** makemore part 2 **00:53:20–end**, plus the description's exercises **E01** and **E02**.
**Do:**
1. Split the data, make the hidden layer bigger, and make the embeddings bigger, as he does.
2. Visualize the 2-D embeddings. Do the vowels cluster?
3. **E02:** compute the loss you *should* get at initialization (`−ln(1/27) ≈ 3.30`), then fix your initialization to get close to it.
4. **E01:** tune the model to beat his validation loss of about 2.2.
**Done when:** your validation loss is at or below about 2.2, and your initial loss is about 3.3 rather than much higher.
**Knowledge check:**
- Why should the loss at initialization be about 3.30 for 27 characters?
- What's the sign of overfitting in train vs. val loss?
- Which change helped your validation loss the most?

### Session 3.10 — Initialization: why training goes wrong (~2 h)
- [ ] Done
**Goal:** see the problems a careless initialization causes (huge initial loss, saturated tanh) and fix them with Kaiming init.
**Resource:** ["Building makemore Part 3: Activations & Gradients, BatchNorm"](https://www.youtube.com/watch?v=P6sfmUTpUmc) **00:00:00–00:40:40**.
**Do:**
1. Fix the initial loss by scaling down the output layer.
2. Plot the histogram of tanh activations. Find the saturated ones (near ±1), then fix them.
3. Apply Kaiming init (`gain / sqrt(fan_in)`).
**Done when:** your tanh histogram is no longer piled up at ±1, and your validation loss improves on the lecture's own starter code that you ran at the start of the session. Compare against that, not your tuned Session 3.9 model.
**Knowledge check:**
- Why does a saturated tanh stop learning? (Think about its derivative from Session 2.3.)
- What problem does Kaiming initialization solve?
- What is a "dead neuron"?

### Session 3.11 — Batch normalization (~2 h)
- [ ] Done
**Goal:** understand BatchNorm: what it does, why it works, and why it's awkward.
**Resource:** makemore part 3 **00:40:40–01:18:35**.
**Do:**
1. Implement BatchNorm by hand: compute the batch mean and variance, normalize, then scale and shift with `gamma` and `beta`.
2. Add running mean and variance for inference.
3. Follow the ResNet-50 walkthrough, and note where BatchNorm appears.
**Done when:** your network trains with BatchNorm, and you can explain why inference needs the running statistics.
**Knowledge check:**
- What does BatchNorm do to a layer's activations?
- Why does BatchNorm make examples in a batch depend on each other, and why is that a problem?
- Why is the bias before a BatchNorm layer useless?

### Session 3.12 — PyTorch-ify and diagnose with visualizations (~2 h)
- [ ] Done
**Goal:** organize the code like `torch.nn`, and learn the four diagnostic plots that show whether a network is healthy.
**Resource:** makemore part 3 **01:18:35–end**.
**Do:**
1. Rebuild the network as `Linear`, `BatchNorm1d`, and `Tanh` classes.
2. Make all four plots: forward activations, backward gradients, parameter/gradient ratios, and update:data ratio over time.
3. Remove BatchNorm and see the plots go bad. Bring it back.
**Done when:** you have all four plots, and the update:data ratio sits near 1e-3 (about −3 on the log scale) for a healthy run.
**Knowledge check:**
- What does the update:data ratio tell you, and why is about 1e-3 healthy?
- Without any non-linearities, what is a deep network equivalent to?
- Which of the four plots would you check first if a new model wasn't learning?

### Session 3.13 — Backprop Ninja: the atomic graph (~2.5 h)
- [ ] Done
**Goal:** manually backpropagate through every tensor operation of the MLP. This is the hardest and most rewarding session in the guide.
**Resource:** ["Building makemore Part 4: Becoming a Backprop Ninja"](https://www.youtube.com/watch?v=q8SA3rM6ckI) **00:00:00–01:26:31**, and the lecture's Colab (linked in the video description).
**Do:**
1. Watch 00:00–13:01 (intro and starter code). Open the Colab and save a copy.
2. **Try exercise 1 yourself first.** For each line, write the gradient, then run the `cmp()` check. Only after you've tried a line should you watch his solution.
3. Watch his exercise 1 solution (13:01–01:26:31) for any lines you couldn't get.
**Done when:** every `cmp()` line in exercise 1 prints `exact: True` (or approximately True with a max difference around 1e-9).
**Sticking points:** Check shapes on every line. A gradient must have exactly the same shape as the tensor it belongs to. If shapes don't match, you're probably missing a `.sum(dim, keepdim=True)` from broadcasting, which is Session 3.2 coming back.
**Knowledge check:**
- When a tensor was broadcast in the forward pass, what has to happen to its gradient in the backward pass?
- What is the gradient of `a @ b` with respect to `a`? Check it with shapes.
- What did Karpathy mean by backprop being a "leaky abstraction"?

### Session 3.14 — Anchor derivation #4 and the remaining ninja exercises (~2.5 h)
- [ ] Done
**Goal:** derive the softmax + cross-entropy gradient on paper, then finish the backprop exercises.
**Resource:** makemore part 4 **01:26:31–end**.
**Do:**
1. **Anchor derivation #4 (on paper, before 01:26:31):** for logits `z`, `p = softmax(z)`, and loss `L = −log p_y`, show that `dL/dz_i = p_i − 1[i = y]`. In other words, the gradient is "the probabilities, minus 1 at the correct class."
2. Check it numerically: take random `z` of length 5 and target `y = 2`. Compare `F.softmax(z) − one_hot(y)` with a central-difference gradient of `F.cross_entropy`.
3. Do exercise 2 in the Colab using your result (remember to divide by the batch size), then compare with his solution.
4. Do exercises 3 (BatchNorm backward) and 4 (putting it together).
**Done when:** your derivation gives `p − onehot(y)`, the numeric check agrees to about 1e-6, and exercises 2–4 pass their `cmp()` checks.
**Sticking points:** The derivation splits into two cases, `i = y` and `i ≠ y`. Do them separately. Use `d/dz_i log Σⱼ e^{z_j} = p_i`.
**Knowledge check:**
- Why is `p − onehot(y)` such a satisfying result? What does it "push" the logits to do?
- Why does dividing by the batch size appear in the gradient?
- After this session, what does `loss.backward()` actually compute?

### Session 3.15 — WaveNet: going deeper (~2 h)
- [ ] Done
**Goal:** build a deeper, hierarchical model, and see the real development process of a neural net.
**Resource:** ["Building makemore Part 5: Building a WaveNet"](https://www.youtube.com/watch?v=t3YJ5hKiMQ0) (full video, about 56 min).
**Do:**
1. Code along: containers (`Sequential`), `block_size = 8`, then the hierarchical WaveNet structure.
2. **Find the BatchNorm1d bug** (around 38:50) before he explains it.
3. Scale up and train.
**Done when:** your validation loss gets close to **2.0**, better than your MLP from Session 3.9.
**Knowledge check:**
- How does WaveNet merge context, compared with the flat MLP?
- What was the BatchNorm1d bug, and why did it fail silently?
- How does "dilated causal convolution" relate to what you built?

### Session 3.16 — Project: makemore on your own data (~2.5 h)
- [ ] Done
**Goal:** without a video, train a character-level model on a dataset you chose, in a clean Python script (not a notebook).
**Resource:** [PyTorch `torch.nn` docs](https://docs.pytorch.org/docs/stable/nn.html) (reference only); a dataset of your choice with at least 5,000 items. A good default is city names from [GeoNames](https://download.geonames.org/export/dump/): `cities15000.zip` has about 25,000 cities, and the name is the second tab-separated column. Or use any word list you care about.
**Do:**
1. Make `~/ai-learning/makemore_mine.py`. It loads your data, builds the vocabulary from your data (it may not be 27 characters), and does a train/val/test split.
2. Use an MLP or WaveNet with `torch.nn` modules, Kaiming init, and BatchNorm.
3. Check that the initial loss is about `−ln(1/vocab_size)` before training.
4. Train, print the train and val loss, and save 20 samples to a text file.
5. Write a `RESULTS.md`: your data, model, final losses, what you tried, and what worked.
**Done when:** the script runs end to end with one command, the initial loss matches the expected value, the val loss clearly beats a bigram baseline you compute on the same data, and the samples look plausibly like your data.
**Knowledge check:**
- How did your vocabulary size change the expected initial loss?
- What was your biggest overfitting risk, and how did you check for it?
- If you had 10× more data, what would you change first?
