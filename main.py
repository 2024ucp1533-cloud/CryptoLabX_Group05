"""
CryptoLabX - main.py
=====================
Week 1 entry point: a menu-driven command-line interface for the
CryptoLabX cryptanalysis toolkit.

Current scope (Assignment 1 / Week 1):
    - Menu framework (Encrypt / Decrypt / Attack / Analyze / Exit)
    - Dataset text-file analysis (character/word/line/unique-char counts,
      letter frequency)
    - Session logging (date, time, selected option)

No cryptographic algorithms are implemented yet -- those modules
(classical/, attacks/, modern/, math/) will be filled in during later
assignments. Selecting Encrypt, Decrypt, or Attack currently shows a
"Coming Soon" placeholder.
"""

from utils.logger import log_action
from utils.file_analysis import (
    list_dataset_files,
    read_dataset_file,
    analyze_text,
    format_report,
)

DATASETS_DIR = "datasets"


def print_banner():
    print("=" * 45)
    print("           CryptoLabX Toolkit")
    print("      Junior Cryptanalyst Workstation")
    print("=" * 45)


def print_menu():
    print("\nMain Menu")
    print("---------")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Attack")
    print("4. Analyze")
    print("5. Exit")


def coming_soon(feature_name):
    print(f"\n[{feature_name}] -> Coming Soon! This module will be built in a later assignment.")


def run_analyze():
    """Task 4: let the user pick a dataset file and view its statistics."""
    files = list_dataset_files(DATASETS_DIR)

    if not files:
        print(f"\nNo .txt files found in '{DATASETS_DIR}/'. Please add some dataset files first.")
        return

    print("\nAvailable dataset files:")
    for idx, fname in enumerate(files, start=1):
        print(f"  {idx}. {fname}")

    choice = input(f"\nSelect a file (1-{len(files)}), or 0 to cancel: ").strip()

    if not choice.isdigit() or not (0 <= int(choice) <= len(files)):
        print("Invalid selection.")
        return

    choice = int(choice)
    if choice == 0:
        return

    filename = files[choice - 1]
    try:
        text = read_dataset_file(filename, DATASETS_DIR)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return

    stats = analyze_text(text)
    print(format_report(filename, stats))


def main():
    print_banner()

    while True:
        print_menu()
        choice = input("Select an option (1-5): ").strip()

        if choice == "1":
            log_action("Encrypt")
            coming_soon("Encrypt")
        elif choice == "2":
            log_action("Decrypt")
            coming_soon("Decrypt")
        elif choice == "3":
            log_action("Attack")
            coming_soon("Attack")
        elif choice == "4":
            log_action("Analyze")
            run_analyze()
        elif choice == "5":
            log_action("Exit")
            print("\nExiting CryptoLabX. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a number between 1 and 5.")


if __name__ == "__main__":
    main()
