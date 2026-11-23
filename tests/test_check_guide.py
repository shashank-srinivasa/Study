import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))
from check_guide import parse_sessions, validate, extract_urls  # noqa: E402

FIX = Path(__file__).parent / "fixtures"
CLI = Path(__file__).resolve().parent.parent / "tools" / "check_guide.py"


def load(name):
    return (FIX / name).read_text()


def test_parses_good_fixture():
    s = parse_sessions(load("good.md"))
    assert [x.id for x in s] == ["1.1", "1.2"]
    assert [x.hours for x in s] == [2.0, 1.5]
    assert all(x.has_checkbox for x in s)
    assert validate(s) == []


def test_missing_done_when_reported():
    errs = validate(parse_sessions(load("missing_done_when.md")))
    assert any("1.1" in e and "Done when" in e for e in errs)


def test_hours_out_of_range_reported():
    errs = validate(parse_sessions(load("bad_hours.md")))
    assert any("hours" in e for e in errs)


def test_optional_hours_separate():
    s = parse_sessions(load("optional.md"))
    assert sum(x.hours for x in s if not x.optional) == 2.0
    assert sum(x.hours for x in s if x.optional) == 1.5


def test_duplicate_session_id_reported():
    errs = validate(parse_sessions(load("duplicate.md")))
    assert any("duplicate" in e.lower() and "1.1" in e for e in errs)


def test_extract_urls():
    urls = extract_urls("[a](https://x.com/1) and https://x.com/2 and [b](https://x.com/1)")
    assert urls == ["https://x.com/1", "https://x.com/2"]


def test_cli_hours_bounds():
    r = subprocess.run([sys.executable, str(CLI), str(FIX / "good.md"), "--hours", "10", "20"])
    assert r.returncode == 1


def test_cli_ok():
    r = subprocess.run([sys.executable, str(CLI), str(FIX / "good.md"), "--hours", "1", "5"],
                       capture_output=True, text=True)
    assert r.returncode == 0
    assert "core=3.5" in r.stdout


def test_cli_missing_file_fails():
    r = subprocess.run([sys.executable, str(CLI), str(FIX / "nope.md")])
    assert r.returncode == 1


def test_knowledge_check_required():
    errs = validate(parse_sessions(load("no_kc.md")))
    assert any("Knowledge check" in e for e in errs)


def test_knowledge_check_needs_three_questions():
    errs = validate(parse_sessions(load("short_kc.md")))
    assert any("Knowledge check" in e and "3" in e for e in errs)
