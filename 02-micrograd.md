# Phase 2 — micrograd: build backpropagation yourself (~14 h)

**The resource:** Andrej Karpathy's *Neural Networks: Zero to Hero*, lecture 1:
["The spelled-out intro to neural networks and backpropagation: building micrograd"](https://www.youtube.com/watch?v=VMj-3S1tku0)
(about 2 h 25 min). Code: [karpathy/micrograd](https://github.com/karpathy/micrograd); his notebooks
from the video are in [nn-zero-to-hero/lectures/micrograd](https://github.com/karpathy/nn-zero-to-hero/tree/master/lectures/micrograd).

**Why this lecture:** it is one of the most widely recommended explanations of backpropagation for
programmers. By the end you'll have written, from scratch, the core idea that PyTorch and every
model training run (including Claude's) rely on.

**How to work through it:** **type every line yourself** in your own notebook
(`~/ai-learning/02-micrograd.ipynb`). Don't download his notebook and press run. Pause the video
often. When something breaks, debug it before moving on. Timestamps below come from the video's
own chapter list.

**Device:** pure Python on CPU. No GPU needed in this phase.

---

### Session 2.1 — Derivatives, the micrograd way (~1.5 h)
- [ ] Done
**Goal:** see what micrograd is and redo derivatives numerically, as Karpathy does.
**Resource:** micrograd lecture **00:00:00–00:19:09** ("intro" through "derivative of a function with multiple inputs").
**Do:**
1. Watch 00:00–08:08 (overview). Don't code yet. Just get the big picture.
2. Watch 08:08–19:09 and code along: `f(x) = 3x² − 4x + 5` (your Phase 1 function!), the numeric slope, then the multi-input example `d = a*b + c`.
3. For `d = a*b + c`, before he reveals each answer, predict whether nudging `a`, `b`, or `c` raises or lowers `d`, and by how much.
**Done when:** your notebook reproduces his numeric derivatives, and your predictions for `d = a*b + c` were right (or you understand why they weren't).
**Knowledge check:**
- With `a = 2, b = −3, c = 10`, why is the derivative of `d` with respect to `a` equal to `b`?
- What's the derivative of `d` with respect to `c`, and why is it always 1?
- What is micrograd, in one sentence?

### Session 2.2 — The Value object and anchor derivation #2 (~2 h)
- [ ] Done
**Goal:** build the `Value` class and the graph visualization, then backpropagate through a small expression **by hand**.
**Resource:** micrograd lecture **00:19:09–00:52:52** ("starting the core Value object…" through "preview of a single optimization step").
**Do:**
1. Watch 19:09–32:10 and code the `Value` class (`__add__`, `__mul__`, `_prev`, `_op`) and `draw_dot`. Graphviz install: `brew install graphviz` and `uv pip install graphviz`.
2. **Anchor derivation #2 (on paper, before watching 32:10):** for `e = a*b`, `d = e + c`, `L = d*f` with `a=2, b=−3, c=10, f=−2`, compute `L` and then `dL/dd, dL/df, dL/de, dL/dc, dL/da, dL/db` by working backwards with the chain rule.
3. Now watch 32:10–51:10 and compare with your paper answers.
4. Check numerically: nudge each input by `h = 0.0001` in code and recompute `L`.
5. Watch 51:10–52:52 (the optimization-step preview).
**Done when:** your paper gradients are `dL/dd = −2, dL/df = 4, dL/de = −2, dL/dc = −2, dL/da = 6, dL/db = −4`, and your numeric checks agree.
**Sticking points:** `draw_dot` errors usually mean the Graphviz *system* binary is missing (`brew install graphviz`), not just the Python package. If you get stuck on the derivation, re-watch Session 1.4's chain-rule video. "Multiply the local slopes along the path" is all that's happening.
**Knowledge check:**
- Why do you compute gradients from the output *backwards*?
- For a `+` node, how does the gradient pass to its inputs? For a `*` node?
- What does `dL/da = 6` tell you about nudging `a` up slightly?

### Session 2.3 — A neuron, and anchor derivation #3 (~2 h)
- [ ] Done
**Goal:** backpropagate through a single neuron with a `tanh` activation, by hand.
**Resource:** micrograd lecture **00:52:52–01:09:02** ("manual backpropagation example #2: a neuron").
**Do:**
1. Watch until he has set up the neuron (`x1=2, x2=0, w1=−3, w2=1, b=6.8813735870195432`; `n = x1w1 + x2w2 + b`; `o = tanh(n)`). **Pause.**
2. **Anchor derivation #3 (on paper):** using `d/dn tanh(n) = 1 − tanh(n)²`, compute `do/dn`, then the gradients for `w1, w2, x1, x2, b`.
3. Watch the rest of the section and compare.
4. Check numerically in code by nudging each input.
**Done when:** your paper answers are `o ≈ 0.7071`, `do/dn = 0.5`, `do/dw1 = 1.0`, `do/dw2 = 0.0`, `do/dx1 = −1.5`, `do/dx2 = 0.5`, `do/db = 0.5`, and the numeric checks agree.
**Knowledge check:**
- Why is `do/dw2 = 0`? What does that mean for learning `w2` from this example?
- Why does the gradient of a weight depend on its input `x`?
- What does an "activation function" like `tanh` add to a neuron?

### Session 2.4 — Automatic backward pass (~2 h)
- [ ] Done
**Goal:** make backprop automatic: each operation knows its local derivative, and a topological sort runs them in order.
**Resource:** micrograd lecture **01:09:02–01:43:55** ("implementing the backward function for each operation" through "doing the same thing but in PyTorch").
**Do:**
1. Code `_backward` for `+`, `*`, and `tanh` (01:09–01:17).
2. Code `backward()` with topological sort (01:17–01:22). Run it on your neuron and check you get Session 2.3's gradients.
3. Watch the multiple-use bug (01:22–01:27). **Before he fixes it,** reproduce it with `b = a + a` and see the wrong gradient (1 instead of 2).
4. Add `exp`, division, subtraction, and `pow`, then rebuild `tanh` from them (01:27–01:39).
5. Install PyTorch if you haven't (Phase 0), and redo the neuron in PyTorch (01:39–01:43). Compare the gradients.
**Done when:** `o.backward()` on your neuron gives the same gradients as your paper (and as PyTorch), and `a + a` gives gradient 2.
**Sticking points:** Use `+=` for gradients, not `=`. That *is* the multiple-use fix. Forgetting it is the most common micrograd bug.
**Knowledge check:**
- Why must gradients *accumulate* (`+=`) rather than be assigned?
- Why do you need a topological order before calling each `_backward`?
- What is the same, and what's different, between your `Value` and a PyTorch tensor with `requires_grad=True`?

### Session 2.5 — A neural network library and training (~2 h)
- [ ] Done
**Goal:** build `Neuron`, `Layer`, and `MLP` classes and train a network with gradient descent.
**Resource:** micrograd lecture **01:43:55–02:14:03** ("building out a neural net library…" through "doing gradient descent optimization manually").
**Do:**
1. Code `Neuron`, `Layer`, `MLP` (01:43–01:51).
2. Create the tiny 4-example dataset and the squared-error loss (01:51–01:57).
3. Add `parameters()` (01:57–02:01).
4. Write the training loop (02:01–02:14). **Reproduce his bug** of forgetting to zero the gradients, then fix it.
5. Train until the loss is small. Print your predictions next to the targets.
**Done when:** your loss drops below about 0.01, and your predictions are close to `[1.0, −1.0, −1.0, 1.0]`.
**Sticking points:** If the loss goes up or jumps around, your learning rate is too big (try 0.05) or you forgot to zero the gradients before `backward()`.
**Knowledge check:**
- What are the three steps of every training iteration?
- What goes wrong if you don't reset `.grad` to 0 each iteration, and why?
- How many parameters does `MLP(3, [4, 4, 1])` have? Work it out, then check with `len(parameters())`.

### Session 2.6 — The real micrograd, PyTorch, and the exercises (~2 h)
- [ ] Done
**Goal:** connect your code to the real micrograd repo and PyTorch, and complete Karpathy's exercises.
**Resource:** micrograd lecture **02:14:03–end**; Karpathy's exercise Colab (linked in the video description under "Exercises"); [karpathy/micrograd](https://github.com/karpathy/micrograd) `micrograd/engine.py` and `nn.py`.
**Do:**
1. Watch 02:14–02:25.
2. Read `engine.py` and `nn.py` in the repo line by line. Note anything that differs from your version.
3. Open the exercise Colab from the video description. Save a copy to your Drive, and solve it without re-watching.
**Done when:** you've completed the exercise notebook, and can explain each line of `engine.py`.
**Knowledge check:**
- Why does the real micrograd use `relu` instead of `tanh` in its demo?
- Where in PyTorch's source is the backward pass for `tanh`, and what formula does it use?
- What would you need to add to micrograd to train on thousands of examples efficiently?

### Session 2.7 — Project: micrograd from memory (~2.5 h)
- [ ] Done
**Goal:** without the video or your old notebook, rebuild micrograd and train it on a dataset the lecture didn't use.
**Resource:** [scikit-learn `make_moons`](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_moons.html) (reference only; `uv pip install scikit-learn`).
**Do:**
1. In a new file, `~/ai-learning/mygrad.py`, write `Value` with `+ − * / pow exp tanh relu` and `backward()`, from memory. Peek only if stuck for more than 15 minutes, and write down what you had to peek at.
2. Write a `test_mygrad.py` that checks every operation's gradient against PyTorch on random inputs (tolerance 1e-6).
3. Generate 100 points with `make_moons(n_samples=100, noise=0.1)`. Labels should be ±1.
4. Train an `MLP(2, [16, 16, 1])` with a hinge or squared-error loss.
5. Plot the decision boundary with matplotlib (`contourf` over a grid).
**Done when:** your gradient tests pass, training accuracy is at least 95%, and your boundary plot visibly separates the two moons.
**Knowledge check:**
- Which part did you have to peek at, and why do you think it was the hard part?
- Why does this dataset need a hidden layer (why can't a single neuron separate it)?
- What did you change (learning rate, steps, width) to reach 95%, and what effect did each change have?
