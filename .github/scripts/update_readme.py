"""Regenerate the repo list in README.md between the REPOS markers.

Standard library only. Reads GITHUB_TOKEN from the environment if set.
"""
import json
import os
import re
import sys
import urllib.request

OWNER = "progineousgb"
README = "README.md"
START = "<!-- REPOS:START -->"
END = "<!-- REPOS:END -->"

# Section order, the topic that selects it, and whether it shows a language column.
SECTIONS = [
    ("library", "Libraries", True),
    ("tool", "Tools", True),
    ("script", "Scripts", False),
    ("config", "Configs and notes", False),
]

# Used only when a repo has none of the topics above.
LANGUAGE_FALLBACK = {"Shell": "script", None: "config", "Jinja": "config", "HCL": "config"}


def api(url):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", "Bearer " + token)
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)


def list_repos():
    repos, page = [], 1
    while True:
        batch = api(f"https://api.github.com/users/{OWNER}/repos?type=owner&per_page=100&page={page}")
        repos += batch
        if len(batch) < 100:
            return repos
        page += 1


def old_descriptions(section):
    """Row text already in the README, used when a repo has no About description."""
    found = {}
    for m in re.finditer(r"^\| \[([^\]]+)\]\([^)]*\) \|(?: [^|]* \|)? (.*) \|$", section, re.M):
        found[m.group(1)] = m.group(2)
    return found


def group_of(repo):
    topics = repo.get("topics") or []
    for topic, _, _ in SECTIONS:
        if topic in topics:
            return topic
    return LANGUAGE_FALLBACK.get(repo.get("language"), "tool")


def render(repos, previous):
    out = []
    for topic, title, with_lang in SECTIONS:
        rows = sorted((r for r in repos if group_of(r) == topic), key=lambda r: r["name"])
        if not rows:
            continue
        out += [f"## {title}", ""]
        out += ["| Repo | Language | What it does |", "| --- | --- | --- |"] if with_lang else ["| Repo | What it does |", "| --- | --- |"]
        for r in rows:
            desc = (r.get("description") or previous.get(r["name"], "")).replace("|", "\\|").strip()
            link = f"[{r['name']}]({r['html_url']})"
            out.append(f"| {link} | {r.get('language') or ''} | {desc} |" if with_lang else f"| {link} | {desc} |")
        out.append("")
    return "\n".join(out)


def main():
    text = open(README, encoding="utf-8").read()
    if START not in text or END not in text:
        sys.exit("README.md has no REPOS markers")
    head, rest = text.split(START, 1)
    current, tail = rest.split(END, 1)
    repos = [r for r in list_repos()
             if not r["private"] and not r["fork"] and not r["archived"] and r["name"] != OWNER]
    new = head + START + "\n\n" + render(repos, old_descriptions(current)) + END + tail
    if new != text:
        open(README, "w", encoding="utf-8").write(new)
        print("README.md updated")
    else:
        print("README.md unchanged")


if __name__ == "__main__":
    main()
