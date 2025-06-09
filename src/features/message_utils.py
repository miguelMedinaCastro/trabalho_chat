from ..lib import os

users = {}

def create_user(user_name: str):
    if user_name not in users:    
        print("you dont have a account, create one")
        password = input("your new password: ")
        users[user_name] = password
        os.system('clear')
    authentication = input("type your password: ")
    if users.get(user_name) == authentication:
        print("welcome")
        