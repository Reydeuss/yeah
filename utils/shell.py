import subprocess

def git_clone(url: str):
    cmd = f'git clone {url}'
    subprocess.run(cmd.split())
