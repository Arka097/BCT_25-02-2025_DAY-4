from prettytable import PrettyTable

users = []  # Step 1: Empty list to store user data

def sign_up():
    user = {}  # Step 2: Dictionary for user data
    user["name"] = input("Enter Name: ")
    user["email"] = input("Enter Email: ")
    user["password"] = input("Enter Password: ")
    users.append(user)  # Step 4: Save user data
    print("Sign-up successful!\n")

def login():
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    
    for user in users:  # Step 5: Check login credentials
        if user["email"] == email and user["password"] == password:
            print("Login successful!\n")
            return
    print("Login failed! Incorrect email or password.\n")

def show_users():
    if not users:
        print("No users available.\n")
        return

    table = PrettyTable(["Name", "Email"])  # Step 6: Display in table format
    for user in users:
        table.add_row([user["name"], user["email"]])
    
    print("\nRegistered Users:")
    print(table)

def delete_user():
    email = input("Enter Email to delete: ")
    
    for user in users:  # Step 7: Delete user
        if user["email"] == email:
            users.remove(user)
            print("User deleted.\n")
            return
    print("User not found.\n")

while True:
    print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    elif choice == "3":
        show_users()
    elif choice == "4":
        delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
