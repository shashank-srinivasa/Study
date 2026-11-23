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
- **Learn it**: verified tutorials (videos and articles) that explain *what* and *why*, chosen because they explain the meaning, not just the procedure. Start with the first one.
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
**Learn it:**
- [Quick Insight: Subtracting Negative Numbers](https://betterexplained.com/articles/subtracting-negative-numbers/) — BetterExplained, article. *Covers:* negatives as direction.
**If shaky:** search "negative numbers" and "multiplying negative numbers".

### C2 — Fractions, decimals, and division
**What it is:** a fraction `a/b` is "a divided into b equal parts". Decimals are the same numbers written another way (3/4 = 0.75).
**Why it exists:** to describe parts of a whole, and ratios between quantities.
**In AI:** probabilities (0.7 = 7/10), averages, learning rates (0.001), and slope (rise ÷ run) are all fractions.
**Self-test:** 3/4 as a decimal? And 1/2 + 1/3 = ? *(Answers: 0.75 and 5/6.)*
**Learn it:**
- [What Are Fractions?](https://www.youtube.com/watch?v=I1u3pM9g9o8) — Math Antics, 12 min video. *Covers:* what a fraction means.
- [Quick Insight: Intuitive Meaning of Division](https://betterexplained.com/articles/division-intuition/) — BetterExplained, article. *Covers:* what division really does.
**If shaky:** search "adding fractions with unlike denominators" and "fractions to decimals".

### C3 — Order of operations
**What it is:** the agreed order for working out an expression: brackets, then exponents, then × and ÷, then + and −.
**Why it exists:** so that `2 + 3 × 4` means the same thing to everyone. Without the rule, written math would be ambiguous.
**In AI:** every formula you type into Python follows these same rules. A missing bracket is a classic bug.
**Self-test:** 2 + 3 × 4 = ? and (2 + 3) × 4 = ? *(Answers: 14 and 20.)*
**Learn it:**
- [Why Does the Order of Operations Work? Is it just convention?](https://www.youtube.com/watch?v=-P884DAepn0) — The Bearded Math Man, 8 min video. *Covers:* why the order isn't arbitrary.
- [Order of Operations](https://www.mathsisfun.com/operation-order-bodmas.html) — Math is Fun, article. *Covers:* the rule itself.
**If shaky:** search "order of operations".

### C4 — Variables and expressions
**What it is:** a variable (like `x`) is a named placeholder for a number. An expression (like `2x + 1`) is a recipe that gives a number once you know `x`. An expression is **not** an equation. It has no `=` sign and asks no question.
**Why it exists:** to describe a calculation once and reuse it for any input. It's exactly like a variable in code.
**In AI:** a model is one giant expression. Its variables are the input data and the weights.
**Self-test:** if x = 3, what is 2x + 1? Which of these is an equation: `2x + 1` or `2x + 1 = 7`? *(Answers: 7. The second one is the equation.)*
**Learn it:**
- [Introduction to Algebra](https://www.mathsisfun.com/algebra/introduction.html) — Math is Fun, article. *Covers:* what a variable is, with a "Why use a letter?" section.
- [Algebra Basics: What Is Algebra?](https://www.youtube.com/watch?v=NybHckSEQBI) — Math Antics, 12 min video. *Covers:* unknowns and variables.
**If shaky:** search "evaluating expressions" and "expressions vs equations".

### C5 — Equations and solving
**What it is:** an equation says two things are equal (`2x + 3 = 11`). "Solving" means finding the value of `x` that makes it true, by undoing operations on both sides so it stays balanced.
**Why it exists:** to answer "which input gives this output?"
**In AI:** you rarely solve equations exactly. AI mostly *minimizes* instead (C20). But you'll rearrange formulas often.
**Self-test:** solve 2x + 3 = 11. *(Answer: x = 4. Subtract 3, then divide by 2.)*
**Learn it:**
- [Solving Equations](https://www.mathsisfun.com/algebra/equations-solving.html) — Math is Fun, article. *Covers:* what a "solution" is and the balance idea.
**If shaky:** search "two-step equations".

## Functions and graphs

### C6 — Function
**What it is:** a machine: one input goes in, exactly one output comes out. `f(x) = x² + 1` is the recipe, and `f(3)` means "put 3 in" (output: 10).
**Why it exists:** to describe how one quantity depends on another, such as distance on time or price on size.
**In AI:** **a neural network is a function.** Text or pixels go in and predictions come out. The loss is also a function: weights go in, "how wrong" comes out. This is the most important idea in the whole phase.
**Self-test:** f(x) = x² + 1. What is f(3)? What is f(−3)? *(Answers: 10 and 10.)*
**Learn it:**
- [The intuitive idea of a function](https://www.youtube.com/watch?v=G8qvOZ9DE3c) — Dr. Trefor Bazett, 5 min video. *Covers:* a function as instruction, graph and machine.
- [What is a Function?](https://www.mathsisfun.com/sets/function.html) — Math is Fun, article. *Covers:* "like a machine".
- [Neural networks lesson (text)](https://www.3blue1brown.com/lessons/neural-networks) — 3Blue1Brown. *Covers:* AI link: "the entire network is just a function".
**If shaky:** search "evaluating functions" and "what is a function".

### C7 — Graph of a function
**What it is:** a picture of every input-output pair. Each point `(x, y)` means "input x gives output y". The curve is all of them together.
**Why it exists:** to *see* how a function behaves at once: where it rises, falls, and is lowest.
**In AI:** loss curves (loss over training steps) are graphs, and you'll read them constantly to judge whether training works.
**Self-test:** is the point (1, 2) on the graph of y = 2x? *(Answer: yes, because 2 × 1 = 2.)*
**Learn it:**
- [Graph of an Equation](https://www.mathsisfun.com/sets/graph-equation.html) — Math is Fun, article. *Covers:* what a graph shows.
- [The paradox of the derivative (lesson text)](https://www.3blue1brown.com/lessons/derivatives) — 3Blue1Brown. *Covers:* reading meaning off a graph.
**If shaky:** search "coordinate plane" and "graphing functions".

### C8 — Slope of a line
**What it is:** how steep a line is: rise ÷ run, or "how much the output changes per 1 unit of input".
**Why it exists:** to measure a *rate of change*, like speed (distance per hour) or price per kilogram.
**In AI:** the derivative (C15) is slope generalized to curves, and gradients are slopes. Training is driven entirely by slopes.
**Self-test:** slope of the line through (1, 2) and (3, 8)? *(Answer: (8 − 2)/(3 − 1) = 3.)*
**Learn it:**
- [Intuition for Slope-Intercept Form](https://betterexplained.com/articles/intuition-for-slope-intercept-form/) — BetterExplained, article. *Covers:* slope as a rate of change.
**If shaky:** search "slope from two points".

### C9 — Quadratic functions: lowest point vs. "solving"
**What it is:** a function with an `x²` term, such as `3x² − 4x + 5`. If the number in front of `x²` is positive, the graph is a U shape. That's because `x²` grows quickly in both directions, so eventually it dominates everything else.
**Why it exists:** many real things curve. Thrown objects, areas, and costs that first fall then rise all follow quadratic shapes.
**Two different questions you can ask:**
- *"Where does it equal 0?"* (solving `3x² − 4x + 5 = 0`): where the U crosses the x-axis. The quadratic formula is a shortcut for this. **This one never crosses:** its lowest value is above 0, so it has no real solution.
- *"Where is it lowest?"* At `x = −b/(2a)`. For `3x² − 4x + 5` that's `x = 4/6 = 2/3`, where the output is `11/3 ≈ 3.67`.

**In AI:** AI almost always asks the *second* question: where is the loss lowest? A loss function is a U-like surface in millions of dimensions, and training means finding its bottom. Sessions 1.3, 1.5 and 1.13 all use this exact function.
**Self-test:** for `x² − 6x + 10`: where is it lowest, and what's the lowest value? Does `x² − 6x + 10 = 0` have a real solution? *(Answers: at x = 3 the value is 1. No: the lowest value is 1, so it never reaches 0.)*
**Learn it:**
- [Graphing Quadratic Equations](https://www.mathsisfun.com/algebra/quadratic-equation-graphing.html) — Math is Fun, article. *Covers:* the U shape and its lowest point (the vertex).
- [Quadratic Equations](https://www.mathsisfun.com/algebra/quadratic-equation.html) — Math is Fun, article. *Covers:* what "solving" finds, and when the graph never crosses zero.
- [Real World Examples of Quadratic Equations](https://www.mathsisfun.com/algebra/quadratic-equation-real-world.html) — Math is Fun, article. *Covers:* why quadratics exist.
**If shaky:** search "vertex of a parabola" and "intro to quadratic functions".

## Exponents, logs, and sums

### C10 — Exponents
**What it is:** `2³` means 2 × 2 × 2 = 8, repeated multiplication. The rules follow from that: `aᵐ · aⁿ = aᵐ⁺ⁿ` (count the factors), `a⁰ = 1`, and `a⁻ⁿ = 1/aⁿ`.
**Why it exists:** to write repeated multiplication and fast growth compactly (compound interest, doubling).
**In AI:** `x²` in squared error, `eˣ` in softmax, and numbers like `1e-3` (= 10⁻³ = 0.001) for learning rates.
**Self-test:** 2³? 2⁰? 2⁻¹? 2³ · 2²? *(Answers: 8, 1, 0.5, 2⁵ = 32.)*
**Learn it:**
- [What does an exponent really mean?](https://betterexplained.com/articles/what-does-an-exponent-mean/) — BetterExplained, article. *Covers:* repeated multiplication, and growth.
**If shaky:** search "exponent properties" and "negative exponents".

### C11 — Logarithms
**What it is:** the reverse of an exponent. `log₂(8)` asks "2 to what power gives 8?" (Answer: 3.)
**Why it exists:** to turn multiplication into addition, `log(a · b) = log a + log b`, and to handle numbers spanning huge ranges.
**In AI:** probabilities of long sentences are tiny products (0.1 × 0.2 × 0.05 …). Computers underflow on those, so models add **log-probabilities** instead. The loss function uses `−log`.
**Self-test:** log₂(8)? log₁₀(100)? log(a · b) in terms of log a and log b? *(Answers: 3, 2, log a + log b.)*
**Learn it:**
- [Logarithms, Explained](https://www.youtube.com/watch?v=zzu2POfYv0Y) — TED-Ed, 3 min video. *Covers:* what logs are and why they're useful.
- [Using Logarithms in the Real World](https://betterexplained.com/articles/using-logs-in-the-real-world/) — BetterExplained, article. *Covers:* logs "find the cause for an effect".
**If shaky:** search "intro to logarithms" and "logarithm properties".

### C12 — Σ (sigma) notation and the mean
**What it is:** `Σᵢ₌₁ⁿ xᵢ` means "add up x₁ through xₙ". It's a `for` loop that sums. The mean is that sum divided by n.
**Why it exists:** to write long sums compactly.
**In AI:** the loss is usually a mean over many examples, `(1/n) Σᵢ lossᵢ`, and matrix multiplication is sums of products.
**Self-test:** Σᵢ₌₁³ 2i = ? Mean of [2, 4, 9]? *(Answers: 2 + 4 + 6 = 12; 15/3 = 5.)*
**Learn it:**
- [Math Notation Explained with For Loops](https://www.youtube.com/watch?v=hhcDnaUsCnY) — Compute Illustrated, 8 min video. *Covers:* Σ is just a for loop.
- [How To Analyze Data Using the Average](https://betterexplained.com/articles/how-to-analyze-data-using-the-average/) — BetterExplained, article. *Covers:* what the mean really is.
**If shaky:** search "summation notation" and "mean".

### C13 — e and eˣ
**What it is:** `e ≈ 2.718` is a special constant. The function `eˣ` is the one function whose slope at every point equals its own value.
**Why it exists:** it appears naturally whenever something grows in proportion to its size, and that slope property makes calculus with it very simple.
**In AI:** softmax (C29) uses `eˣ` to turn any numbers into positive ones, and `tanh` is built from it.
**Self-test:** e⁰ = ? What is the derivative of eˣ? Can eˣ ever be negative? *(Answers: 1; eˣ itself; no, it's always positive.)*
**Learn it:**
- [An Intuitive Guide To Exponential Functions & e](https://betterexplained.com/articles/an-intuitive-guide-to-exponential-functions-e/) — BetterExplained, article. *Covers:* e as the base rate of growth.
- [What's so special about Euler's number e?](https://www.youtube.com/watch?v=m2MIpDrF7Es) — 3Blue1Brown, 13 min video (also in Session 1.5). *Covers:* why eˣ is its own slope.
**If shaky:** search "e and compound interest" and "derivative of e^x".

## Calculus

### C14 — "What happens as h gets tiny" (the limit idea)
**What it is:** you can't divide by zero, but you can see what a calculation *approaches* as a number gets closer and closer to zero.
**Why it exists:** it's the trick that lets us talk about the slope *at a single point* of a curve, where "rise over run" would have a run of 0.
**In AI:** this is exactly how you'll check gradients numerically: nudge by a tiny `h` and watch what the slope approaches.
**Self-test:** for f(x) = x², `(f(1 + h) − f(1)) / h` simplifies to `2 + h`. What does it approach as h → 0? *(Answer: 2.)*
**Learn it:**
- [An Intuitive Introduction To Limits](https://betterexplained.com/articles/an-intuitive-introduction-to-limits/) — BetterExplained, article. *Covers:* limits as an estimate when you can't compute directly.
- [Limits (An Introduction)](https://www.mathsisfun.com/calculus/limits.html) — Math is Fun, article. *Covers:* getting closer and closer.
**If shaky:** search "limits intro".

### C15 — Derivative
**What it is:** the slope of a curve at one point, or "if I nudge the input a tiny bit, how much does the output change, and in which direction?"
**Why it exists:** to measure an instant rate of change (speed *right now*, not on average).
**In AI:** this is **the** core idea of training. For every weight, the derivative of the loss says which way to nudge that weight to make the model less wrong.
**Self-test:** if f′(3) = 14, about how much does f change when x goes from 3 to 3.01? *(Answer: up by about 14 × 0.01 = 0.14.)*
**Learn it:**
- [The paradox of the derivative](https://www.youtube.com/watch?v=9vKqVkMQHKk) — 3Blue1Brown, 16 min video (also in Session 1.3). *Covers:* what a derivative is.
- [Calculus: Building Intuition for the Derivative](https://betterexplained.com/articles/calculus-building-intuition-for-the-derivative/) — BetterExplained, article. *Covers:* why derivatives exist.
- [Gradient descent lesson (text)](https://www.3blue1brown.com/lessons/gradient-descent) — 3Blue1Brown. *Covers:* AI link: derivatives drive learning.
**If shaky:** search "derivative as slope of tangent line".

### C16 — Derivative rules (power, constant multiple, sum)
**What it is:** shortcuts that give derivatives without computing limits: `d/dx xⁿ = n·xⁿ⁻¹`, constants multiply through, and the derivative of a sum is the sum of the derivatives.
**Why it exists:** working out limits by hand every time is slow. The rules are patterns that always hold.
**In AI:** micrograd builds each operation's local derivative from rules like these.
**Self-test:** d/dx (5x³)? d/dx (x² + 7)? *(Answers: 15x²; 2x, because a constant doesn't change, so its slope is 0.)*
**Learn it:**
- [Derivative formulas through geometry](https://www.youtube.com/watch?v=S0_qX4VJhMQ) — 3Blue1Brown, 17 min video (also in Session 1.4). *Covers:* why the rules are true, shown geometrically.
**If shaky:** search "power rule" and "basic differentiation rules".

### C17 — Function composition
**What it is:** feeding one function's output into another, `f(g(x))`. It's a pipeline: `x → g → f → result`.
**Why it exists:** complicated processes are chains of simple steps.
**In AI:** a neural network is a long composition: layer 1 → layer 2 → … → loss. This is why the chain rule (C18) matters so much.
**Self-test:** g(x) = x + 1 and f(u) = u². What is f(g(2))? *(Answer: g(2) = 3, then f(3) = 9.)*
**Learn it:**
- [Visualizing the chain rule and product rule](https://www.youtube.com/watch?v=YG15m2VwSjA) — 3Blue1Brown, 16 min video (also in Session 1.4). *Covers:* composition as a pipeline.
- [Composition of Functions](https://www.mathsisfun.com/sets/functions-composition.html) — Math is Fun, article. *Covers:* what composition is, and why order matters.
**If shaky:** search "composite functions".

### C18 — Chain rule
**What it is:** the derivative of a pipeline is the product of the local slopes along it. If `y = f(g(x))`, then `dy/dx = f′(g(x)) · g′(x)`.
**Why it exists:** to get the derivative of a complicated chain from the derivatives of its simple steps.
**In AI:** **backpropagation is the chain rule**, applied from the loss backwards through every layer. Phase 2 is built entirely on this.
**Self-test:** derivative of `(3x + 1)²`? Its value at x = 0? *(Answers: 2(3x + 1) · 3 = 6(3x + 1); 6.)*
**Learn it:**
- [Visualizing the chain rule and product rule](https://www.youtube.com/watch?v=YG15m2VwSjA) — 3Blue1Brown, 16 min video (also in Session 1.4). *Covers:* how nudges pass through a chain.
**If shaky:** search "chain rule intro".

### C19 — Partial derivatives and the gradient
**What it is:** when a function has several inputs, `f(x, y)`, a *partial derivative* is the slope in one input's direction, holding the others fixed. The **gradient** is the list of all of them together.
**Why it exists:** real functions depend on many things at once, and you need to know how each one affects the output.
**In AI:** a model's loss depends on millions of weights. The gradient tells you, for every single weight, which direction reduces the loss. `loss.backward()` computes exactly this.
**Self-test:** f(x, y) = x·y + y. What is ∂f/∂x? ∂f/∂y? The gradient at (2, 3)? *(Answers: y; x + 1; (3, 3).)*
**Learn it:**
- [Vector Calculus: Understanding the Gradient](https://betterexplained.com/articles/vector-calculus-understanding-the-gradient/) — BetterExplained, article. *Covers:* what the gradient is and why it points uphill.
- [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) — 3Blue1Brown, 20 min video (also in Session 1.12). *Covers:* AI link: the gradient over many weights.
**If shaky:** search "partial derivatives introduction" and "gradient".

### C20 — Minimum and gradient descent
**What it is:** the minimum is the input where a function is lowest. *Gradient descent* finds it by repeatedly stepping a little downhill: `x_new = x − learning_rate × slope`.
**Why it exists:** for big functions you can't just solve for the bottom (C9's formula only works for a simple U), but you can always walk downhill.
**In AI:** **this is what training is.** Every training step is one step of gradient descent on the loss.
**Self-test:** f(x) = (x − 2)², start at x = 0, learning rate 0.25. The slope is 2(x − 2). Where are you after one step? *(Answer: slope = −4, so x = 0 − 0.25 × (−4) = 1. You moved toward the minimum at 2.)*
**Learn it:**
- [Gradient descent, how neural networks learn](https://www.youtube.com/watch?v=IHZwWFHWa-w) — 3Blue1Brown, 20 min video (also in Session 1.12). *Covers:* what, why and AI.
- [Linear regression: Gradient descent](https://developers.google.com/machine-learning/crash-course/linear-regression/gradient-descent) — Google ML Crash Course, article. *Covers:* AI link: finding the lowest loss.
**If shaky:** search "gradient descent" (3Blue1Brown's Neural Networks chapter 2 in Session 1.12 covers it well).

## Linear algebra

### C21 — Vector
**What it is:** an ordered list of numbers, `[2, 1]`. You can also picture it as an arrow from the origin. You add vectors element by element, and multiplying by a number scales every element.
**Why it exists:** to bundle related numbers together, like a position, a direction, or a set of features.
**In AI:** everything becomes a vector. A word becomes an *embedding* vector, an image becomes a vector of pixels, and a model's hidden state is a vector.
**Self-test:** [1, 2] + [3, −1]? 2 · [1, 2]? *(Answers: [4, 1]; [2, 4].)*
**Learn it:**
- [Vectors | Essence of linear algebra ch. 1](https://www.youtube.com/watch?v=fNk_zzaMoSs) — 3Blue1Brown, 10 min video (also in Session 1.6). *Covers:* arrows and lists are the same thing.
**If shaky:** search "vectors intro" (linear algebra).

### C22 — Linear combination
**What it is:** scaling some vectors and adding them up: `a·v + b·w`.
**Why it exists:** it's the basic way to build new vectors out of known ones. "Every point on the grid is some amount of right plus some amount of up."
**In AI:** a neuron computes a weighted sum, and an attention output is a weighted mix of value vectors. Both are linear combinations.
**Self-test:** 2·[1, 0] + 3·[0, 1]? *(Answer: [2, 3].)*
**Learn it:**
- [Linear combinations, span, and basis vectors](https://www.youtube.com/watch?v=k7RM-ot2NWY) — 3Blue1Brown, 10 min video (also in Session 1.6). *Covers:* building vectors from others.
**If shaky:** search "linear combinations and span".

### C23 — Matrix as a transformation
**What it is:** a grid of numbers that *transforms* vectors. It can stretch, rotate, or squish space. Its columns say where the basic arrows `[1, 0]` and `[0, 1]` end up.
**Why it exists:** to describe "do this to every point" with a single object.
**In AI:** every layer's weights are a matrix. A layer transforms its input vector into a new representation.
**Self-test:** the matrix `[[2, 0], [0, 1]]` applied to `[1, 1]` gives? *(Answer: [2, 1]. It stretches the x direction by 2.)*
**Learn it:**
- [Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE) — 3Blue1Brown, 11 min video (also in Session 1.7). *Covers:* a matrix says where the basic arrows land.
**If shaky:** search "matrix vector products" and "linear transformations".

### C24 — Matrix multiplication and shapes
**What it is:** combining two matrices. Each entry of `A @ B` is a dot product of a row of A with a column of B. It only works when A's column count equals B's row count, and `(m × n) @ (n × p)` gives `(m × p)`.
**Why it exists:** to apply one transformation after another, or to process many vectors at once.
**In AI:** this is the single most common operation in deep learning, and what GPUs are built to do fast (Phase 5). Shape errors are the most common bug you'll hit.
**Self-test:** shape of (2 × 3) @ (3 × 4)? Does (2 × 3) @ (2 × 3) work? *(Answers: 2 × 4; no, because 3 ≠ 2.)*
**Learn it:**
- [Matrix multiplication as composition](https://www.youtube.com/watch?v=XkY2DOUCWMU) — 3Blue1Brown, 10 min video (also in Session 1.7). *Covers:* why multiplication means applying one transformation after another.
- [A Programmer's Intuition for Matrix Multiplication](https://betterexplained.com/articles/matrix-multiplication/) — BetterExplained, article. *Covers:* matrices as data flow, for programmers.
**If shaky:** search "multiplying matrices".

### C25 — Dot product
**What it is:** multiply matching elements and add: `[1, 2] · [3, 4] = 1·3 + 2·4 = 11`. Geometrically it measures how much two vectors point the same way. A dot product of 0 means they're at right angles.
**Why it exists:** it's a single number that captures alignment, or similarity.
**In AI:** attention computes dot products between a query and keys to decide "which words are relevant to this one?" Similarity search also uses dot products.
**Self-test:** [1, 2] · [3, 4]? [1, 0] · [0, 1]? *(Answers: 11; 0, so they're perpendicular.)*
**Learn it:**
- [Vector Calculus: Understanding the Dot Product](https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/) — BetterExplained, article. *Covers:* "directional multiplication".
- [Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0) — 3Blue1Brown, 14 min video (also in Session 1.8). *Covers:* projection and alignment.
**If shaky:** search "dot product".

## Probability

### C26 — Probability
**What it is:** a number from 0 (impossible) to 1 (certain) for how likely something is. The probabilities of all possible outcomes add up to 1.
**Why it exists:** to reason precisely about uncertainty.
**In AI:** a language model doesn't "know" the next word. It assigns a probability to every possible next token.
**Self-test:** for a fair die, what is P(even)? What must P(1) + … + P(6) equal? *(Answers: 3/6 = 1/2; 1.)*
**Learn it:**
- [Seeing Theory: Basic Probability](https://seeing-theory.brown.edu/basic-probability/index.html) — Brown University, interactive. *Covers:* what probability is for.
**If shaky:** search "basic probability".

### C27 — Probability distribution
**What it is:** a full list of outcomes with a probability for each, all non-negative and summing to 1.
**Why it exists:** to describe *all* the possibilities at once, not just one.
**In AI:** the model's output for each position is a distribution over its whole vocabulary (for example 50,257 tokens for GPT-2).
**Self-test:** is [0.5, 0.3, 0.3] a valid distribution? *(Answer: no. It sums to 1.1.)*
**Learn it:**
- [Seeing Theory: Probability Distributions](https://seeing-theory.brown.edu/probability-distributions/index.html) — Brown University, interactive. *Covers:* the likelihoods of all outcomes.
- [The Main Ideas behind Probability Distributions](https://www.youtube.com/watch?v=oI3hZJqXJuc) — StatQuest, 5 min video. *Covers:* the main idea.
**If shaky:** search "probability distributions" (statistics & probability).

### C28 — Conditional probability
**What it is:** `P(A | B)`, the probability of A *given that* B happened. It means narrowing your attention to only the cases where B is true.
**Why it exists:** because new information changes how likely things are.
**In AI:** a language model computes P(next token | all previous tokens). That conditional is the entire job.
**Self-test:** from a standard deck, P(king | the card is a face card)? *(Answer: 4 kings out of 12 face cards = 1/3.)*
**Learn it:**
- [Seeing Theory: Compound Probability](https://seeing-theory.brown.edu/compound-probability/index.html) — Brown University, interactive. *Covers:* conditioning as "shrinking the sample space".
- [Conditional Probabilities, Clearly Explained!!!](https://www.youtube.com/watch?v=_IgyaD7vOOA) — StatQuest, 11 min video. *Covers:* the idea, step by step.
**If shaky:** search "conditional probability".

### C29 — Softmax
**What it is:** a function that turns any list of numbers into a probability distribution: `softmaxᵢ = eᶻⁱ / Σⱼ eᶻʲ`. `eˣ` makes everything positive, and dividing by the sum makes it add to 1.
**Why it exists:** models produce raw scores (*logits*) that can be any number, but we need probabilities.
**In AI:** it's the last step of every language model's output, and it's also inside attention.
**Self-test:** softmax([0, 0])? softmax([1, 1, 1])? What happens if you add 5 to every input? *(Answers: [0.5, 0.5]; [1/3, 1/3, 1/3]; nothing changes, which is why subtracting the max is a safe trick.)*
**Learn it:**
- [Multi-class classification (softmax)](https://developers.google.com/machine-learning/crash-course/neural-networks/multi-class) — Google ML Crash Course, article. *Covers:* AI link: why outputs must add up to 1.
- [Neural Networks Part 5: ArgMax and SoftMax](https://www.youtube.com/watch?v=KpKog-L9veg) — StatQuest, 14 min video. *Covers:* when and why to use softmax.
**If shaky:** there's no Khan topic for this. Re-read C13 and C27, then Session 1.11.

### C30 — Cross-entropy (negative log-likelihood)
**What it is:** a score for how surprised the model was by the right answer: `−log(probability given to the correct answer)`.
**Why it exists:** we need one number that is 0 when the model is perfectly confident and right, and that grows large when the model is confident and wrong.
**In AI:** **this is the loss function used to train language models**, Claude-like models included. "Training lowered the loss" means "the model became less surprised by real text".
**Self-test:** loss when the correct answer gets probability 1? 0.5? 0.01? *(Answers: 0; about 0.693; about 4.6.)*
**Learn it:**
- [What is cross-entropy, and why is it used in ML?](https://www.youtube.com/watch?v=GlYgs6v2YfU) — 3Blue1Brown, 34 min video (also in Session 1.11). *Covers:* what, why and AI.
- [Neural Networks Part 6: Cross Entropy](https://www.youtube.com/watch?v=6ArSys5qHAU) — StatQuest, 10 min video. *Covers:* a shorter, more procedural overview.
**If shaky:** re-read C11 (logs), then watch the 3Blue1Brown cross-entropy video in Session 1.11.
