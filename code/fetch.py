#fetch a session JSON file to be used in ssh.py
import os
import json

#returns session name (.json) as string
def find_session(session_name: str=None) -> str:
    if not session_name:
        session_name = "most_recent"
    for dirpath, dirnames, filenames in os.walk("./sessions"):
        if session_name in filenames:
            return os.path.join(dirpath, session_name + ".json")
    return None

# def select_node(address: str, session_path: str, node_name: str):
    
#main function which calls find_session then 
def get_address_with_node_name(session_path: str, node_name: str):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)

    for node_id in range(len(session["node_names"])):
        if session["node_names"][node_id] == node_name:
            return session["addresses"][node_id]
    return None
            
def get_address_with_node_id(session_path: str, node_id: int):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)
    if node_id >= len(session["addresses"]) or node_id < 0:
        return None
    return session["addresses"][node_id] 


