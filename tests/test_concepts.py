"""Phase 1 must be meaning-first: concept cards plus 'Before this' links in every math session."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARTS = ("**What it is:**", "**Why it exists:**", "**In AI:**", "**Self-test:**", "**If shaky:**")


def cards():
    text = (ROOT / "01-concepts.md").read_text()
    return re.findall(r"^### (C\d+) — (.+?)\n(.*?)(?=^### C\d+ — |\Z)", text, re.S | re.M)


def test_concept_cards_exist_and_are_complete():
    cs = cards()
    assert len(cs) >= 28
    for cid, title, body in cs:
        for part in PARTS:
            assert part in body, f"{cid} {title} missing {part}"


def test_every_math_session_links_its_prerequisites():
    text = (ROOT / "01-math-foundations.md").read_text()
    anchors = {f"{cid.lower()}-" for cid, _, _ in cards()}
    sessions = re.findall(r"^### Session (1\.\d+) — .*?(?=^### Session |\Z)", text, re.S | re.M)
    bodies = re.split(r"^### Session ", text, flags=re.M)[1:]
    for body in bodies:
        sid = body.split(" ", 1)[0]
        if sid == "1.0":
            continue
        assert "**Before this:**" in body, f"Session {sid} has no Before this"
        links = re.findall(r"01-concepts\.md#(c\d+-)", body)
        assert links, f"Session {sid} links no concept cards"
        for l in links:
            assert l in anchors, f"Session {sid} links unknown card {l}"


def test_session_1_0_diagnostic_exists():
    assert "### Session 1.0 — " in (ROOT / "01-math-foundations.md").read_text()


def test_partial_derivatives_taught_in_1_12():
    text = (ROOT / "01-math-foundations.md").read_text()
    s = text[text.index("### Session 1.12"):text.index("### Session 1.13")]
    assert "partial derivative" in s.lower()


def test_every_card_links_at_least_one_tutorial():
    for cid, title, body in cards():
        m = re.search(r"\*\*Learn it:\*\*(.*?)(?=\*\*If shaky:\*\*)", body, re.S)
        assert m, f"{cid} has no Learn it"
        assert re.search(r"\]\(https?://", m.group(1)), f"{cid} Learn it has no link"
