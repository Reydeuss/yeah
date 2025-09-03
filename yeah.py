#!/usr/bin/python3

import argparse
import os
import subprocess
import sys
import requests

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

    rpc_url = f'https://aur.archlinux.org/rpc/v5/search/{args.keywords}'
    r = requests.get(rpc_url)
    data = r.json()
    count = data['resultcount']
    print(f'Got {count} results.')

    if count > 0:
        for result in data['results']:
            print(f'aur/{result['Name']} {result['Version']}')
            print(f'{result["Description"]}')
            print('') # Newline
    else:
        print('Maybe try another keyword?')

def check_package_exists(package_name: str):
    rpc_url = f'https://aur.archlinux.org/rpc/v5/info/{package_name}'
    r = requests.get(rpc_url)
    data = r.json()

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
