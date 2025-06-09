#!/usr/bin/env python3
"""Command-line interface for PagerDuty Automation Finder."""

import argparse

from pd_finder.core import main as pd_main

def parse_args():
    parser = argparse.ArgumentParser(description="PagerDuty Automation Finder CLI")
    parser.add_argument("--start", type=str, required=True,
                        help="Start datetime in ISO format (e.g., 2021-01-01T00:00:00Z)")
    parser.add_argument("--end", type=str, required=True,
                        help="End datetime in ISO format (e.g., 2021-01-02T00:00:00Z)")
    return parser.parse_args()

def main():
    args = parse_args()
    pd_main(start=args.start, end=args.end)

if __name__ == "__main__":
    main()