def role_based_masking(data, role):
    if role == "admin":
        return data  # Full access
    return f"**** **** **** {data[-4:]}"  # Masked for other roles

# Usage
credit_card = "4111111111111234"
print("Admin View:", role_based_masking(credit_card, "admin"))
print("CSR View:", role_based_masking(credit_card, "csr"))
