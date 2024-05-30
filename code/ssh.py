import subprocess

def enter(address: str):
    command = f"ssh -o StrictHostKeyChecking=no {address}"
    print(f"Connecting to {address}...")
    subprocess.check_call(command, shell=True)
    return None
#enter("teddyt@localhost")
