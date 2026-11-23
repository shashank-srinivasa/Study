"""Regression tests for learner-facing content fixes from the final review."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read(name):
    return (ROOT / name).read_text()


def section(text, start, end):
    return text[text.index(start):text.index(end)]


def test_tokenizer_split_includes_training_loop_in_4_7():  # I1
    s = section(read("04-gpt.md"), "### Session 4.7", "### Session 4.8")
    assert "00:00:00–00:39:20" in s


def test_gpt2_chapter_warns_cuda_only_calls_on_mac():  # I2
    t = read("04-gpt.md")
    assert "torch.mps.synchronize()" in section(t, "### Session 4.13", "### Session 4.16")


def test_5_9_resets_baseline_before_measuring():  # I3
    s = section(read("05-hardware.md"), "### Session 5.9", "### Session 5.10")
    assert "50257" in s and "B=16, T=1024" in s


def test_nanochat_session_includes_env_setup():  # I4
    s = section(read("04-gpt.md"), "### Session 4.18", "### Session 4.19")
    assert "uv sync --extra cpu" in s


def test_cloud_terminate_and_file_transfer_and_fallback():  # I5
    t = read("05-hardware.md")
    head = t[: t.index("### Session 5.1")]
    assert "Terminate" in head and "scp" in head and "Lambda" in head


def test_spec_resources_present():  # I6
    assert "mml-book" in read("01-math-foundations.md")
    assert "eMlx5fFNoYc" in section(read("04-gpt.md"), "### Session 4.3", "### Session 4.4")


def test_no_unverifiable_crowd_claims():  # I7
    assert "most people say" not in read("03-makemore.md")
    assert "most common advice from people" not in read("README.md")


def test_micrograd_project_uses_double_for_tolerance():  # re-graded minor
    s = section(read("02-micrograd.md"), "### Session 2.7", "**Knowledge check:**\n- Which part")
    assert ".double()" in s


def test_batched_attention_match_uses_eval_mode():  # re-graded minor
    s = section(read("04-gpt.md"), "### Session 4.6", "### Session 4.7")
    assert "model.eval()" in s


def test_3_10_compares_against_lecture_baseline():  # re-graded minor
    s = section(read("03-makemore.md"), "### Session 3.10", "### Session 3.11")
    assert "starter code" in s.split("**Done when:**")[1]
