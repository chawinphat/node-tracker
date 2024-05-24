import subprocess

def enter(address: str):
    command = f"ssh -o StrictHostKeyChecking=no {address}"
    subprocess.check_call(command, shell=True)

enter("teddyt@localhost")
