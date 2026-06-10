#!/usr/bin/env python3
"""Build deterministic workshop sample files for the messy archive exercise."""

from __future__ import annotations

import csv
import math
import random
import wave
from pathlib import Path

from openpyxl import Workbook
from PIL import Image, ImageDraw
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


REPO_ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = REPO_ROOT / "sample-files" / "messy-research-archive"


def ensure_dirs() -> None:
    for name in [
        "00_admin",
        "01_raw_exports",
        "02_notes and transcripts",
        "03_large-ish mock files",
        "figures FINAL",
        "old-analysis",
        "misc",
    ]:
        (ARCHIVE / name).mkdir(parents=True, exist_ok=True)


def write_text(path: Path, body: str) -> None:
    path.write_text(body.strip() + "\n", encoding="utf-8")


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_workbook(path: Path, sheets: dict[str, list[list[object]]]) -> None:
    wb = Workbook()
    default = wb.active
    wb.remove(default)
    for title, rows in sheets.items():
        ws = wb.create_sheet(title=title)
        for row in rows:
            ws.append(row)
    wb.save(path)


def write_pdf(path: Path, title: str, paragraphs: list[str]) -> None:
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    c.setFont("Helvetica-Bold", 16)
    c.drawString(72, height - 72, title)
    c.setFont("Helvetica", 10)
    y = height - 110
    for paragraph in paragraphs:
        for line in wrap(paragraph, 88):
            c.drawString(72, y, line)
            y -= 14
            if y < 80:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = height - 72
        y -= 10
    c.save()


def wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line: list[str] = []
    for word in words:
        if sum(len(part) for part in line) + len(line) + len(word) > width:
            lines.append(" ".join(line))
            line = [word]
        else:
            line.append(word)
    if line:
        lines.append(" ".join(line))
    return lines


def write_image(path: Path, size: tuple[int, int], seed: int, label: str) -> None:
    rng = random.Random(seed)
    image = Image.new("RGB", size, (242, 242, 236))
    draw = ImageDraw.Draw(image)
    for _ in range(420):
        x0 = rng.randrange(0, size[0])
        y0 = rng.randrange(0, size[1])
        x1 = min(size[0], x0 + rng.randrange(20, 220))
        y1 = min(size[1], y0 + rng.randrange(10, 160))
        colour = (
            rng.randrange(35, 215),
            rng.randrange(45, 205),
            rng.randrange(50, 220),
        )
        draw.rectangle((x0, y0, x1, y1), outline=colour, width=rng.randrange(1, 4))
    draw.rectangle((24, 24, size[0] - 24, 86), fill=(250, 250, 246), outline=(40, 40, 40))
    draw.text((44, 46), label, fill=(20, 20, 20))
    image.save(path, quality=88)


def write_wav(path: Path) -> None:
    sample_rate = 16000
    duration_seconds = 45
    with wave.open(str(path), "w") as handle:
        handle.setnchannels(1)
        handle.setsampwidth(2)
        handle.setframerate(sample_rate)
        for i in range(sample_rate * duration_seconds):
            value = int(12000 * math.sin(2 * math.pi * 440 * i / sample_rate))
            handle.writeframesraw(value.to_bytes(2, byteorder="little", signed=True))


def write_noise_png(path: Path, size: tuple[int, int], seed: int) -> None:
    rng = random.Random(seed)
    pixels = bytes(rng.randrange(0, 256) for _ in range(size[0] * size[1]))
    image = Image.frombytes("L", size, pixels)
    image.save(path)


def write_large_mock_csv(path: Path) -> None:
    rng = random.Random(20260610)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow(["record_id", "timestamp", "sensor_a", "sensor_b", "status", "comment"])
        for i in range(60000):
            writer.writerow(
                [
                    f"M{i:06}",
                    f"2025-03-{1 + (i % 28):02}T{(i // 3600) % 24:02}:{(i // 60) % 60:02}:{i % 60:02}",
                    round(rng.uniform(10, 90), 4),
                    round(rng.uniform(0, 1), 6),
                    ["ok", "check", "repeat", "missing"][i % 4],
                    "fictional high-volume mock export",
                ]
            )


