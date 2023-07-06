# User data stored in a dictionary (can be replaced with a database)
users = {
    "john@example.com": {
        "first_name": "John",
        "last_name": "Doe",
        "password": "password123"
    },
    "jane@example.com": {
        "first_name": "Jane",
        "last_name": "Smith",
        "password": "password456"
    }
}

def signup():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

    if password != confirm_password:
        print("Passwords do not match.")
        return

    if email in users:
        print("User already exists. Please log in.")
        return

    # Store user data in the dictionary (or save to a database)
    users[email] = {
        "first_name": first_name,
        "last_name": last_name,
        "password": password
    }
    print("Sign up successful!")

def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if email not in users or users[email]["password"] != password:
        print("Invalid email or password.")
        return

    print("Login successful!")
    # Perform actions after successful login

def signout():
    print("Signed out successfully!")

# Main program loop
while True:
    print("\n--- User Authentication System ---")
    print("1. Sign up")
    print("2. Log in")
    print("3. Sign out")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        signout()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please try again.")
