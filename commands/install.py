def check_package_exists(package_name: str):
    data = rpc.info(package_name)

    return data['resultcount'] > 0

def run(pkgname: str):
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
