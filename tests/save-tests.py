from code import save
def save_test_invalid_ip():
    addresses = ["192.168.1.1", "10.0.0.256", "172.16.0.1"]
    node_names = ["Node1", "Node2", "Node3"]
    session_name = "MySession"

    try:
        save_session(addresses, node_names, session_name)
    except ValueError as e:
        print(e)
    except NotImplementedError as e:
        print(e)

def save_test_valid_ip():
    addresses = ["192.168.1.1", "10.0.0.255", "172.16.0.1"]
    node_names = ["Node1", "Node2", "Node3"]
    session_name = "MySession"

    try:
        save_session(addresses, node_names, session_name)
    except ValueError as e:
        print(e)
    except NotImplementedError as e:
        print(e)
