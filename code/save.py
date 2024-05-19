from typing import List
import ipaddress
import json
from datetime import datetime


def is_valid_ip(address: str):
    try:
        ip_obj = ipaddress.ip_address(address)
        #print(f"{address} is a valid IP address")
        return True
    except ValueError:
        return False

def save_session_to_json(addresses: List[str], node_names: List[str], session_name: str):

    # datetime object containing current date and time
    now = datetime.now()
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

    session_info = {
        "addresses": addresses,
        "node_names": node_names,
        "session_name": session_name,
        "save_time": dt_string
    }

    session_json_object = json.dumps(session_info, indent=4)
    #no session name given, save to default name
    if session_name == None:
        file_name = "most_recent.json"
    else:
        file_name = session_name.lower() + ".json"
    save_path = "sessions/" + file_name

    with open(save_path, "w") as outfile:
        outfile.write(session_json_object)
        print("written json file")

#main function
def save_session(addresses: List[str], node_names: List[str] = None, session_name: str = None):
    #check if addresses are correctly formatted
    for address in addresses:
        if not is_valid_ip(address):
            raise ValueError(f"Error: Invalid IP address found: {address}")
    
    if len(addresses) != len(node_names):
        raise IndexError("Error: Number of addresses and node names are not equal.")
    
    #formulate json file
    save_session_to_json(addresses, node_names, session_name)

addresses = ["192.168.1.1", "10.0.0.255", "172.16.0.1"]
node_names = ["Node1", "Node2", "Node3"]
session_name = "MySession"

try:
    save_session(addresses, node_names, session_name)
except ValueError as e:
    print(e)
except NotImplementedError as e:
    print(e)

