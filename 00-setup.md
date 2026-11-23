# Phase 0 — Set up your Mac (~3 h)

You'll use your M4 Max for everything except the CUDA/Triton sessions in Phase 5, which use a
cloud GPU. Do this once and you're set for the whole guide.

**Why a separate Python:** your system Python is 3.14. PyTorch does ship builds for it, but
course notebooks and libraries lag behind the newest Python. A dedicated environment pinned to
**Python 3.13** avoids version surprises and keeps the guide's packages away from everything
else on your machine. (Checked against PyPI on 2026-11-23: PyTorch 2.15.0 has macOS arm64
wheels for Python 3.11–3.15.)

### Session 0.1 — Create your learning environment (~1.5 h)
- [ ] Done
**Goal:** a working Python 3.13 environment with PyTorch that can use your Mac's GPU.
**Resource:** [uv documentation](https://docs.astral.sh/uv/) — "Getting started" and "Python versions" pages; [PyTorch install page](https://pytorch.org/get-started/locally/) — select Stable / Mac / Pip / Python.
**Do:**
1. Make a workspace for all your code from this guide: `mkdir -p ~/ai-learning && cd ~/ai-learning`
2. Create the environment: `uv venv --python 3.13 .venv` (uv downloads Python 3.13 if you don't have it).
3. Activate it: `source .venv/bin/activate`. Your prompt should now show `(.venv)`. Run this every time you open a new terminal for the guide.
4. Install the core packages: `uv pip install torch numpy matplotlib jupyterlab`
5. Check it works:
   `python -c "import sys, torch; print(sys.version.split()[0], torch.__version__, torch.backends.mps.is_available())"`
6. Check the GPU really computes:
   `python -c "import torch; x = torch.ones(3, device='mps'); print((x * 2).cpu())"`
**Done when:** step 5 prints `3.13.x`, a torch version (2.15 or newer), and `True`. Step 6 prints `tensor([2., 2., 2.])`.
**Sticking points:** If step 5 prints `False` for MPS, run `python -c "import platform; print(platform.machine())"`. It must print `arm64`. If it prints `x86_64`, you're running an Intel (Rosetta) Python: delete `.venv` and recreate it from a native terminal. If `uv` isn't found in a new terminal, open a fresh shell. Never `pip install` into the system Python 3.14.
**Knowledge check:**
- Why does this guide use its own virtual environment instead of your system Python?
- What command do you run in each new terminal before working on the guide?
- What does `torch.backends.mps.is_available()` tell you, and what is "MPS"? (Hint: the PyTorch install page and the [MPS backend notes](https://docs.pytorch.org/docs/stable/notes/mps.html).)

### Session 0.2 — Notebooks, tensors, and a Colab account (~1.5 h)
- [ ] Done
**Goal:** be comfortable opening a notebook and running a few tensor operations, and have a cloud GPU account ready for Phase 5.
**Resource:** [PyTorch "Tensors" tutorial](https://pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html); [JupyterLab docs](https://jupyterlab.readthedocs.io/en/stable/) — "Starting JupyterLab" only; [Google Colab](https://colab.research.google.com/).
**Do:**
1. In `~/ai-learning` with the venv active, run `jupyter lab`. A browser tab opens.
2. Make a new notebook `00-tensors.ipynb` and type the code cells from the PyTorch Tensors tutorial yourself. Don't copy-paste. It's short, and typing builds the habit you'll need for Karpathy's lectures.
3. In one cell, set `device = "mps"`, create a tensor on it, and multiply two 1000×1000 random matrices with `@`. Print the result's `.shape` and `.device`.
4. Open Google Colab, sign in with a personal Google account, and create a notebook. Choose **Runtime → Change runtime type → T4 GPU**. Run `!nvidia-smi`. You won't use it until Phase 5. This step just makes sure you have access before you need it.
**Done when:** your notebook runs the tutorial top to bottom without errors; the matmul cell prints `torch.Size([1000, 1000])` and `mps:0`; and in Colab `!nvidia-smi` shows a Tesla T4.
**Sticking points:** Colab's free GPUs aren't guaranteed. If no GPU is available, try again later. Phase 5 also lists paid alternatives, so you won't be blocked.
**Go deeper:** If you've never used Jupyter, spend 15 minutes on keyboard shortcuts (Shift+Enter runs a cell, `Esc` then `B` adds a cell below).
**Knowledge check:**
- What is a tensor, and how is it different from a Python list?
- How do you move a tensor from the CPU to your Mac's GPU, and back?
- What does `@` do between two tensors, and what has to be true about their shapes?
- Why will you need Colab later, when your Mac already has a GPU?
