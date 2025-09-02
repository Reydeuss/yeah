#!/usr/bin/python3

import argparse
import requests

parser = argparse.ArgumentParser(
    prog="yeah",
    description="A custom AUR helper written in Python",
)

parser.add_argument("command")
parser.add_argument("keywords")

args = parser.parse_args()

if args.command == "search" and args.keywords:
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
