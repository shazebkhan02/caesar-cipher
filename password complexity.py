import re

def assess_password_strength(password):
    # Initialize score and feedback
    score = 0
    feedback = []

    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[\W_]', password))

    # Evaluate password based on the criteria
    if length_criteria:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if uppercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")

    if lowercase_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")

    if number_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one number.")

    if special_criteria:
        score += 1
    else:
        feedback.append("Password should include at least one special character (e.g., !, @, #, etc.).")

    # Determine password strength based on score
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Moderate",
        2: "Weak",
        1: "Very Weak",
        0: "Extremely Weak",
    }
    
    strength = strength_levels.get(score, "Unknown")

    # Display feedback to the user
    print(f"Password Strength: {strength}")
    if feedback:
        print("\nFeedback to Improve Your Password:")
        for suggestion in feedback:
            print(f"- {suggestion}")

def main():
    # Get user input
    password = input("Enter a password to assess its strength: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()
