#!/usr/bin/env python3
"""
Basic Python program: prints a greeting.
Usage: python Testing1.py --name Alice --count 3
"""

import argparse

def greet(name: str, count: int = 1) -> None:
    """Print a greeting count times."""
    for i in range(count):
        print(f"Hello, {name}!")

def parse_args():
    parser = argparse.ArgumentParser(description="Print a greeting multiple times.")
    parser.add_argument("--name", "-n", default="World", help="Name to greet")
    parser.add_argument("--count", "-c", type=int, default=1, help="Number of times to print")
    return parser.parse_args()

def main():
    args = parse_args()
    greet(args.name, args.count)

if __name__ == "__main__":
    main()