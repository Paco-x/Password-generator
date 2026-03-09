import secrets


length = int(input("Length_of_the_password: "))
count = int(input("How many passwords: "))

if count <= 0:
    print("Enter a positive number")
elif length <= 0:
    print("Length must be a positive number")
else:
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_characters = "!@#$%^&*()"
    all_characters = lowercase + uppercase + digits + special_characters

    for i in range(count):
        password = "".join(secrets.choice(all_characters) for _ in range(length))
        print(f"Generated Password {i + 1}: {password}")