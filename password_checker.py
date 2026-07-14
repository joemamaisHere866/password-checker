"""
Password Strength Checker
"""

import re
import sys

class PasswordChecker:
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "password123", "admin", 
            "letmein", "qwerty", "abc123", "monkey",
            "dragon", "master", "hello", "fuckyou"
        ]
    
    def check_length(self, password):
        length = len(password)
        if length < 8:
            return 0, "Too short (minimum 8 characters)"
        elif length < 12:
            return 1, "Good length"
        else:
            return 2, "Excellent length"
    
    def check_uppercase(self, password):
        if any(c.isupper() for c in password):
            return 1, "Has uppercase letters"
        else:
            return 0, "Missing uppercase letters"
    
    def check_lowercase(self, password):
        if any(c.islower() for c in password):
            return 1, "Has lowercase letters"
        else:
            return 0, "Missing lowercase letters"
    
    def check_digits(self, password):
        if any(c.isdigit() for c in password):
            return 1, "Has numbers"
        else:
            return 0, "Missing numbers"
    
    def check_special_characters(self, password):
        special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        if any(c in special_chars for c in password):
            return 1, "Has special characters"
        else:
            return 0, "Missing special characters"
    
    def check_common_password(self, password):
        if password.lower() in self.common_passwords:
            return 0, "Common password - easily guessable!"
        else:
            return 1, "Not a common password"
    
    def check_password(self, password):
        results = {
            'length': self.check_length(password),
            'uppercase': self.check_uppercase(password),
            'lowercase': self.check_lowercase(password),
            'digits': self.check_digits(password),
            'special': self.check_special_characters(password),
            'common': self.check_common_password(password)
        }
        
        total_score = sum(result[0] for result in results.values())
        
        if total_score <= 3:
            strength = "WEAK 🔴"
            color = "red"
            emoji = "🔴"
        elif total_score <= 5:
            strength = "MEDIUM 🟡"
            color = "yellow"
            emoji = "🟡"
        else:
            strength = "STRONG 🟢"
            color = "green"
            emoji = "🟢"
        
        return results, total_score, strength
    
    def display_results(self, password):
        print("\n" + "="*50)
        print("PASSWORD STRENGTH CHECKER")
        print("="*50)
        print(f"Password: {'*' * len(password)}")
        print("-"*50)
        
        results, score, strength = self.check_password(password)
        
        for check, (passed, message) in results.items():
            status = "✅" if passed > 0 else "❌"
            print(f"{status} {message}")
        
        print("-"*50)
        print(f"Score: {score}/8")
        print(f"Strength: {strength}")
        print("="*50)
        
        if score < 6:
            print("\n💡 Suggestions to improve your password:")
            for check, (passed, message) in results.items():
                if passed == 0:
                    if "length" in check:
                        print("  - Use at least 12 characters")
                    elif "uppercase" in check:
                        print("  - Add uppercase letters (A-Z)")
                    elif "lowercase" in check:
                        print("  - Add lowercase letters (a-z)")
                    elif "digits" in check:
                        print("  - Add numbers (0-9)")
                    elif "special" in check:
                        print("  - Add special characters (!@#$%^&*)")
                    elif "common" in check:
                        print("  - Avoid common passwords")
        else:
            print("\n🎉 Your password is strong!")
        
        return results

def main():
    print("🔐 Welcome to Password Strength Checker 🔐")
    print("Press Ctrl+C to exit\n")
    
    checker = PasswordChecker()
    
    while True:
        try:
            password = input("Enter a password to check: ")
            if password:
                checker.display_results(password)
                print("\n" + "-"*50)
        except KeyboardInterrupt:
            print("\n\nGoodbye! 👋")
            sys.exit(0)
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()