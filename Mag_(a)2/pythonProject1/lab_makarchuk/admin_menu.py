from main_menu import data
import json
def admin_menu():
    while True:
        print("Admin menu is successfully started!")
        print("For admin commands checks please type '!help'")
        admin_input = input('Choose what you want to do: ')
        match admin_input:
            case "delete":
                delete_user_input = input('Which user do you want to delete from users? (Enter name): ')
                users = data.get('users', [])
                new_users = [user for user in users if user['username'] != delete_user_input]
                data['users'] = new_users
                with open('user_data.json', 'w') as json_file:
                    json.dump(data, json_file, indent=4)
            case "delete all":
                delete_all_user_input = input("You will wipe all users' accounts, are you sure? ")
                for data_user in data["users"]:
                    updated_data = {}
                    for key, value in data_user.items():
                        if key != delete_all_user_input:
                            updated_data.update({key : value})
                            removed_value = value
                            print(f"User {removed_value} is successfully deleted.")
                        else:
                            print("Error")
                with open('user_data.json', 'w') as json_file:
                    json.dump(updated_data, json_file, indent=4)
            case "help":
                print("In this block you can watch your commands, now available: !help, !delete, !delete all for return to menu write 'R'")
                print("for back to register choose command !unlogin")
            case "exit":
                print("Close the program.")
                break
            case "unlogin":
                pass