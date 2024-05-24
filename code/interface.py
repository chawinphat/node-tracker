import json
from rich import print as rprint
from PyInquirer import prompt, print_json, Separator

def display_session_json(session_path):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)
    rprint("[yellow]=============================================[yello]")
    if not session["node_names"]:
        for node_id in range(len(session["addresses"])):
            print(node_id, ":", session["addresses"][node_id])
    else:
        for node_id in range(len(session["addresses"])):
            print(node_id, ":", session["addresses"][node_id], session["node_names"][node_id])

#display_session_json("most_recent.json")

def display_session_new(session_path):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)

    choices = []
    padding = 4
    max_node_address = max(len(adr) for adr in session["addresses"]) + padding
    max_node_id = len(session["addresses"]) - 1 + padding
    max_node_name = None
    if session["node_names"]:
        max_node_name = max(len(name) for name in session["node_names"]) + padding
    for node_id in range(len(session["addresses"])):
        row = ""
        row += str(node_id).ljust(max_node_id)
        row += session["addresses"][node_id].ljust(max_node_address)
        if max_node_name:
            row += session["node_names"][node_id].ljust(max_node_name)
        choices.append({"value": node_id, "name": row})

    
    module_list_question = questions = [
        {
            'type': 'list',
            'name': 'username',
            'message': 'Select any one node: ',
            'choices': choices,
        }
    ]

    username = prompt(module_list_question)
    print(username)
    rprint("[yellow]=============================================[yello]")
    rprint("[green bold]Enter folder name :[green bold]")

display_session_new("most_recent.json")



