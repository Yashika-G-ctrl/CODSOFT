#!/usr/bin/env python3
"""
password_generator.py – CLI strong password maker
"""

import secrets
import string

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Please enter a positive integer.")

def build_charset():
    charset = string.ascii_lowercase
    if input("Include UPPERCASE letters? (y/n): ").lower().startswith("y"):
        charset += string.ascii_uppercase
    if input("Include DIGITS? (y/n): ").lower().startswith("y"):
        charset += string.digits
    if input("Include SYMBOLS? (y/n): ").lower().startswith("y"):
        charset += string.punctuation
    if len(charset) < 2:
        print("You disabled everything! Using lowercase only.")
        charset = string.ascii_lowercase
    return charset

def generate_password(length, charset):
    # Ensure at least one of each enabled category is present
    password = []
    if string.ascii_lowercase in charset:
        password.append(secrets.choice(string.ascii_lowercase))
    if string.ascii_uppercase in charset and any(c in charset for c in string.ascii_uppercase):
        password.append(secrets.choice(string.ascii_uppercase))
    if string.digits in charset and any(c in charset for c in string.digits):
        password.append(secrets.choice(string.digits))
    if string.punctuation in charset and any(c in charset for c in string.punctuation):
        password.append(secrets.choice(string.punctuation))

    # Fill the rest of the password
    while len(password) < length:
        password.append(secrets.choice(charset))

    # Shuffle to avoid predictable pattern
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    print("=== Strong Password Generator ===")
    length = get_positive_int("Desired length: ")
    charset = build_charset()
    pwd = generate_password(length, charset)
    print("\nGenerated password:", pwd)

if __name__ == "__main__":
    main()