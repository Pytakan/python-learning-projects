users = [
    {"username": "admin",
     "password": "admin123",
     "role": "admin"},
    {"username": "user1", "password": "user123", "role": "user"},
    {"username": "guest", "password": "guest123", "role": "guest"},
]
def authenticate(username, password,**kwargs):
    for user in users:
        if user["username"] == username and user["password"] == password:
            return f"Welcome {username}! You are logged in as {user['role']}."
        #else:
            #raise ValueError("Invalid username or password.")
    raise ValueError("Invalid username or password.")

user1,user2,user3=users
try:
    print(authenticate(**user1))  # Should succeed
    print(authenticate(**user2))  # Should succeed
    print(authenticate("user1", "wrongpassword"))  # Should fail
except ValueError as e:
    print(f"Error: {e}")