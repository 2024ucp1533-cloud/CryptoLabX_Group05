"""
logger.py
---------
Task 5 utility: maintains a log file that records the date, time, and the
menu option selected for every program execution/action.
"""

import os
from datetime import datetime

LOG_DIR = "outputs"
LOG_FILE = os.path.join(LOG_DIR, "cryptolabx.log")


def log_action(action):
    """
    Append a timestamped record of the selected menu option to the log file.
    Creates the outputs/ directory and log file automatically if missing.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{date_str} {time_str}] Menu Option Selected: {action}\n")


def read_log(last_n=None):
    """Return the log file contents as a list of lines (optionally last N)."""
    if not os.path.isfile(LOG_FILE):
        return []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines[-last_n:] if last_n else lines
