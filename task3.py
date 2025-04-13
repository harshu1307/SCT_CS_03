import re

def check_password_strength(password):
    score = 0  # Fixed indentation

    # Check each criterion
    length_ok = len(password) >= 8
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Score based on criteria
    score += length_ok + has_lower + has_upper + has_digit + has_special

    print("\nPassword Strength Check:")
    print(f" - Length >= 8: {'Yes' if length_ok else 'No'}")
    print(f" - Lowercase: {'Yes' if has_lower else 'No'}")
    print(f" - Uppercase: {'Yes' if has_upper else 'No'}")
    print(f" - Digit: {'Yes' if has_digit else 'No'}")
    print(f" - Special Character: {'Yes' if has_special else 'No'}")

    strength = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak"
    }

    print(f"\nPassword Strength: {strength[score]}")

# Main program
if __name__ == "__main__":
    password = input("Enter your password: ")
    check_password_strength(password)