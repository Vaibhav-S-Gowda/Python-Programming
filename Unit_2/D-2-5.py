# A password class uses a static method to check strength rules. 
# You must test five passwords and classify each result.

class Password:
    min_length = 8
    
    @staticmethod
    def check_strength(password: str) -> str:
        '''Assesses the strength of a given password using simple checks'''
        # Initialize flags for the rules
        is_long_enough = False
        has_uppercase = False
        has_lowercase = False
        has_digit = False
        has_special = False
        
        if len(password) >=Password.min_length:
            is_long_enough = True
            
        for char in password:
            if 'A' <= char <= 'Z':
                has_uppercase = True
            elif 'a' <= char <= 'z':
                has_lowercase = True
            elif '0' <= char <= '9':
                has_digit = True
            elif char in "!@#$%^&*()_-=+[]{}|/<>,.:;?":
                has_special = True
                
        # List all rules and count how many were met
        rules_met = [
            is_long_enough,
            has_uppercase,
            has_lowercase,
            has_digit,
            has_special
        ]
        
        score = sum(rules_met)
        
        # Classify the password based on the score
        if score >= 4:
            classification = "Strong"
        elif score >= 2:
            classification = "Moderate"
        else:
            classification = "Weak"
            
        print('-' * 50)
        print(f"password: {password}")
        print(f"Score: {score}/5 | Classification: {classification}")
        print(f"  - Long Enough({Password.min_length}+): {'Yes' if is_long_enough else 'no'}")
        print(f"  - Contains Uppercase:{'Yes' if has_uppercase else 'no'}")
        print(f"  - Contains Lowercase:{'Yes' if has_lowercase else 'no'}")
        print(f"  - Contains Digit:{'Yes' if has_digit else 'no'}")
        print(f"  - Contains Special Char:{'Yes' if has_special else 'no'}")
        
test_passwords = [
    "SecureP@ss1",
    "mypass",
    "AdminPassword",
    "user12345",
    "Go!Go!2025",
]
        
print("---Password Strength Test Results ---")

for password in test_passwords:
    Password.check_strength(password)
        