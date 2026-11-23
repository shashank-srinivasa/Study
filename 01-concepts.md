# Phase 1 companion — Concept cards (meaning first)

**Why this file exists:** knowing *how* to do a math procedure isn't the same as knowing *what it
is* or *why anyone does it*. Every card below answers those questions first. Each math session
links to the cards it relies on in its **Before this** block. Read those cards first, and
take each self-test.

**How to use a card:**
- **What it is**, in plain words.
- **Why it exists**: the problem it was invented to solve.
- **In AI**: where you'll meet it again in this guide.
- **Self-test**: do it in your head or on paper, *then* check the answer.
- **If shaky**: what to search for on Khan Academy ([Pre-algebra](https://www.khanacademy.org/math/pre-algebra), [Algebra 1](https://www.khanacademy.org/math/algebra), [Algebra 2](https://www.khanacademy.org/math/algebra2), [Differential calculus](https://www.khanacademy.org/math/differential-calculus), [Multivariable calculus](https://www.khanacademy.org/math/multivariable-calculus), [Linear algebra](https://www.khanacademy.org/math/linear-algebra), [Statistics & probability](https://www.khanacademy.org/math/statistics-probability)). Use the site's search box with the exact term given.

**The map.** Each arrow means "you need the left one to make sense of the right one":

```
C1 negatives ─┐
C2 fractions ─┼→ C3 order of operations → C4 variables & expressions → C5 equations
              │
              └→ C6 function → C7 graph → C8 slope → C9 quadratic (minimum vs. roots)
                     │
                     ├→ C10 exponents → C11 logarithms
                     │        └→ C13 e and eˣ
                     ├→ C12 Σ and the mean
                     └→ C14 "as h gets tiny" → C15 derivative → C16 derivative rules
                              C17 composition ──────────────→ C18 chain rule
                                         C18 → C19 partial derivatives & gradient → C20 minimum & gradient descent

C2 → C21 vector → C22 linear combination → C23 matrix as transformation → C24 matrix multiplication → C25 dot product

C2 → C26 probability → C27 distribution → C28 conditional probability
          C13 + C27 → C29 softmax;  C11 + C27 → C30 cross-entropy
```

---

## Foundations (checked in Session 1.0)

### C1 — Negative numbers
**What it is:** numbers below zero, positions to the left of 0 on a number line.
**Why it exists:** to describe "less than nothing" or a direction: debt, temperatures below zero, moving backwards.
**In AI:** weights, gradients, and errors are negative all the time. A negative gradient means "increase this weight to reduce the error".
**Self-test:** −3 − 5 = ? and (−2) × (−4) = ? *(Answers: −8 and 8. Minus times minus is plus.)*
**If shaky:** search "negative numbers" and "multiplying negative numbers".

### C2 — Fractions, decimals, and division
**What it is:** a fraction `a/b` is "a divided into b equal parts". Decimals are the same numbers written another way (3/4 = 0.75).
**Why it exists:** to describe parts of a whole, and ratios between quantities.
**In AI:** probabilities (0.7 = 7/10), averages, learning rates (0.001), and slope (rise ÷ run) are all fractions.
**Self-test:** 3/4 as a decimal? And 1/2 + 1/3 = ? *(Answers: 0.75 and 5/6.)*
**If shaky:** search "adding fractions with unlike denominators" and "fractions to decimals".

### C3 — Order of operations
**What it is:** the agreed order for working out an expression: brackets, then exponents, then × and ÷, then + and −.
**Why it exists:** so that `2 + 3 × 4` means the same thing to everyone. Without the rule, written math would be ambiguous.
**In AI:** every formula you type into Python follows these same rules. A missing bracket is a classic bug.
**Self-test:** 2 + 3 × 4 = ? and (2 + 3) × 4 = ? *(Answers: 14 and 20.)*
**If shaky:** search "order of operations".

### C4 — Variables and expressions
**What it is:** a variable (like `x`) is a named placeholder for a number. An expression (like `2x + 1`) is a recipe that gives a number once you know `x`. An expression is **not** an equation. It has no `=` sign and asks no question.
**Why it exists:** to describe a calculation once and reuse it for any input. It's exactly like a variable in code.
**In AI:** a model is one giant expression. Its variables are the input data and the weights.
**Self-test:** if x = 3, what is 2x + 1? Which of these is an equation: `2x + 1` or `2x + 1 = 7`? *(Answers: 7. The second one is the equation.)*
**If shaky:** search "evaluating expressions" and "expressions vs equations".

### C5 — Equations and solving
**What it is:** an equation says two things are equal (`2x + 3 = 11`). "Solving" means finding the value of `x` that makes it true, by undoing operations on both sides so it stays balanced.
**Why it exists:** to answer "which input gives this output?"
**In AI:** you rarely solve equations exactly. AI mostly *minimizes* instead (C20). But you'll rearrange formulas often.
**Self-test:** solve 2x + 3 = 11. *(Answer: x = 4. Subtract 3, then divide by 2.)*
**If shaky:** search "two-step equations".

## Functions and graphs

### C6 — Function
**What it is:** a machine: one input goes in, exactly one output comes out. `f(x) = x² + 1` is the recipe, and `f(3)` means "put 3 in" (output: 10).
**Why it exists:** to describe how one quantity depends on another, such as distance on time or price on size.
**In AI:** **a neural network is a function.** Text or pixels go in and predictions come out. The loss is also a function: weights go in, "how wrong" comes out. This is the most important idea in the whole phase.
**Self-test:** f(x) = x² + 1. What is f(3)? What is f(−3)? *(Answers: 10 and 10.)*
**If shaky:** search "evaluating functions" and "what is a function".

### C7 — Graph of a function
**What it is:** a picture of every input-output pair. Each point `(x, y)` means "input x gives output y". The curve is all of them together.
**Why it exists:** to *see* how a function behaves at once: where it rises, falls, and is lowest.
**In AI:** loss curves (loss over training steps) are graphs, and you'll read them constantly to judge whether training works.
**Self-test:** is the point (1, 2) on the graph of y = 2x? *(Answer: yes, because 2 × 1 = 2.)*
**If shaky:** search "coordinate plane" and "graphing functions".

### C8 — Slope of a line
**What it is:** how steep a line is: rise ÷ run, or "how much the output changes per 1 unit of input".
**Why it exists:** to measure a *rate of change*, like speed (distance per hour) or price per kilogram.
**In AI:** the derivative (C15) is slope generalized to curves, and gradients are slopes. Training is driven entirely by slopes.
**Self-test:** slope of the line through (1, 2) and (3, 8)? *(Answer: (8 − 2)/(3 − 1) = 3.)*
**If shaky:** search "slope from two points".

### C9 — Quadratic functions: lowest point vs. "solving"
**What it is:** a function with an `x²` term, such as `3x² − 4x + 5`. If the number in front of `x²` is positive, the graph is a U shape. That's because `x²` grows quickly in both directions, so eventually it dominates everything else.
**Why it exists:** many real things curve. Thrown objects, areas, and costs that first fall then rise all follow quadratic shapes.
**Two different questions you can ask:**
- *"Where does it equal 0?"* (solving `3x² − 4x + 5 = 0`): where the U crosses the x-axis. The quadratic formula is a shortcut for this. **This one never crosses:** its lowest value is above 0, so it has no real solution.
- *"Where is it lowest?"* At `x = −b/(2a)`. For `3x² − 4x + 5` that's `x = 4/6 = 2/3`, where the output is `11/3 ≈ 3.67`.

**In AI:** AI almost always asks the *second* question: where is the loss lowest? A loss function is a U-like surface in millions of dimensions, and training means finding its bottom. Sessions 1.3, 1.5 and 1.13 all use this exact function.
**Self-test:** for `x² − 6x + 10`: where is it lowest, and what's the lowest value? Does `x² − 6x + 10 = 0` have a real solution? *(Answers: at x = 3 the value is 1. No: the lowest value is 1, so it never reaches 0.)*
**If shaky:** search "vertex of a parabola" and "intro to quadratic functions".

## Exponents, logs, and sums

### C10 — Exponents
**What it is:** `2³` means 2 × 2 × 2 = 8, repeated multiplication. The rules follow from that: `aᵐ · aⁿ = aᵐ⁺ⁿ` (count the factors), `a⁰ = 1`, and `a⁻ⁿ = 1/aⁿ`.
**Why it exists:** to write repeated multiplication and fast growth compactly (compound interest, doubling).
**In AI:** `x²` in squared error, `eˣ` in softmax, and numbers like `1e-3` (= 10⁻³ = 0.001) for learning rates.
**Self-test:** 2³? 2⁰? 2⁻¹? 2³ · 2²? *(Answers: 8, 1, 0.5, 2⁵ = 32.)*
**If shaky:** search "exponent properties" and "negative exponents".

### C11 — Logarithms
**What it is:** the reverse of an exponent. `log₂(8)` asks "2 to what power gives 8?" (Answer: 3.)
**Why it exists:** to turn multiplication into addition, `log(a · b) = log a + log b`, and to handle numbers spanning huge ranges.
**In AI:** probabilities of long sentences are tiny products (0.1 × 0.2 × 0.05 …). Computers underflow on those, so models add **log-probabilities** instead. The loss function uses `−log`.
**Self-test:** log₂(8)? log₁₀(100)? log(a · b) in terms of log a and log b? *(Answers: 3, 2, log a + log b.)*
**If shaky:** search "intro to logarithms" and "logarithm properties".

### C12 — Σ (sigma) notation and the mean
**What it is:** `Σᵢ₌₁ⁿ xᵢ` means "add up x₁ through xₙ". It's a `for` loop that sums. The mean is that sum divided by n.
**Why it exists:** to write long sums compactly.
**In AI:** the loss is usually a mean over many examples, `(1/n) Σᵢ lossᵢ`, and matrix multiplication is sums of products.
**Self-test:** Σᵢ₌₁³ 2i = ? Mean of [2, 4, 9]? *(Answers: 2 + 4 + 6 = 12; 15/3 = 5.)*
**If shaky:** search "summation notation" and "mean".

### C13 — e and eˣ
**What it is:** `e ≈ 2.718` is a special constant. The function `eˣ` is the one function whose slope at every point equals its own value.
**Why it exists:** it appears naturally whenever something grows in proportion to its size, and that slope property makes calculus with it very simple.
**In AI:** softmax (C29) uses `eˣ` to turn any numbers into positive ones, and `tanh` is built from it.
**Self-test:** e⁰ = ? What is the derivative of eˣ? Can eˣ ever be negative? *(Answers: 1; eˣ itself; no, it's always positive.)*
**If shaky:** search "e and compound interest" and "derivative of e^x".

## Calculus

### C14 — "What happens as h gets tiny" (the limit idea)
**What it is:** you can't divide by zero, but you can see what a calculation *approaches* as a number gets closer and closer to zero.
**Why it exists:** it's the trick that lets us talk about the slope *at a single point* of a curve, where "rise over run" would have a run of 0.
**In AI:** this is exactly how you'll check gradients numerically: nudge by a tiny `h` and watch what the slope approaches.
**Self-test:** for f(x) = x², `(f(1 + h) − f(1)) / h` simplifies to `2 + h`. What does it approach as h → 0? *(Answer: 2.)*
**If shaky:** search "limits intro".

### C15 — Derivative
**What it is:** the slope of a curve at one point, or "if I nudge the input a tiny bit, how much does the output change, and in which direction?"
**Why it exists:** to measure an instant rate of change (speed *right now*, not on average).
**In AI:** this is **the** core idea of training. For every weight, the derivative of the loss says which way to nudge that weight to make the model less wrong.
**Self-test:** if f′(3) = 14, about how much does f change when x goes from 3 to 3.01? *(Answer: up by about 14 × 0.01 = 0.14.)*
**If shaky:** search "derivative as slope of tangent line".

### C16 — Derivative rules (power, constant multiple, sum)
**What it is:** shortcuts that give derivatives without computing limits: `d/dx xⁿ = n·xⁿ⁻¹`, constants multiply through, and the derivative of a sum is the sum of the derivatives.
**Why it exists:** working out limits by hand every time is slow. The rules are patterns that always hold.
**In AI:** micrograd builds each operation's local derivative from rules like these.
**Self-test:** d/dx (5x³)? d/dx (x² + 7)? *(Answers: 15x²; 2x, because a constant doesn't change, so its slope is 0.)*
**If shaky:** search "power rule" and "basic differentiation rules".

### C17 — Function composition
**What it is:** feeding one function's output into another, `f(g(x))`. It's a pipeline: `x → g → f → result`.
**Why it exists:** complicated processes are chains of simple steps.
**In AI:** a neural network is a long composition: layer 1 → layer 2 → … → loss. This is why the chain rule (C18) matters so much.
**Self-test:** g(x) = x + 1 and f(u) = u². What is f(g(2))? *(Answer: g(2) = 3, then f(3) = 9.)*
**If shaky:** search "composite functions".

### C18 — Chain rule
**What it is:** the derivative of a pipeline is the product of the local slopes along it. If `y = f(g(x))`, then `dy/dx = f′(g(x)) · g′(x)`.
**Why it exists:** to get the derivative of a complicated chain from the derivatives of its simple steps.
**In AI:** **backpropagation is the chain rule**, applied from the loss backwards through every layer. Phase 2 is built entirely on this.
**Self-test:** derivative of `(3x + 1)²`? Its value at x = 0? *(Answers: 2(3x + 1) · 3 = 6(3x + 1); 6.)*
**If shaky:** search "chain rule intro".

### C19 — Partial derivatives and the gradient
**What it is:** when a function has several inputs, `f(x, y)`, a *partial derivative* is the slope in one input's direction, holding the others fixed. The **gradient** is the list of all of them together.
**Why it exists:** real functions depend on many things at once, and you need to know how each one affects the output.
**In AI:** a model's loss depends on millions of weights. The gradient tells you, for every single weight, which direction reduces the loss. `loss.backward()` computes exactly this.
**Self-test:** f(x, y) = x·y + y. What is ∂f/∂x? ∂f/∂y? The gradient at (2, 3)? *(Answers: y; x + 1; (3, 3).)*
**If shaky:** search "partial derivatives introduction" and "gradient".

### C20 — Minimum and gradient descent
**What it is:** the minimum is the input where a function is lowest. *Gradient descent* finds it by repeatedly stepping a little downhill: `x_new = x − learning_rate × slope`.
**Why it exists:** for big functions you can't just solve for the bottom (C9's formula only works for a simple U), but you can always walk downhill.
**In AI:** **this is what training is.** Every training step is one step of gradient descent on the loss.
**Self-test:** f(x) = (x − 2)², start at x = 0, learning rate 0.25. The slope is 2(x − 2). Where are you after one step? *(Answer: slope = −4, so x = 0 − 0.25 × (−4) = 1. You moved toward the minimum at 2.)*
**If shaky:** search "gradient descent" (3Blue1Brown's Neural Networks chapter 2 in Session 1.12 covers it well).

## Linear algebra

### C21 — Vector
**What it is:** an ordered list of numbers, `[2, 1]`. You can also picture it as an arrow from the origin. You add vectors element by element, and multiplying by a number scales every element.
**Why it exists:** to bundle related numbers together, like a position, a direction, or a set of features.
**In AI:** everything becomes a vector. A word becomes an *embedding* vector, an image becomes a vector of pixels, and a model's hidden state is a vector.
**Self-test:** [1, 2] + [3, −1]? 2 · [1, 2]? *(Answers: [4, 1]; [2, 4].)*
**If shaky:** search "vectors intro" (linear algebra).

### C22 — Linear combination
**What it is:** scaling some vectors and adding them up: `a·v + b·w`.
**Why it exists:** it's the basic way to build new vectors out of known ones. "Every point on the grid is some amount of right plus some amount of up."
**In AI:** a neuron computes a weighted sum, and an attention output is a weighted mix of value vectors. Both are linear combinations.
**Self-test:** 2·[1, 0] + 3·[0, 1]? *(Answer: [2, 3].)*
**If shaky:** search "linear combinations and span".

### C23 — Matrix as a transformation
**What it is:** a grid of numbers that *transforms* vectors. It can stretch, rotate, or squish space. Its columns say where the basic arrows `[1, 0]` and `[0, 1]` end up.
**Why it exists:** to describe "do this to every point" with a single object.
**In AI:** every layer's weights are a matrix. A layer transforms its input vector into a new representation.
**Self-test:** the matrix `[[2, 0], [0, 1]]` applied to `[1, 1]` gives? *(Answer: [2, 1]. It stretches the x direction by 2.)*
**If shaky:** search "matrix vector products" and "linear transformations".

### C24 — Matrix multiplication and shapes
**What it is:** combining two matrices. Each entry of `A @ B` is a dot product of a row of A with a column of B. It only works when A's column count equals B's row count, and `(m × n) @ (n × p)` gives `(m × p)`.
**Why it exists:** to apply one transformation after another, or to process many vectors at once.
**In AI:** this is the single most common operation in deep learning, and what GPUs are built to do fast (Phase 5). Shape errors are the most common bug you'll hit.
**Self-test:** shape of (2 × 3) @ (3 × 4)? Does (2 × 3) @ (2 × 3) work? *(Answers: 2 × 4; no, because 3 ≠ 2.)*
**If shaky:** search "multiplying matrices".

### C25 — Dot product
**What it is:** multiply matching elements and add: `[1, 2] · [3, 4] = 1·3 + 2·4 = 11`. Geometrically it measures how much two vectors point the same way. A dot product of 0 means they're at right angles.
**Why it exists:** it's a single number that captures alignment, or similarity.
**In AI:** attention computes dot products between a query and keys to decide "which words are relevant to this one?" Similarity search also uses dot products.
**Self-test:** [1, 2] · [3, 4]? [1, 0] · [0, 1]? *(Answers: 11; 0, so they're perpendicular.)*
**If shaky:** search "dot product".

## Probability

### C26 — Probability
**What it is:** a number from 0 (impossible) to 1 (certain) for how likely something is. The probabilities of all possible outcomes add up to 1.
**Why it exists:** to reason precisely about uncertainty.
**In AI:** a language model doesn't "know" the next word. It assigns a probability to every possible next token.
**Self-test:** for a fair die, what is P(even)? What must P(1) + … + P(6) equal? *(Answers: 3/6 = 1/2; 1.)*
**If shaky:** search "basic probability".

### C27 — Probability distribution
**What it is:** a full list of outcomes with a probability for each, all non-negative and summing to 1.
**Why it exists:** to describe *all* the possibilities at once, not just one.
**In AI:** the model's output for each position is a distribution over its whole vocabulary (for example 50,257 tokens for GPT-2).
**Self-test:** is [0.5, 0.3, 0.3] a valid distribution? *(Answer: no. It sums to 1.1.)*
**If shaky:** search "probability distributions" (statistics & probability).

### C28 — Conditional probability
**What it is:** `P(A | B)`, the probability of A *given that* B happened. It means narrowing your attention to only the cases where B is true.
**Why it exists:** because new information changes how likely things are.
**In AI:** a language model computes P(next token | all previous tokens). That conditional is the entire job.
**Self-test:** from a standard deck, P(king | the card is a face card)? *(Answer: 4 kings out of 12 face cards = 1/3.)*
**If shaky:** search "conditional probability".

### C29 — Softmax
**What it is:** a function that turns any list of numbers into a probability distribution: `softmaxᵢ = eᶻⁱ / Σⱼ eᶻʲ`. `eˣ` makes everything positive, and dividing by the sum makes it add to 1.
**Why it exists:** models produce raw scores (*logits*) that can be any number, but we need probabilities.
**In AI:** it's the last step of every language model's output, and it's also inside attention.
**Self-test:** softmax([0, 0])? softmax([1, 1, 1])? What happens if you add 5 to every input? *(Answers: [0.5, 0.5]; [1/3, 1/3, 1/3]; nothing changes, which is why subtracting the max is a safe trick.)*
**If shaky:** there's no Khan topic for this. Re-read C13 and C27, then Session 1.11.

### C30 — Cross-entropy (negative log-likelihood)
**What it is:** a score for how surprised the model was by the right answer: `−log(probability given to the correct answer)`.
**Why it exists:** we need one number that is 0 when the model is perfectly confident and right, and that grows large when the model is confident and wrong.
**In AI:** **this is the loss function used to train language models**, Claude-like models included. "Training lowered the loss" means "the model became less surprised by real text".
**Self-test:** loss when the correct answer gets probability 1? 0.5? 0.01? *(Answers: 0; about 0.693; about 4.6.)*
**If shaky:** re-read C11 (logs), then watch the 3Blue1Brown cross-entropy video in Session 1.11.
