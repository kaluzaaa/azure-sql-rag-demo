"""Command line: `uv run demo load`."""

import argparse

from demo.load import load


def main() -> None:
    parser = argparse.ArgumentParser(prog="demo", description="Azure SQL RAG demo")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("load", help="create the schema and load data/ with embeddings")
    args = parser.parse_args()
    if args.command == "load":
        load()
