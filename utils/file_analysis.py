"""
file_analysis.py
-----------------
Task 4 utility: reads a text file from the datasets/ folder and reports
basic statistics -- character count, word count, line count, unique
character count, and letter frequency distribution.
"""

import os
import string
from collections import Counter


def list_dataset_files(datasets_dir="datasets"):
    """Return a sorted list of .txt files available in the datasets folder."""
    if not os.path.isdir(datasets_dir):
        return []
    return sorted(
        f for f in os.listdir(datasets_dir)
        if f.lower().endswith(".txt")
    )


def read_dataset_file(filename, datasets_dir="datasets"):
    """Read and return the full text content of a dataset file."""
    filepath = os.path.join(datasets_dir, filename)
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"'{filename}' not found in '{datasets_dir}/'")

    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def analyze_text(text):
    """
    Compute basic statistics for the given text.

    Returns a dictionary with:
        char_count       - total number of characters (including spaces/newlines)
        word_count        - total number of whitespace-separated words
        line_count        - total number of lines
        unique_char_count - number of distinct characters used
        letter_frequency  - Counter of A-Z letter frequencies (case-insensitive)
    """
    char_count = len(text)
    word_count = len(text.split())
    # Count lines: handle files with/without a trailing newline gracefully
    line_count = len(text.splitlines())
    unique_char_count = len(set(text))

    letters_only = [ch.upper() for ch in text if ch.isalpha()]
    letter_frequency = Counter(letters_only)

    return {
        "char_count": char_count,
        "word_count": word_count,
        "line_count": line_count,
        "unique_char_count": unique_char_count,
        "letter_frequency": letter_frequency,
    }


def format_report(filename, stats):
    """Format the analysis results into a readable report string."""
    lines = []
    lines.append(f"\n--- Analysis Report: {filename} ---")
    lines.append(f"Characters       : {stats['char_count']}")
    lines.append(f"Words            : {stats['word_count']}")
    lines.append(f"Lines            : {stats['line_count']}")
    lines.append(f"Unique Characters: {stats['unique_char_count']}")
    lines.append("\nLetter Frequency (A-Z):")

    freq = stats["letter_frequency"]
    total_letters = sum(freq.values()) or 1  # avoid division by zero

    for letter in string.ascii_uppercase:
        count = freq.get(letter, 0)
        if count > 0:
            pct = (count / total_letters) * 100
            bar = "#" * min(count, 50)
            lines.append(f"  {letter}: {count:>4}  ({pct:5.2f}%)  {bar}")

    lines.append("-" * 40)
    return "\n".join(lines)
