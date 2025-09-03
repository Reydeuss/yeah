import requests

def search(term: str):
    url = f'https://aur.archlinux.org/rpc/v5/search/{term}'
    r = requests.get(url)

    return r.json()

def info(pkgname: str):
    url = f'https://aur.archlinux.org/rpc/v5/info/{pkgname}'
    r = requests.get(url)

    return r.json()
