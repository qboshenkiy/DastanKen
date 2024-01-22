# user_app/main.py
from user_app.user import User

users = []

def add_user(username, email):
    new_user = User(username, email)
    users.append(new_user)
    print(f"User {username} added successfully!")

def list_users():
    if users:
        print("List of Users:")
        for user in users:
            print(f"Username: {user.username}, Email: {user.email}")
    else:
        print("No users found.")

def find_user(username):
    for user in users:
        if user.username == username:
            print(f"User found - Username: {user.username}, Email: {user.email}")
            return
    print(f"No user found with the username: {username}")

if __name__ == "__main__":
    add_user("john_doe", "john@example.com")
    add_user("jane_doe", "jane@example.com")

    list_users()

    find_user("john_doe")
    find_user("unknown_user")
