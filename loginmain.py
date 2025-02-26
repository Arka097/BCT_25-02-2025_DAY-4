import login_manage as um  # alias of login_manage

while True:
    print("\n1. Sign Up\n2. Login\n3. Show Users\n4. Delete User\n5. Exit")
    choice = input("Enter choice: ")
    
    if choice == "1":
        um.sign_up()
    elif choice == "2":
        um.login()
    elif choice == "3":
        um.show_users()
    elif choice == "4":
        um.delete_user()
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice! Try again.\n")
