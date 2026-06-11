#!/usr/bin/env python3
"""Build the GitHub Pages activity guide from Markdown source."""

from __future__ import annotations

import html
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs" / "page-source" / "activities.md"
OUTPUT = ROOT / "docs" / "index.html"


def slugify(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"\1", text)
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug or "section"


def inline_markdown(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        escaped,
    )
    return escaped


def read_source() -> tuple[dict[str, str], list[str]]:
    lines = SOURCE.read_text(encoding="utf-8").splitlines()
    meta: dict[str, str] = {}
    if lines and lines[0] == "---":
        end = lines.index("---", 1)
        for line in lines[1:end]:
            if ":" in line:
                key, value = line.split(":", 1)
                meta[key.strip()] = value.strip().strip('"')
        lines = lines[end + 1 :]
    return meta, lines


def collect_nav(lines: list[str]) -> list[tuple[str, str]]:
    nav = []
    for line in lines:
        if line.startswith("## "):
            title = line[3:].strip()
            nav.append((slugify(title), title))
    return nav


def render_markdown(lines: list[str]) -> str:
    out: list[str] = []
    in_ul = False
    in_ol = False
    in_code = False
    code_lang = ""
    code_lines: list[str] = []
    section_open = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_code() -> None:
        nonlocal in_code, code_lang, code_lines
        code = html.escape("\n".join(code_lines))
        lang_class = f" language-{html.escape(code_lang)}" if code_lang else ""
        out.append('<div class="copy-block">')
        out.append('<button type="button" class="copy-button">Copy</button>')
        out.append(f'<pre><code class="{lang_class.strip()}">{code}</code></pre>')
        out.append("</div>")
        in_code = False
        code_lang = ""
        code_lines = []

    for raw in lines:
        line = raw.rstrip()
        if in_code:
            if line.startswith("```"):
                flush_code()
            else:
                code_lines.append(raw)
            continue
        if line.startswith("```"):
            close_lists()
            in_code = True
            code_lang = line[3:].strip()
            code_lines = []
            continue
        if not line.strip():
            close_lists()
            continue
        if line.startswith("# "):
            close_lists()
            continue
        if line.startswith("## "):
            close_lists()
            if section_open:
                out.append("</section>")
            title = line[3:].strip()
            classes = "activity-card"
            if not title.lower().startswith("activity"):
                classes += " resource-card"
            out.append(f'<section id="{slugify(title)}" class="{classes}">')
            out.append(f'<h2>{inline_markdown(title)}</h2>')
            section_open = True
            continue
        if line.startswith("### "):
            close_lists()
            out.append(f'<h3>{inline_markdown(line[4:].strip())}</h3>')
            continue
        if line.startswith("> "):
            close_lists()
            out.append(f'<blockquote>{inline_markdown(line[2:].strip())}</blockquote>')
            continue
        if re.match(r"\d+\. ", line):
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            item = re.sub(r"^\d+\. ", "", line)
            out.append(f"<li>{inline_markdown(item)}</li>")
            continue
        if line.startswith("- "):
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{inline_markdown(line[2:].strip())}</li>")
            continue
        if ":" in line and len(line) < 80 and not line.endswith("."):
            close_lists()
            label, value = line.split(":", 1)
            out.append(
                f'<p class="meta-line"><strong>{inline_markdown(label)}:</strong>{inline_markdown(value)}</p>'
            )
            continue
        close_lists()
        out.append(f"<p>{inline_markdown(line)}</p>")

    close_lists()
    if in_code:
        flush_code()
    if section_open:
        out.append("</section>")
    return "\n".join(out)


def build_page() -> str:
    meta, lines = read_source()
    title = meta.get("title", "Using AI Agents for Reproducible Research")
    subtitle = meta.get("subtitle", "Activity guide")
    nav = collect_nav(lines)
    content = render_markdown(lines)
    nav_html = "\n".join(f'<a href="#{slug}">{html.escape(label)}</a>' for slug, label in nav)
    return f"""<!doctype html>
<html lang="en-GB">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{html.escape(title)}</title>
    <meta name="description" content="Activity guide for Using AI Agents for Reproducible Research.">
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%23002047'/%3E%3Cpath d='M16 19h32v26H16z' fill='%23fffaf0'/%3E%3Cpath d='M22 27h20M22 34h14' stroke='%23002047' stroke-width='4' stroke-linecap='round'/%3E%3Ccircle cx='47' cy='45' r='7' fill='%23b31b34'/%3E%3C/svg%3E">
  </head>
  <body>
    <header class="site-header">
      <a class="brand" href="#top">AI Agents for Reproducible Research</a>
      <nav aria-label="Activity navigation">
        {nav_html}
      </nav>
    </header>
    <main id="top">
      <section class="hero">
        <div class="hero-copy">
          <p class="deck-source">{html.escape(subtitle)}</p>
          <h1>{html.escape(title)}</h1>
          <p>Follow the workshop sequence, download the sample files, and copy the prompts you need for Codex.</p>
          <div class="hero-actions">
            <a class="button primary" href="https://github.com/techczech/agents-for-reproducibility/raw/main/workshop-sample-files.zip">Download sample files</a>
            <a class="button secondary" href="https://dominiks-handouts.pages.dev/oa8c">Open public handout</a>
          </div>
        </div>
        <figure class="hero-visual">
          <img src="assets/research-workflow.png" alt="Illustration of a research workflow with files and outputs.">
        </figure>
      </section>
      <section class="guide-shell">
        <aside class="side-nav" aria-label="Page sections">
          <p>Activities</p>
          {nav_html}
        </aside>
        <div class="activity-flow">
          {content}
        </div>
      </section>
    </main>
    <script>
      document.querySelectorAll('.copy-block').forEach((block) => {{
        const button = block.querySelector('.copy-button');
        const code = block.querySelector('code');
        button.addEventListener('click', async () => {{
          await navigator.clipboard.writeText(code.innerText);
          button.textContent = 'Copied';
          setTimeout(() => button.textContent = 'Copy', 1500);
        }});
      }});
    </script>
  </body>
</html>
"""


def main() -> int:
    OUTPUT.write_text(build_page(), encoding="utf-8")
    print(f"wrote {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
