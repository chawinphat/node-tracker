import json
from rich import print as rprint
from PyInquirer import prompt, print_json, Separator
#display_session_json("most_recent.json")

def display_session(session_path):
    session_file = open(session_path, 'r')
    session = json.load(session_file)

    choices = []
    padding = 4
    max_node_address = max(len(adr) for adr in session["addresses"]) + padding
    max_node_id = len(str(len(session["addresses"]))) - 1 + padding

    max_node_name = None
    if session["node_names"]:
        max_node_name = max(len(name) for name in session["node_names"]) + padding
    
    #form table headers
    header = "| " + "Node Id".ljust(max_node_id) + "| " + "IP Address".ljust(max_node_address) + "| "
    if max_node_name:
        header += "Name".ljust(max_node_name) + "|"

    #form table rows
    for node_id in range(len(session["addresses"])):
        row = ""
        row += str(node_id).ljust(max_node_id)
        row += session["addresses"][node_id].ljust(max_node_address)
        if max_node_name:
            row += session["node_names"][node_id].ljust(max_node_name)
        choices.append({"value": node_id, "name": row})

    
    module_list_question = [
        {
            'type': 'list',
            'name': 'nodeId',
            'message': "Select Node",
            'choices': choices,
        }
    ]
    
    #display
    rprint("[yellow]=============================================[yellow]")
    #print(header)
    selection = prompt(module_list_question)["nodeId"]
    return selection
    
# display_session("mysession.json")



