#!/usr/bin/env python3
"""Typing Game — type each prompt as fast and accurately as you can."""

import random
import time
import sys

PROMPTS = {
    "easy": [
        "print hello world",
        "cats and dogs",
        "python is fun",
        "type this line",
        "keep going now",
        "open the file",
        "save your work",
        "count to ten",
    ],
    "medium": [
        "The quick brown fox jumps over the lazy dog.",
        "Practice typing every day to get faster.",
        "Variables store values that programs can use.",
        "If statements let your program make choices.",
        "A loop repeats a block of code many times.",
        "Functions group steps you want to reuse.",
        "Input from the user always comes in as text.",
        "Debugging means finding and fixing mistakes.",
    ],
    "hard": [
        "for i in range(10): print(i * i)",
        "if score >= 90: grade = 'A'",
        "total = float(input('Enter amount: '))",
        "while n > 0: n = n - 1",
        "def add(a, b): return a + b",
        "colors = ['red', 'green', 'blue']",
        "name = input('What is your name? ')",
        "print(f'Hello, {name}!')",
    ],
}

ROUNDS = 5
GREEN = "\033[32m"
RED = "\033[31m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BOLD = "\033[1m"
DIM = "\033[2m"
RESET = "\033[0m"


def color_enabled():
    return sys.stdout.isatty()


def c(code, text):
    if color_enabled():
        return f"{code}{text}{RESET}"
    return text


def pick_level():
    print()
    print(c(BOLD, "  TYPING GAME"))
    print(c(DIM, "  Type each line. Enter submits. Ctrl+C quits."))
    print()
    print("  1) easy")
    print("  2) medium")
    print("  3) hard")
    print()
    while True:
        choice = input("  Level [1-3]: ").strip()
        if choice in ("1", "easy", "e"):
            return "easy"
        if choice in ("2", "medium", "m", ""):
            return "medium"
        if choice in ("3", "hard", "h"):
            return "hard"
        print("  Pick 1, 2, or 3.")


def wpm(chars, seconds):
    if seconds <= 0:
        return 0.0
    return (chars / 5.0) / (seconds / 60.0)


def accuracy(prompt, typed):
    if not prompt:
        return 100.0
    matches = sum(1 for a, b in zip(prompt, typed) if a == b)
    extra = abs(len(prompt) - len(typed))
    denom = max(len(prompt), len(typed))
    return max(0.0, 100.0 * (matches / denom)) if denom else 100.0


def play_round(prompt, number):
    print()
    print(c(DIM, f"  Round {number}/{ROUNDS}"))
    print(c(CYAN + BOLD, f"  {prompt}"))
    print("  ", end="", flush=True)
    start = time.perf_counter()
    typed = input()
    elapsed = time.perf_counter() - start
    acc = accuracy(prompt, typed)
    speed = wpm(len(typed), elapsed)
    perfect = typed == prompt
    mark = c(GREEN, "perfect") if perfect else c(RED, "miss")
    print(f"  {mark}  {speed:5.1f} WPM  {acc:5.1f}%  {elapsed:4.1f}s")
    return speed, acc, perfect


def main():
    random.seed()
    try:
        level = pick_level()
        pool = PROMPTS[level][:]
        random.shuffle(pool)
        lines = pool[:ROUNDS]
        speeds = []
        accs = []
        hits = 0
        print()
        input(c(YELLOW, "  Press Enter to start..."))
        for i, prompt in enumerate(lines, start=1):
            speed, acc, perfect = play_round(prompt, i)
            speeds.append(speed)
            accs.append(acc)
            if perfect:
                hits += 1
        print()
        print(c(BOLD, "  RESULTS"))
        print(f"  Level:    {level}")
        print(f"  Perfect:  {hits}/{ROUNDS}")
        print(f"  Avg WPM:  {sum(speeds) / len(speeds):.1f}")
        print(f"  Avg acc:  {sum(accs) / len(accs):.1f}%")
        print()
        again = input("  Play again? [y/N] ").strip().lower()
        if again in ("y", "yes"):
            main()
        else:
            print("  Good practice. See you next round.")
            print()
    except KeyboardInterrupt:
        print("\n  Quit. Nice try.")
        print()


if __name__ == "__main__":
    main()
