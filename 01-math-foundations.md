# Phase 1 — Math foundations (~26.5 h)

**Who this is for:** you haven't done math in about 10 years. That's fine. This phase starts from
"what is a function" and ends with you understanding, visually and intuitively, the math a
neural network uses. It isn't a math degree. It's exactly enough to make Phases 2–4 make sense.

**How to watch 3Blue1Brown:** pause often. After each video, write 3–5 lines in your own words
in a notebook (paper is best). If you can't, rewatch the confusing part. This habit matters
more than speed.

**Meaning first:** every session starts with a **Before this** block linking to [concept cards](01-concepts.md). Each card says *what* an idea is, *why* it exists, and *where it shows up in AI*, with a one-minute self-test. Don't skip them. Knowing a procedure without knowing its purpose is exactly the gap this phase closes. Start with Session 1.0.

**Your one rule for this phase:** don't skip the pen-and-paper parts. You'll do one of the
guide's four *anchor derivations* here. The other three come in Phases 2 and 3.

---

### Session 1.0 — Foundations check: arithmetic and algebra (~1 h)
- [ ] Done
**Goal:** find any gaps in the basics *before* they make later topics feel hard, and understand what each basic idea is for.
**Resource:** concept cards [C1 Negative numbers](01-concepts.md#c1--negative-numbers), [C2 Fractions, decimals, and division](01-concepts.md#c2--fractions-decimals-and-division), [C3 Order of operations](01-concepts.md#c3--order-of-operations), [C4 Variables and expressions](01-concepts.md#c4--variables-and-expressions), [C5 Equations and solving](01-concepts.md#c5--equations-and-solving); [Khan Academy — Pre-algebra](https://www.khanacademy.org/math/pre-algebra) for anything shaky.
**Do:**
1. For each of C1–C5, read "What it is" and "Why it exists", then do the self-test on paper **before** looking at the answer.
2. Mark each card ✅ (got it right and could explain why) or ❌.
3. For every ❌, use the card's "If shaky" search term on Khan Academy: watch the video and do practice until you get 5 in a row right.
4. Read C6 (function). It's the single most important idea in this phase, and Session 1.1 builds on it.
**Done when:** all five self-tests are ✅, and you can say in one sentence each what an expression is, what an equation is, and how they differ.
**Sticking points:** Being rusty here is completely normal after 10 years. Fixing a ❌ usually takes 15–30 minutes, not days.
**Knowledge check:**
- What is the difference between `2x + 1` and `2x + 1 = 7`?
- What does "solving" an equation actually find?
- Why do we need an agreed order of operations?

### Session 1.1 — Refresher: functions and graphs (~1.5 h)
- [ ] Done
**Goal:** remember what a function is, and how to read its graph.
**Before this:** [C4 Variables and expressions](01-concepts.md#c4--variables-and-expressions), [C5 Equations and solving](01-concepts.md#c5--equations-and-solving), [C6 Function](01-concepts.md#c6--function). Read each card and do its self-test. If one is shaky, fix it first. Then read C7 and C9 *after* this session's videos.
**Resource:** [Khan Academy — Algebra 1](https://www.khanacademy.org/math/algebra). Use the site search for **"functions"** and **"graphing quadratic functions"** and do the intro videos plus a few practice questions.
**Do:**
1. Watch the intro to functions and do 5–10 practice questions until they feel easy.
2. On paper, sketch `f(x) = x²`, `f(x) = 2x + 1`, and `f(x) = 3x² − 4x + 5` by plugging in x = −2…3.
3. Read [C9](01-concepts.md#c9--quadratic-functions-lowest-point-vs-solving): what a quadratic is, and the difference between *where it equals 0* and *where it is lowest*.
4. In a notebook (`~/ai-learning/01-math.ipynb`), plot the same three with matplotlib: `xs = np.linspace(-2, 3, 100); plt.plot(xs, 3*xs**2 - 4*xs + 5)`.
**Done when:** your hand sketch and your matplotlib plot of `3x² − 4x + 5` have the same shape, with the lowest point near x ≈ 0.67.
**Sticking points:** If the plotting code feels like the hard part, it isn't the point. Copy the pattern and change the formula.
**Knowledge check:**
- What does `f(3)` mean for `f(x) = 3x² − 4x + 5`, and what is it?
- Why is the graph of `x²` a "U" shape?
- What does the slope of `2x + 1` tell you about how the output changes when x changes?

### Session 1.2 — Refresher: exponents, logs, and Σ notation (~2 h)
- [ ] Done
**Goal:** be comfortable with `eˣ`, `log`, and `Σ`. These appear in almost every ML formula (softmax, the loss function).
**Before this:** [C3 Order of operations](01-concepts.md#c3--order-of-operations), [C6 Function](01-concepts.md#c6--function), [C10 Exponents](01-concepts.md#c10--exponents). Read each card and do its self-test. If one is shaky, fix it first. C11 and C12 are what this session teaches. Read them alongside.
**Resource:** [Khan Academy — Algebra 2](https://www.khanacademy.org/math/algebra2). Search for **"exponent properties"**, **"introduction to logarithms"**, and **"summation notation"**.
**Do:**
1. Exponents: work through the properties (`aᵐ·aⁿ = aᵐ⁺ⁿ`, `a⁰ = 1`, `a⁻ⁿ = 1/aⁿ`) until you can do the practice without looking.
2. Logs: understand `log` as "the exponent you need". Do the practice questions.
3. Σ: learn to read `Σᵢ₌₁ⁿ xᵢ` as "a for-loop that adds things up". In Python, write `sum(x[i] for i in range(n))` for a small list.
4. In your notebook, plot `np.exp(xs)` and `np.log(xs)` for positive `xs`.
**Done when:** without notes, you can compute `log₁₀(1000)`, `e⁰`, and `Σᵢ₌₁⁴ i²` (the answers are 3, 1, 30) and explain each.
**Knowledge check:**
- What is `log(a·b)` in terms of `log a` and `log b`? (This is why ML adds log-probabilities instead of multiplying probabilities.)
- Why is `eˣ` always positive?
- Translate `(1/n) Σᵢ xᵢ` into one line of Python. What everyday quantity is it?

### Session 1.3 — What a derivative actually is (~2 h)
- [ ] Done
**Goal:** the intuition that a derivative is a "local slope", the rate of change at a point.
**Before this:** [C2 Fractions, decimals, and division](01-concepts.md#c2--fractions-decimals-and-division), [C6 Function](01-concepts.md#c6--function), [C7 Graph of a function](01-concepts.md#c7--graph-of-a-function), [C8 Slope of a line](01-concepts.md#c8--slope-of-a-line). Read each card and do its self-test. If one is shaky, fix it first. C14 and C15 are what this session teaches. Read them after the videos.
**Resource:** 3Blue1Brown *Essence of calculus*: [Chapter 1 "The essence of calculus"](https://www.youtube.com/watch?v=WUvTyaaNkzM) and [Chapter 2 "The paradox of the derivative"](https://www.youtube.com/watch?v=9vKqVkMQHKk).
**Do:**
1. Watch Chapter 1. Write down the main idea in 3 lines.
2. Watch Chapter 2. Pause when he zooms in on a curve and say out loud what "dt" means.
3. In your notebook, define `f = lambda x: 3*x**2 - 4*x + 5`. Compute `(f(3 + h) - f(3)) / h` for `h = 1, 0.1, 0.01, 0.001`. Watch the value settle.
**Done when:** your printed values approach **14**, and you can explain why making `h` tiny gives the slope at x = 3.
**Knowledge check:**
- In plain words, what does "the derivative of f at x = 3 is 14" mean?
- Why can't we just set h = 0 in `(f(x+h) − f(x))/h`?
- If a derivative is negative at a point, what is the function doing there?

### Session 1.4 — Derivative rules and the chain rule (~2 h)
- [ ] Done
**Goal:** know the power rule, sum rule, product rule, and above all the **chain rule**, which is the core of backpropagation.
**Before this:** [C10 Exponents](01-concepts.md#c10--exponents), [C15 Derivative](01-concepts.md#c15--derivative), [C17 Function composition](01-concepts.md#c17--function-composition). Read each card and do its self-test. If one is shaky, fix it first. C16 and C18 are what this session teaches.
**Resource:** [Chapter 3 "Derivative formulas through geometry"](https://www.youtube.com/watch?v=S0_qX4VJhMQ) and [Chapter 4 "Visualizing the chain rule and product rule"](https://www.youtube.com/watch?v=YG15m2VwSjA).
**Do:**
1. Watch Chapter 3. On paper, derive `d/dx x² = 2x` the way he does.
2. Watch Chapter 4. Rewatch the chain rule section until you can explain the "nudge passes through" picture.
3. On paper, find the derivative of `g(x) = (2x + 1)²` using the chain rule. Check it numerically in the notebook with the same `h` trick as Session 1.3.
**Done when:** your paper answer for `g'(x)` is `4(2x + 1)`, and at x = 1 your numeric estimate is ≈ 12.
**Sticking points:** The chain rule clicks when you see it as "multiply the local slopes along the path". If the notation `dg/dx = dg/du · du/dx` confuses you, ignore the notation and focus on the nudge picture.
**Go deeper:** [*Mathematics for Machine Learning*](https://mml-book.github.io/book/mml-book.pdf) (free PDF), Chapter 5 "Vector Calculus", Sections 5.1–5.2 (only once the videos make sense).
**Knowledge check:**
- State the chain rule in one sentence, without symbols.
- Why does the product rule have two terms?
- If `y = f(g(x))`, which two slopes do you multiply to get `dy/dx`?

### Session 1.5 — e, exponentials, and anchor derivation #1 (~2 h)
- [ ] Done
**Goal:** understand why `eˣ` is special, and do your first anchor derivation.
**Before this:** [C10 Exponents](01-concepts.md#c10--exponents), [C15 Derivative](01-concepts.md#c15--derivative), [C16 Derivative rules](01-concepts.md#c16--derivative-rules-power-constant-multiple-sum). Read each card and do its self-test. If one is shaky, fix it first. C13 is what this session teaches.
**Resource:** [Chapter 5 "What's so special about Euler's number e?"](https://www.youtube.com/watch?v=m2MIpDrF7Es).
**Do:**
1. Watch Chapter 5.
2. **Anchor derivation #1 (on paper):** for `f(x) = 3x² − 4x + 5`, use the power rule and sum rule to get `f'(x)`. Evaluate it at x = 3.
3. **Check it in code:** compute the *central difference* `(f(x+h) − f(x−h)) / (2h)` at x = 3 with `h = 1e-4`, and compare it with your paper answer.
4. Repeat steps 2–3 at x = −2 and x = 0.5.
**Done when:** your paper formula is `f'(x) = 6x − 4`, and the numeric check matches at all three points to at least 4 decimal places (14, −16, −1).
**Sticking points:** This exact function opens Karpathy's micrograd lecture in Phase 2. You'll meet it again and recognize it.
**Knowledge check:**
- What is the derivative of `eˣ`, and why does that make `e` convenient?
- Why does the central difference usually beat `(f(x+h) − f(x))/h`?
- What does a numeric check prove, and what doesn't it prove, about a formula you derived by hand?

### Session 1.6 — Vectors and linear combinations (~2 h)
- [ ] Done
**Goal:** see vectors as both arrows and lists of numbers, and understand linear combinations.
**Before this:** [C1 Negative numbers](01-concepts.md#c1--negative-numbers), [C2 Fractions, decimals, and division](01-concepts.md#c2--fractions-decimals-and-division), [C7 Graph of a function](01-concepts.md#c7--graph-of-a-function). Read each card and do its self-test. If one is shaky, fix it first. C21 and C22 are what this session teaches.
**Resource:** 3Blue1Brown *Essence of linear algebra*: [Chapter 1 "Vectors"](https://www.youtube.com/watch?v=fNk_zzaMoSs) and [Chapter 2 "Linear combinations, span, and basis vectors"](https://www.youtube.com/watch?v=k7RM-ot2NWY).
**Do:**
1. Watch both chapters and write your 3-line summaries.
2. In NumPy, create `v = np.array([2, 1])` and `w = np.array([-1, 3])`. Compute `3*v + 2*w` by hand first, then in code.
3. Plot `v`, `w`, and `3v + 2w` as arrows with `plt.quiver` (or simple lines from the origin).
**Done when:** your hand result and NumPy agree (`[4, 9]`), and your plot shows `3v + 2w` as the "tip-to-tail" sum.
**Knowledge check:**
- What does it mean for a vector to be a "linear combination" of others?
- What is the span of two vectors that point in the same direction?
- In a neural network, a word or an image becomes a long vector. What do you think one number in that vector represents?

### Session 1.7 — Matrices as transformations (~2 h)
- [ ] Done
**Goal:** see a matrix as a function that transforms space. Matrix multiplication is doing one transformation after another.
**Before this:** [C4 Variables and expressions](01-concepts.md#c4--variables-and-expressions), [C6 Function](01-concepts.md#c6--function), [C21 Vector](01-concepts.md#c21--vector), [C22 Linear combination](01-concepts.md#c22--linear-combination). Read each card and do its self-test. If one is shaky, fix it first. C23 and C24 are what this session teaches.
**Resource:** [Chapter 3 "Linear transformations and matrices"](https://www.youtube.com/watch?v=kYB8IZa5AuE) and [Chapter 4 "Matrix multiplication as composition"](https://www.youtube.com/watch?v=XkY2DOUCWMU).
**Do:**
1. Watch both chapters. Write your summaries.
2. **Write matrix multiplication yourself** in plain Python (three nested loops) for two lists-of-lists. Test it against `np.array(A) @ np.array(B)` on a 2×3 times 3×2 example.
3. Use `time.perf_counter()` to time your loop version against NumPy on 200×200 random matrices.
**Done when:** your function matches NumPy, and you've seen NumPy run hundreds of times faster or more. Remember that gap: Phase 5 is about why it happens.
**Knowledge check:**
- What do the columns of a 2×2 matrix tell you about the transformation?
- Why does the order of matrix multiplication matter (AB ≠ BA)?
- For `A @ B` to work, what has to be true about their shapes, and what shape is the result?

### Session 1.8 — Dot products (~2 h)
- [ ] Done
**Goal:** understand the dot product as a "similarity" measurement. It is the heart of attention in Transformers.
**Before this:** [C21 Vector](01-concepts.md#c21--vector), [C24 Matrix multiplication and shapes](01-concepts.md#c24--matrix-multiplication-and-shapes). Read each card and do its self-test. If one is shaky, fix it first. C25 is what this session teaches.
**Resource:** [Chapter 9 "Dot products and duality"](https://www.youtube.com/watch?v=LyGKycYT2v0); optionally [Chapter 8 "Nonsquare matrices as transformations between dimensions"](https://www.youtube.com/watch?v=v8VSDg_WQlA) first.
**Do:**
1. Watch Chapter 9 (and Chapter 8 if you have time).
2. In NumPy, compute dot products between pairs of vectors that point the same way, opposite ways, and at right angles. Note the sign of each.
3. Compute *cosine similarity*, `a·b / (|a||b|)`, for the same pairs.
**Done when:** you can predict the sign of a dot product from a drawing of the two arrows before running the code.
**Go deeper:** [*Mathematics for Machine Learning*](https://mml-book.github.io/book/mml-book.pdf) (free PDF), Chapter 3 "Analytic Geometry", Sections 3.1–3.4 (norms, inner products, angles).
**Knowledge check:**
- What does a dot product of 0 mean geometrically?
- How is one entry of a matrix product `C = A @ B` a dot product?
- Why might "how much do these two vectors point the same way?" be a useful question for a language model?

### Session 1.9 — More linear algebra (optional) (~2 h)
- [ ] Done
**Goal:** a broader picture of linear algebra. Not required to continue.
**Before this:** [C23 Matrix as a transformation](01-concepts.md#c23--matrix-as-a-transformation), [C24 Matrix multiplication and shapes](01-concepts.md#c24--matrix-multiplication-and-shapes). Read each card and do its self-test. If one is shaky, fix it first.
**Resource:** [Chapter 7 "Inverse matrices, column space and null space"](https://www.youtube.com/watch?v=uQhTuRlWMxw), [Chapter 13 "Change of basis"](https://www.youtube.com/watch?v=P2LTAUO1TdA), [Chapter 14 "Eigenvectors and eigenvalues"](https://www.youtube.com/watch?v=PFDu9oVAE-g).
**Do:**
1. Watch any or all of them. Summarize each in 3 lines.
**Done when:** you can explain an eigenvector in one sentence.
**Knowledge check:**
- What is an eigenvector, geometrically?
- What does it mean for a matrix to have no inverse?
- What is a "basis"?

### Session 1.10 — Probability: Bayes and distributions (~2 h)
- [ ] Done
**Goal:** the intuition behind probabilities, conditional probability, and distributions. A language model outputs a probability distribution over the next token.
**Before this:** [C2 Fractions, decimals, and division](01-concepts.md#c2--fractions-decimals-and-division), [C12 Σ](01-concepts.md#c12--σ-sigma-notation-and-the-mean). Read each card and do its self-test. If one is shaky, fix it first. C26, C27 and C28 are what this session teaches.
**Resource:** 3Blue1Brown ["Bayes theorem, the geometry of changing beliefs"](https://www.youtube.com/watch?v=HZGCoVF3YvM) and ["Binomial distributions | Probabilities of probabilities, part 1"](https://www.youtube.com/watch?v=8idr1WZ1A7Q).
**Do:**
1. Watch the Bayes video. Redo his example on paper.
2. Watch the binomial distributions video.
3. In NumPy, simulate 10,000 rolls of a loaded die with `np.random.choice(6, size=10000, p=[...])` and plot a histogram. Check that the frequencies match your `p`.
**Done when:** you can explain P(A | B) with a concrete example, and your histogram matches the probabilities you chose.
**Knowledge check:**
- What must the probabilities in a distribution add up to?
- What is P(A | B) in plain words?
- A model says the next word is "cat" with 0.7 and "dog" with 0.2. What could the remaining 0.1 be?

### Session 1.11 — Cross-entropy: how models are scored (~2 h)
- [ ] Done
**Goal:** understand cross-entropy, the loss function used to train nearly every language model.
**Before this:** [C11 Logarithms](01-concepts.md#c11--logarithms), [C13 e and eˣ](01-concepts.md#c13--e-and-eˣ), [C26 Probability](01-concepts.md#c26--probability), [C27 Probability distribution](01-concepts.md#c27--probability-distribution). Read each card and do its self-test. If one is shaky, fix it first. C29 and C30 are what this session teaches.
**Resource:** 3Blue1Brown ["What is cross-entropy, and why is it used in ML? | Information theory, part 2"](https://www.youtube.com/watch?v=GlYgs6v2YfU).
**Do:**
1. Watch the video. Pause at each formula and write it down.
2. In NumPy, write `softmax(z) = np.exp(z) / np.exp(z).sum()`. Try `z = [2.0, 1.0, 0.1]` and check that the outputs sum to 1.
3. Write `cross_entropy(p, target_index) = -np.log(p[target_index])`. Compute it when the model is confident and right, unsure, and confident and wrong.
**Done when:** you can show with numbers that being confidently wrong gives a much bigger loss than being unsure.
**Sticking points:** If `softmax` overflows on large numbers (`exp(1000)` → `inf`), subtract `z.max()` first. You'll see Karpathy do the same thing.
**Go deeper:** [*Mathematics for Machine Learning*](https://mml-book.github.io/book/mml-book.pdf) (free PDF), Chapter 6 "Probability and Distributions", Sections 6.1–6.2.
**Knowledge check:**
- What does softmax do to a list of arbitrary numbers?
- Why does cross-entropy use `−log`, and what is it when the model gives the right answer probability 1?
- Why is "low loss" the goal of training?

### Session 1.12 — Neural networks, intuitively (~2 h)
- [ ] Done
**Goal:** the big picture of what a neural network is and how it learns, before you build one.
**Before this:** [C15 Derivative](01-concepts.md#c15--derivative), [C17 Function composition](01-concepts.md#c17--function-composition), [C18 Chain rule](01-concepts.md#c18--chain-rule), [C20 Minimum and gradient descent](01-concepts.md#c20--minimum-and-gradient-descent). Read each card and do its self-test. If one is shaky, fix it first. C19 is new here (see step 3).
**Resource:** 3Blue1Brown *Neural networks*: [Chapter 1 "But what is a neural network?"](https://www.youtube.com/watch?v=aircAruvnKk), [Chapter 2 "Gradient descent, how neural networks learn"](https://www.youtube.com/watch?v=IHZwWFHWa-w), [Chapter 3 "Backpropagation, intuitively"](https://www.youtube.com/watch?v=Ilg3gGewQ5U), [Chapter 4 "Backpropagation calculus"](https://www.youtube.com/watch?v=tIeHLnjs5U8).
**Do:**
1. Watch chapters 1–2. Write your summaries.
2. Watch chapters 3–4. In chapter 4, pause and copy the chain-rule expression into your notes. Point to where Session 1.4 shows up.
3. **Partial derivatives and the gradient:** read [C19](01-concepts.md#c19--partial-derivatives-and-the-gradient). For `f(x, y) = x·y + y`, compute ∂f/∂x and ∂f/∂y on paper, then check numerically: nudge only `x` by `h = 1e-4` (keeping `y` fixed), then only `y`. At (2, 3) both should be ≈ 3.
4. In your own words, write a 1-paragraph answer to: "How does a neural network learn?"
**Done when:** your partial-derivative check matches (≈ 3 and ≈ 3), and your paragraph uses the words *loss*, *gradient*, and *chain rule* correctly.
**Knowledge check:**
- What is a "weight", and what does training change?
- What is gradient descent, using a ball-on-a-hill picture?
- Why is backpropagation "just the chain rule"?

### Session 1.13 — Project: your NumPy math toolkit (~2.5 h)
- [ ] Done
**Goal:** without a video, build a tiny toolkit of the math you've learned, and prove each piece works.
**Before this:** [C9 Quadratic functions](01-concepts.md#c9--quadratic-functions-lowest-point-vs-solving), [C12 Σ](01-concepts.md#c12--σ-sigma-notation-and-the-mean), [C20 Minimum and gradient descent](01-concepts.md#c20--minimum-and-gradient-descent), [C24 Matrix multiplication and shapes](01-concepts.md#c24--matrix-multiplication-and-shapes), [C29 Softmax](01-concepts.md#c29--softmax), [C30 Cross-entropy](01-concepts.md#c30--cross-entropy-negative-log-likelihood). Read each card and do its self-test. If one is shaky, fix it first. This project uses all of them. Skim the self-tests first.
**Resource:** [NumPy user guide](https://numpy.org/doc/stable/user/index.html) (reference only).
**Do:** create `~/ai-learning/mathkit.py` with these functions, plus a `test_mathkit.py` that checks each one using `pytest` (`uv pip install pytest`):
1. `numeric_derivative(f, x, h=1e-5)` using a central difference. Test it on `3x² − 4x + 5` at x = 3 (expect ≈ 14).
2. `matmul(A, B)` using plain Python loops. Test it against `np.array(A) @ np.array(B)` on random 3×4 and 4×2 inputs.
3. `softmax(z)`, numerically stable. Test that outputs sum to 1, and that `softmax([1000, 1000])` returns `[0.5, 0.5]` without `nan`.
4. `cross_entropy(p, target)`. Test that a perfect prediction gives ≈ 0 and a 50/50 guess gives ≈ 0.693.
5. `gradient_descent(f, x0, lr, steps)`, which minimizes a 1-D function using your `numeric_derivative`. Test that it finds the minimum of `3x² − 4x + 5` near x = 0.667.
**Done when:** `pytest test_mathkit.py` passes all 5 tests.
**Knowledge check:**
- In your `gradient_descent`, what happens if the learning rate is too large? Try it.
- Why did `softmax` need the max-subtraction trick to pass test 3?
- Which of these five functions does a neural network use during training?

### Session 1.14 — Readiness check before Phase 2 (~1.5 h)
- [ ] Done
**Goal:** confirm you're ready for Karpathy's micrograd lecture, and patch any gaps.
**Before this:** [C15 Derivative](01-concepts.md#c15--derivative), [C18 Chain rule](01-concepts.md#c18--chain-rule), [C29 Softmax](01-concepts.md#c29--softmax), [C30 Cross-entropy](01-concepts.md#c30--cross-entropy-negative-log-likelihood). Read each card and do its self-test. If one is shaky, fix it first.
**Resource:** your notes from Sessions 1.1–1.13.
**Do:**
1. On a blank page, without notes, write: the chain rule in words; what a derivative means; the formulas for softmax and cross-entropy; what gradient descent does.
2. Compare with your notes. For anything you got wrong or blanked on, redo the session listed below.
**Done when:** all four are correct from memory. If not, go back: chain rule → Session 1.4; derivative → 1.3; softmax/cross-entropy → 1.11; gradient descent → 1.12. Then redo this check.
**Knowledge check:**
- Can you explain to a colleague, in 2 minutes, how a neural network learns?
- Which session's ideas do you feel least sure about? (Revisit it.)
- What is one question you hope Phase 2 will answer?