def build() -> None:
    ensure_dirs()

    survey_rows = [
        {
            "response_id": f"R{i:03}",
            "wave": "pilot" if i < 8 else "main",
            "group": ["control", "intervention", "unknown"][i % 3],
            "confidence_pre": 2 + (i % 4),
            "confidence_post": 3 + (i % 5),
            "free_text": [
                "Useful but I need clearer steps.",
                "The folder was hard to understand.",
                "I liked having outputs to inspect.",
                "Not sure which file is final.",
            ][i % 4],
        }
        for i in range(1, 31)
    ]
    write_csv(ARCHIVE / "01_raw_exports" / "survey_export_2025-03-04.csv", survey_rows)
    write_csv(ARCHIVE / "01_raw_exports" / "survey_export_FINAL_final.csv", list(reversed(survey_rows[:24])))
    write_csv(
        ARCHIVE / "00_admin" / "participant_lookup_DO_NOT_USE_mock.csv",
        [
            {"participant_code": f"P{i:02}", "consent": "yes", "notes": "fictional mock row"}
            for i in range(1, 13)
        ],
    )

    write_workbook(
        ARCHIVE / "01_raw_exports" / "coding_export_nodes_v3.xlsx",
        {
            "Nodes": [
                ["node", "count", "review_status"],
                ["setup friction", 14, "needs merge"],
                ["documentation", 22, "reviewed"],
                ["publishing uncertainty", 9, "unclear"],
            ],
            "Memos": [
                ["memo_id", "summary"],
                ["M01", "Several notes refer to the same setup issue."],
                ["M02", "Final labels may not match transcript headings."],
            ],
        },
    )
    write_workbook(
        ARCHIVE / "old-analysis" / "analysis_workbook_old_DO_NOT_USE.xlsx",
        {
            "Sheet1": [
                ["metric", "value"],
                ["mean_pre", 3.2],
                ["mean_post", 4.1],
                ["missing_rows", 6],
            ]
        },
    )

    write_text(
        ARCHIVE / "02_notes and transcripts" / "Interview notes clean FINAL v2.txt",
        """
        Interview A notes. The participant described using a local folder, then losing
        track of which transcript had been cleaned. They wanted the agent to explain
        its file changes before making them. This is fictional mock content.
        """,
    )
    write_text(
        ARCHIVE / "02_notes and transcripts" / "transcript_A_raw_unchecked.txt",
        """
        SPEAKER 1: I put everything in Downloads first.
        SPEAKER 2: Then what happened?
        SPEAKER 1: I made a folder called final but it has old files too.
        [inaudible]
        """,
    )
    write_text(
        ARCHIVE / "misc" / "README maybe for archive.txt",
        """
        Notes from an imaginary assistant handover. Some file names are misleading on
        purpose. No file contains real participant data.
        """,
    )
    write_text(
        ARCHIVE / "old-analysis" / "draft-findings-notes.md",
        """
        # Draft findings

        These notes are deliberately rough. The exercise is to ask an agent to inspect
        the folder, build an inventory, identify duplicates, and propose a cleaner
        structure before moving or renaming anything.
        """,
    )

    write_pdf(
        ARCHIVE / "00_admin" / "ethics-draft-final-v2.pdf",
        "Mock ethics draft",
        [
            "This fictional PDF imitates a short administrative document. It exists so the archive contains a realistic mix of file formats.",
            "The file should not be treated as a completed ethics document. It is placeholder content for a folder-organisation exercise.",
        ],
    )
    write_pdf(
        ARCHIVE / "misc" / "scan-from-printer-001.pdf",
        "Mock scanned note",
        [
            "A short scanned-note placeholder. The vague name is intentional because participants will practise asking Codex to infer likely categories from content.",
        ],
    )

    write_image(ARCHIVE / "figures FINAL" / "Figure 1 final FINAL.png", (1600, 1000), 11, "Mock figure final FINAL")
    write_image(ARCHIVE / "figures FINAL" / "IMG_0042.JPG", (2400, 1600), 42, "Mock field image")
    write_image(ARCHIVE / "misc" / "screenshot-data-cleaning.png", (1400, 900), 87, "Mock screenshot")
    write_wav(ARCHIVE / "misc" / "meeting_audio_clip_placeholder.wav")
    write_noise_png(ARCHIVE / "03_large-ish mock files" / "raw-camera-export-not-reviewed.png", (2600, 1800), 19)
    write_noise_png(ARCHIVE / "03_large-ish mock files" / "scan_batch_07_uncropped.png", (2200, 1600), 31)
    write_large_mock_csv(ARCHIVE / "03_large-ish mock files" / "sensor_export_all_rows_maybe_final.csv")


if __name__ == "__main__":
    build()
