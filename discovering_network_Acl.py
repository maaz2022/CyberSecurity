acl_rules = {"allow": ["192.168.1.1"], "deny": ["10.0.0.1"]}

def check_ip(ip):
    if ip in acl_rules['deny']:
        return "Blocked"
    return "Allowed"

print(check_ip("10.0.0.1"))
