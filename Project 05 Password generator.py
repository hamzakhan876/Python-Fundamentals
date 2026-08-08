import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

print("\nChoose complexity:")
print("1. Letters only")
print("2. Letters + numbers")
print("3. Letters + numbers + symbols")

choice = input("Enter choice: ")

if choice == "1":
    characters = string.ascii_letters

elif choice == "2":
    characters = string.ascii_letters + string.digits

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

else:
    print("Invalid choice")
    exit()

password = ""

for i in range(length):
    password += random.choice(characters)

if length < 8:
    strength = "Weak"

elif length < 12:
    strength = "Medium"

else:
    strength = "Strong"

print("\nGenerated Password:", password)
print("Strength:", strength)