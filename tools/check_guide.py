#!/usr/bin/env python3
"""Checks that guide chapters follow the session format, hour budgets, and live links."""
from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

HEADING = re.compile(r"^### Session (\d+\.\d+) — (.+?) \(~?([\d.]+) h\)\s*$")
FIELD = re.compile(r"^\*\*(Goal|Resource|Do|Done when|Sticking points|Go deeper|Knowledge check):\*\*\s*(.*)$")
REQUIRED = ("Goal", "Resource", "Do", "Done when", "Knowledge check")
MIN_KC = 3
MIN_H, MAX_H = 1.0, 2.5
MD_LINK = re.compile(r"\]\((https?://[^)\s]+)\)")
BARE = re.compile(r"(?<![(\[])\bhttps?://[^\s)\]>`\"']+")


@dataclass
class Session:
    id: str
    title: str
    hours: float
    optional: bool
    line: int
    fields: dict[str, str] = field(default_factory=dict)
    has_checkbox: bool = False
    kc_count: int = 0


def parse_sessions(text: str) -> list[Session]:
    sessions: list[Session] = []
    cur: Session | None = None
    in_kc = False
    for n, raw in enumerate(text.splitlines(), 1):
        m = HEADING.match(raw)
        if m:
            title = m.group(2)
            cur = Session(m.group(1), title, float(m.group(3)), "(optional)" in title, n)
            sessions.append(cur)
            in_kc = False
            continue
        if raw.startswith("#"):
            cur = None
            continue
        if cur is None:
            continue
        if in_kc and re.match(r"^\s*(-|\d+\.)\s+\S", raw):
            cur.kc_count += 1
        if raw.strip().startswith("- [ ]") or raw.strip().startswith("- [x]"):
            cur.has_checkbox = True
        f = FIELD.match(raw)
        if f:
            cur.fields[f.group(1)] = f.group(2)
            in_kc = f.group(1) == "Knowledge check"
    return sessions


def validate(sessions: list[Session]) -> list[str]:
    errs: list[str] = []
    seen: set[str] = set()
    for s in sessions:
        where = f"Session {s.id} (line {s.line})"
        if s.id in seen:
            errs.append(f"{where}: duplicate session id {s.id}")
        seen.add(s.id)
        for req in REQUIRED:
            if req not in s.fields:
                errs.append(f"{where}: missing field '{req}'")
        if not (MIN_H <= s.hours <= MAX_H):
            errs.append(f"{where}: hours {s.hours} outside {MIN_H}-{MAX_H}")
        if "Knowledge check" in s.fields and s.kc_count < MIN_KC:
            errs.append(f"{where}: Knowledge check has {s.kc_count} questions, needs at least {MIN_KC}")
        if not s.has_checkbox:
            errs.append(f"{where}: missing '- [ ] Done' checkbox")
    return errs


def extract_urls(text: str) -> list[str]:
    found = MD_LINK.findall(text) + BARE.findall(text)
    out: list[str] = []
    for u in found:
        u = u.rstrip(".,;:")
        if u not in out:
            out.append(u)
    return out


def check_url(url: str, timeout: float = 15) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (guide-link-check)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return True, str(r.status)
    except urllib.error.HTTPError as e:
        if e.code in (403, 429, 999):
            return True, f"warn {e.code}"
        return False, str(e.code)
    except Exception as e:  # network errors, timeouts
        return False, type(e).__name__


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--hours", nargs=2, type=float, metavar=("MIN", "MAX"))
    ap.add_argument("--total", nargs=2, type=float, metavar=("MIN", "MAX"))
    ap.add_argument("--links", action="store_true")
    a = ap.parse_args(argv)
    ok = True
    total = 0.0
    for f in a.files:
        p = Path(f)
        if not p.exists():
            print(f"ERROR {f}: file not found")
            ok = False
            continue
        text = p.read_text()
        sessions = parse_sessions(text)
        core = sum(s.hours for s in sessions if not s.optional)
        opt = sum(s.hours for s in sessions if s.optional)
        total += core
        print(f"{f}: sessions={len(sessions)} core={core:g} optional={opt:g}")
        for e in validate(sessions):
            print(f"ERROR {f}: {e}")
            ok = False
        if a.hours and not (a.hours[0] <= core <= a.hours[1]):
            print(f"ERROR {f}: core hours {core:g} outside {a.hours[0]:g}-{a.hours[1]:g}")
            ok = False
        if a.links:
            for u in extract_urls(text):
                good, why = check_url(u)
                if not good:
                    print(f"ERROR {f}: dead link {u} ({why})")
                    ok = False
                elif why.startswith("warn"):
                    print(f"WARN {f}: {u} ({why})")
    print(f"total core={total:g}")
    if a.total and not (a.total[0] <= total <= a.total[1]):
        print(f"ERROR total core {total:g} outside {a.total[0]:g}-{a.total[1]:g}")
        ok = False
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
