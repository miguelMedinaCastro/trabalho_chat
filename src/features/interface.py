from ..lib import sys
from .util import create_group, enter_group, list_groups

def interface(client, user_name):
    while True:
        print("--- Main Menu ---")
        print("1. Create Group")
        print("2. Enter a group")
        print("3. List Groups")
        print("4. Enter. Log out")

        response = int(input("Choose: "))
        
        match response:
            case 1:
                create_group(client)
            case 2:
                enter_group(client, user_name)
            case 3:
                list_groups(client)
            case 4:
                sys.exit("see you next time :)")

    