import random

UPPERCASE = "QWERTYUIOPASDFGHJKLZXCVBNM"
LOWERCASE = "qwertyuiopasdfghjklzxcvbnm"
NUMS = "1234567890"
SPECIAL = "!@#$%^&*()-_~+=[]?:;,.<>`"

def get_validate_pass_len():
    while True:
        try:
            pass_len = int(input("Enter the length of the password (1-50): "))
            if 0 < pass_len <= 50:
                return pass_len
            else:
                print("Invalid input. Please enter a positive integer between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a positive integer between 1 and 50.")

def get_pass_contents():
    use_upper_case = get_yes_or_no_input("Include uppercase? (Y/N): ")
    use_lower_case = get_yes_or_no_input("Include lowercase? (Y/N): ")
    use_nums = get_yes_or_no_input("Include numbers? (Y/N): ")
    use_special_chars = get_yes_or_no_input("Include special characters? (Y/N): ")
    
    while not any([use_upper_case, use_lower_case, use_nums, use_special_chars]):
        print("Please select at least one option.\n")
        use_upper_case = get_yes_or_no_input("Include uppercase? (Y/N): ")
        use_lower_case = get_yes_or_no_input("Include lowercase? (Y/N): ")
        use_nums = get_yes_or_no_input("Include numbers? (Y/N): ")
        use_special_chars = get_yes_or_no_input("Include special characters? (Y/N): ")
    
    return use_upper_case, use_lower_case, use_nums, use_special_chars

def get_yes_or_no_input(message):
    while True:
        user_input = input(message).upper()
        if user_input == "Y":
            return True
        elif user_input == "N":
            return False
        else:
            print("Please enter Y or N.")

def generate_pass(pass_len, use_upper_case, use_lower_case, use_nums, use_special_chars):
    chars = []
    if use_upper_case:
        chars.extend(UPPERCASE)
    if use_lower_case:
        chars.extend(LOWERCASE)
    if use_nums:
        chars.extend(NUMS)
    if use_special_chars:
        chars.extend(SPECIAL)
    
    generated_pass = ""
    for _ in range(pass_len):
        generated_pass += random.choice(chars)

    return generated_pass

pass_len = get_validate_pass_len()
use_upper_case, use_lower_case, use_nums, use_special_chars = get_pass_contents()
generated_pass = generate_pass(pass_len, use_upper_case, use_lower_case, use_nums, use_special_chars)
print("Your password is:", generated_pass)
