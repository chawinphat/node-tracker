import typer
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint
from typing import List

from save import save_session
from fetch import *
from ssh import enter
from interface import display_session_json

app = typer.Typer()

@app.command()
def hello(name: str):
    print(f"Hello {name}")

@app.command("save")
def save_session_command(addresses: List[str], node_names: List[str] = None, session_name: str = None):
    save_session(addresses, node_names, session_name)

@app.command("enter")
def enter_session_command(session_name: str=None, node_id: int=None, node_name: str=None):
    session_path = find_session(session_name)
    if not session_path:
        raise FileNotFoundError("Session does not exist")
    
    if node_id:
        node_address = get_address_with_node_id(session_path, node_id)
        if not node_address:
            raise IndexError("Node Id specified is invalid")
    else: #display the path
        #cli interface here with selection argument
        display_session_json(session_path)
        input = 
    enter(node_address)


if __name__ == "__main__":
    app() 
