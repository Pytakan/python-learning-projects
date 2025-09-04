import random
def is_auth():
    return random.choice([True, False])

def chack_user_auth(func):
    def wrapper(*args, **kwargs):
        if is_auth():
            return func(*args, **kwargs)
        else:
            raise Exception("User is not authenticated") 
    return wrapper

@chack_user_auth
def view_profile(user_id):
    return f"User profile of {user_id}"

try:
    print(view_profile(42)) # May print profile or raise exception
except Exception as e:
    print(e)
