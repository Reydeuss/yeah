#!/usr/bin/python3

import argparse
import os
import subprocess
import sys

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
    if not args.keywords:
        print("Aborting operation due to bad usage.")
        print("Format: yeah search <keywords>")
        sys.exit(1)

    data = rpc.search(args.keywords)
    count = data['resultcount']
    print(f'Got {count} results.')

    if count > 0:
        for result in data['results']:
            print(f'aur/{result["Name"]} {result["Name"]}')
            print(f'{result["Description"]}')
            print('') # Newline
    else:
        print('Maybe try another keyword?')

def check_package_exists(package_name: str):
    data = rpc.info(package_name)

    return data['resultcount'] > 0

if args.command == "install":
    if not args.keywords:
        print("Aborting operation due to bad usage.")
        print("Format: yeah install <keywords>")
        sys.exit(1)

    pkgname = args.keywords

    if not check_package_exists(pkgname):
        print("There is no package with that identifier!")
        print("Try another keyword?")
        sys.exit(1)

    yeah_dir = Path('~/.yeah/').expanduser()
    yeah_dir.mkdir(parents=True, exist_ok=True)
    os.chdir(yeah_dir)

    git_url = f'https://aur.archlinux.org/{pkgname}.git'
    cmd = f'git clone {git_url}'
    subprocess.run(cmd.split())

    os.chdir(pkgname)
    cmd = 'makepkg -si'
    subprocess.run(cmd.split())
