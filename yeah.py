#!/usr/bin/python3

import argparse
import os
import subprocess
import sys

import commands

from aur import rpc
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="yeah",
    description="A custom AUR helper written in Python",
)

parser.add_argument("command")
parser.add_argument("keywords", nargs='?', default=None)

args = parser.parse_args()

if args.command == "search":
    term = args.keywords

    if not term:
        print("Aborting operation due to bad usage.")
        print("Format: yeah search <keywords>")
        sys.exit(1)

    commands.search.run(term)

if args.command == "install":
    if not args.keywords:
        print("Aborting operation due to bad usage.")
        print("Format: yeah install <keywords>")
        sys.exit(1)

    pkgname = args.keywords

    commands.install.run()
