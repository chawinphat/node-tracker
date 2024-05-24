#fetch a session JSON file to be used in ssh.py
import os
import json

#returns session name (.json) as string
def find_session(session_name: str) -> str:
    for dirpath, dirnames, filenames in os.walk("./sessions"):
        if session_name in filenames:
            return os.path.join(dirpath, session_name + ".json")
    raise FileNotFoundError("Session could not be found")

# def select_node(address: str, session_path: str, node_name: str):
    
#main function which calls find_session then 
def get_address_with_node_name(session_path: str, node_name: str):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)

    for i in range(len(session["node_names"])):
        if session["node_names"][i] == node_name:
            return session["addresses"][i]
    return None
            
def get_address_with_node_id(session_path: str, node_id: int):
    session_file = open("./sessions/" + session_path, 'r')
    session = json.load(session_file)
    return session["addresses"][node_id] 


