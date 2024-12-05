import socket
firewall_rules = {"allow": ["80", "443"], "block": ["8080"]}

def check_port(port):
    if port in firewall_rules['block']:
        return "Blocked"
    return "Allowed"

port = "8080"
print(f"Port {port} is {check_port(port)}")
