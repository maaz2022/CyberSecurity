def check_admin(user_role):
    if user_role != "admin":
        return "Access Denied"
    return "Access Granted"

print(check_admin("user"))  # Simulated authorization check
