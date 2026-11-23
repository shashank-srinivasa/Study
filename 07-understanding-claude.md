# Phase 7 (optional) — Understanding Claude: training, interpretability, and agents (~19.5 h)

**Do this after Phase 4** (Phase 5 is not required). You've built a GPT. This phase covers what turns a
model like yours into an assistant like Claude, what researchers have found inside models like
Claude, and how an agent such as Claude Code works.

**An honest caveat:** Anthropic hasn't published Claude's exact architecture, size, or training data.
This phase uses what Anthropic *has* published: its research papers on assistant training and
interpretability, Claude's constitution, and its agent guidance. Links and API details were checked
on 2026-11-23.

**Not counted in the guide's 149 core hours.** This phase is an optional extension.

---

### Session 7.1 — From base model to helpful assistant: RLHF (~2 h)
- [ ] Done
**Goal:** understand how human feedback turns a pretrained model into an assistant.
**Resource:** Bai et al. (Anthropic), ["Training a Helpful and Harmless Assistant with Reinforcement Learning from Human Feedback"](https://arxiv.org/abs/2204.05862) (2022). Read the abstract, Section 1, and skim the figures.
**Do:**
1. Read the abstract and introduction. Draw the pipeline: pretrained model → preference data → preference (reward) model → RL fine-tuning.
2. Find where the paper discusses the tension between helpfulness and harmlessness, and write down one example.
3. Connect it to Session 4.16: which box on your diagram is this paper?
**Done when:** your pipeline diagram labels what data each stage uses and what each stage produces.
**Knowledge check:**
- What is a preference model, and what is it trained on?
- Why can't you just pretrain on "good" text and skip RLHF?
- What is the helpfulness/harmlessness tension in your own words?

### Session 7.2 — Constitutional AI and Claude's constitution (~2 h)
- [ ] Done
**Goal:** understand training with written principles and AI feedback, and read the document describing the values Claude is trained toward.
**Resource:** Bai et al. (Anthropic), ["Constitutional AI: Harmlessness from AI Feedback"](https://arxiv.org/abs/2212.08073) (2022), abstract and Section 1; [Claude's constitution](https://www.anthropic.com/constitution).
**Do:**
1. Read the Constitutional AI abstract and introduction. Write down the two phases: supervised self-critique and revision, then RL from AI feedback.
2. Read Claude's constitution. Note 3 principles that explain behavior you've seen from Claude, for example while it was building this guide.
3. Compare: how does replacing human labels with AI feedback change the pipeline from Session 7.1?
**Done when:** you have the two-phase diagram plus 3 principles, each paired with a behavior you've observed.
**Knowledge check:**
- What is "RLAIF", and how does it differ from RLHF?
- What does the constitution do during training?
- Name one advantage and one risk of training with AI feedback.

### Session 7.3 — What's inside: the accessible version (~2 h)
- [ ] Done
**Goal:** the big picture of interpretability research on Claude models.
**Resource:** Anthropic, ["Mapping the Mind of a Large Language Model"](https://www.anthropic.com/research/mapping-mind-language-model) and ["Tracing the thoughts of a large language model"](https://www.anthropic.com/research/tracing-thoughts-language-model).
**Do:**
1. Read "Mapping the Mind". What is a "feature", and how were features found?
2. Read "Tracing the thoughts". Write down the examples (planning rhymes, mental math, multi-step reasoning) and one result that surprised you.
3. In one paragraph, connect it to your own GPT: where in your `Block` would these features live?
**Done when:** your paragraph correctly places features in the residual stream / activations of your own model.
**Knowledge check:**
- What is the difference between a neuron and a feature?
- What does "steering" a feature mean (for example, the Golden Gate Bridge demo)?
- What did the research show about whether a model's stated reasoning matches its internal computation?

### Session 7.4 — A mathematical framework for transformer circuits (~2.5 h)
- [ ] Done
**Goal:** see a Transformer as a residual stream that attention heads and MLPs read from and write to. This is the foundation of the technical interpretability papers.
**Resource:** ["A Mathematical Framework for Transformer Circuits"](https://transformer-circuits.pub/2021/framework/index.html) (2021). Read the sections on the residual stream, attention heads as independent and additive, and QK/OV circuits.
**Do:**
1. Read with your Session 4.6 `CausalSelfAttention` open. Map the paper's `W_Q, W_K, W_V, W_O` to your code.
2. Write the residual-stream view of your `Block.forward` as `x = x + attn(ln(x)); x = x + mlp(ln(x))`, and explain why each layer "reads from and writes to" the stream.
3. Explain the QK circuit (where to attend) vs. the OV circuit (what to move) in your own words.
**Done when:** every weight matrix the paper names is mapped to a line of your code, and you have written the QK vs. OV explanation.
**Knowledge check:**
- Why is the residual stream a "communication channel"?
- What do the QK and OV circuits each determine?
- Why can attention heads be analyzed independently?

### Session 7.5 — Superposition (optional) (~2 h)
- [ ] Done
**Goal:** understand why single neurons rarely mean one thing.
**Resource:** ["Toy Models of Superposition"](https://transformer-circuits.pub/2022/toy_model/index.html) (2022). Read the introduction and key results.
**Do:**
1. Read the introduction and the first toy-model results. Recreate one small figure in PyTorch: a tiny model that compresses 5 sparse features into 2 dimensions.
**Done when:** your toy model shows several features sharing fewer dimensions, and you can explain why sparsity allows it.
**Knowledge check:**
- What is superposition?
- Why does feature sparsity make superposition possible?
- Why does superposition make interpreting neurons hard?

### Session 7.6 — Finding features at scale: sparse autoencoders (~2 h)
- [ ] Done
**Goal:** understand how millions of interpretable features were extracted from a production Claude model.
**Resource:** ["Scaling Monosemanticity"](https://transformer-circuits.pub/2024/scaling-monosemanticity/index.html) (2024), introduction and feature examples; [Neuronpedia](https://www.neuronpedia.org/) for exploration.
**Do:**
1. Read the introduction. Draw a sparse autoencoder: activations → wide sparse layer → reconstruction.
2. Browse the paper's feature examples, then explore features on Neuronpedia for an open model. Find 3 features and note what activates each.
**Done when:** you have the SAE diagram, and 3 features with example activating texts.
**Knowledge check:**
- What two things does a sparse autoencoder's loss balance?
- Why does the SAE layer need to be much wider than the activations?
- How do researchers check that a feature means what they think it means?

### Session 7.7 — The biology of a large language model (optional) (~2 h)
- [ ] Done
**Goal:** see the current state of tracing how a model computes an answer step by step.
**Resource:** ["On the Biology of a Large Language Model"](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) (2025). Read the introduction and 2–3 case studies.
**Do:**
1. Read the introduction and pick 2–3 case studies. For each, summarize what the attribution graph showed.
**Done when:** you have summaries of 2–3 case studies with the main finding of each.
**Knowledge check:**
- What is an attribution graph?
- Which case study changed how you think about how Claude "reasons"?
- What are the method's limitations, according to the authors?

### Session 7.8 — Hands-on interpretability with TransformerLens (~2.5 h)
- [ ] Done
**Goal:** open up a real model and look at its activations and attention patterns yourself.
**Resource:** [TransformerLens](https://transformerlensorg.github.io/TransformerLens/) ["Main Demo"](https://transformerlensorg.github.io/TransformerLens/generated/demos/Main_Demo.html); background: ["In-context Learning and Induction Heads"](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) (introduction only).
**Do:**
1. `uv pip install transformer_lens` in your guide venv (CPU or MPS is fine for GPT-2 small).
2. Work through the Main Demo: load `gpt2-small`, run with `run_with_cache`, and inspect activations and attention patterns.
3. Follow the demo's induction-head section on a repeated random token sequence, and find which heads attend to "the token after the previous occurrence".
**Done when:** you've identified at least one induction head (layer and head index) and plotted its attention pattern on a repeated sequence.
**Sticking points:** If the demo's plotting helpers need extra packages, install what the error names. If a device error appears on MPS, run on CPU, since GPT-2 small is fast enough.
**Knowledge check:**
- What is an induction head, and why does it need two attention layers?
- What does `run_with_cache` give you, and how is it like a hook?
- How does this connect to the QK/OV view from Session 7.4?

### Session 7.9 — How agents work (~1.5 h)
- [ ] Done
**Goal:** understand the loop behind tools like Claude Code: model, tools, results, repeat.
**Resource:** Anthropic, ["Building effective agents"](https://www.anthropic.com/research/building-effective-agents); Claude docs, ["Tool use overview"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview) and ["How to implement tool use"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use).
**Do:**
1. Read "Building effective agents". List the difference between workflows and agents, and the patterns it names.
2. Read the tool-use docs. Write down the shape of one round trip: you send `tools`; the model replies with `stop_reason: "tool_use"` and `tool_use` blocks; you run them and send back `tool_result` blocks with matching `tool_use_id`; repeat until `stop_reason: "end_turn"`.
3. Look back at this guide's own creation. Which tool calls (web fetch, shell commands) fit that loop?
**Done when:** you can draw the agent loop and name every message type in one round trip.
**Knowledge check:**
- When should you *not* build an agent, according to the article?
- What does the model actually output when it "calls a tool"?
- Who runs the tool: the model, or your code?

### Session 7.10 — Project: build a mini coding agent (~2.5 h)
- [ ] Done
**Goal:** without a tutorial, write a ~100-line agent loop that talks to Claude and uses tools you define. It's a tiny version of Claude Code.
**Resource:** [Anthropic Python SDK](https://pypi.org/project/anthropic/) (`uv pip install anthropic`); the ["How to implement tool use"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use) docs (reference only).
**Do:**
1. Get API access: create an API key in the Claude Console and `export ANTHROPIC_API_KEY=...`. **This costs money.** `claude-opus-5-5` is $4 / $20 per million input/output tokens (checked 2026-11-23). A session of testing is usually small, but check usage in the Console. You can choose a cheaper model ID from the docs' model list if you prefer.
2. In `~/ai-learning/agent/agent.py`, define 3 tools with JSON schemas: `list_files(path)`, `read_file(path)`, and `write_file(path, content)`. **Restrict all paths to a sandbox folder** such as `~/ai-learning/agent/workspace/`, and reject anything outside it.
3. Write the loop yourself (don't use the SDK's tool runner, because the point is to see the loop): call `client.messages.create(model="claude-opus-5-5", max_tokens=16000, tools=..., messages=...)`, then branch on `response.stop_reason`.
4. Give it a task, for example "create `fizzbuzz.py` in the workspace and a test file for it", and print every tool call it makes.
5. Add a confirmation prompt (`y/n`) before every `write_file`, which is the same idea as Claude Code's permission prompts.
**Done when:** your agent completes the task using several tool calls, every call is printed, writes ask for confirmation, and paths outside the sandbox are refused with an error result.
**Sticking points:**
- Append the model's **whole** `response.content` (not just its text) as the assistant message, otherwise the `tool_use` blocks are lost.
- Return **all** tool results from one turn together in **one** user message, each with the matching `tool_use_id`.
- For a failed tool, send a `tool_result` with `"is_error": true`. Don't drop it.
- Handle every `stop_reason`: `end_turn` (done), `tool_use` (run tools), `max_tokens` (cut off), and `refusal` (the model declined; check before reading content).
- `tool_choice` set to `any` or a specific tool is not supported on this model. Use the default (`auto`) and describe in the prompt when to use each tool.
**Knowledge check:**
- What exactly is in `messages` after 3 tool calls? Print it and explain each entry.
- Why is the sandbox path check essential for an agent that writes files?
- How is your loop the same as, and different from, what Claude Code did while building this guide?

### Session 7.11 — Project: break a circuit (~2.5 h)
- [ ] Done
**Goal:** without a tutorial, test a hypothesis about a model's internals by intervening on it.
**Resource:** your Session 7.8 notebook; the [TransformerLens docs](https://transformerlensorg.github.io/TransformerLens/) (reference only).
**Do:**
1. Using `gpt2-small`, measure the loss on the second half of repeated random token sequences. It should be much lower than on the first half: that's in-context learning.
2. Zero-ablate the induction head(s) you found in Session 7.8 using a hook, and re-measure.
3. Ablate a random non-induction head as a control.
4. Write `INTERP.md`: your hypothesis, method, numbers, a plot, and conclusion.
**Done when:** you have numbers showing whether ablating your induction head(s) raises the repeated-half loss much more than the control head, and `INTERP.md` explains the result honestly (including if the effect is smaller than expected).
**Knowledge check:**
- Why do you need a control ablation?
- If ablating one head barely changes the loss, what might explain that?
- How is this experiment a tiny version of the research in Sessions 7.3–7.7?
