def mask_data(data, mask_char="*"):
    return f"{mask_char * 12}{data[-4:]}"

# Usage
credit_card = "4111111111111234"
masked_card = mask_data(credit_card)
print("Masked Credit Card:", masked_card)
