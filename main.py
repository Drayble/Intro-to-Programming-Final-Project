import os
import time

'''
Reference sheet for anyone that doesn't watch Scooby-Doo:
*Note the first letter similarities for simplicity

federick_jones - file handler
raggy - referencer
daphne_blake - directory handler

vault is the password manager
any file with the name "dir" is the menu for the user's planners
filenames should be in this format "user_id"-"planner name".txt
'''
# Global variables
total_users = 0
current_user = 0
current_password = ""


def main():
    try:
        frederick_jones = open("vault.txt")
        global total_users
        while True:
            x = frederick_jones.readline()
            if x != "":
                total_users += 1
            else:
                break
        total_users -= 1
        frederick_jones.close()
        print("Welcome back to the Quick Planner!\n")
        while True:
            while True:
                user_id = input("Please enter your user id: ")
                if user_id.isnumeric() and user_id.isdigit():
                    user_id = int(user_id)
                    if user_id > 0:
                        # checkpoint code
                        while True:
                            chkpt = input((str("Are you sure your user id is ") + str(user_id) + str(
                                "? Enter \"Y\" or \"N\" to continue: ")))
                            if chkpt.isalpha():
                                chkpt = chkpt.lower()
                                if chkpt == "y" or chkpt == "yes" or chkpt == "ye" or chkpt == "no" or chkpt == "n":
                                    # break for checkpoint
                                    break
                                else:
                                    print("That's not an actual response, try again.\n")
                            else:
                                print("That's not an actual response, try again.\n")
                        if chkpt == "y" or chkpt == "yes" or chkpt == "ye":
                            # end of checkpoint code
                            # external break for checkpoint
                            break
                        else:
                            print("\n")
                    else:
                        print("Invalid. Please Make sure your entry is a number greater than 0, and contains no "
                              "decimal points.\n")
                else:
                    print("Invalid. Please Make sure your entry is a number greater than 0, and contains no decimal "
                          "points.\n")
            if user_id > total_users:
                while True:
                    chkpt = input("It seems like you're trying to access an id that hasn't been created yet. Would "
                                  "you like to make a new one?\n")
                    if chkpt.isalpha():
                        chkpt = chkpt.lower()
                        if chkpt == "y" or chkpt == "yes" or chkpt == "ye" or chkpt == "no" or chkpt == "n":
                            # break for checkpoint
                            break
                        else:
                            print("That's not an actual response, try again.\n")
                    else:
                        print("That's not an actual response, try again.\n")
                if chkpt == "y" or chkpt == "yes" or chkpt == "ye":
                    new_user()
                    break
                else:
                    print("That id does not exist, please try again.\n")
            else:
                frederick_jones = open("vault.txt")
                for x in range(0, user_id):
                    raggy = frederick_jones.readline()
                raggy = frederick_jones.readline()
                frederick_jones.close()
                if raggy != "":
                    global current_user
                    current_user = user_id
                    global current_password
                    # this is necessary or else it keeps a new freakin line
                    raggy = raggy.rstrip()
                    raggy = raggy.lstrip()
                    current_password = raggy
                    break
                else:
                    print("That id does not exist, please try again.\n")

    except:
        frederick_jones = open("vault.txt", "x")
        frederick_jones.write("placeholder")
        frederick_jones.close()
        cs()
        print("It seems like this is a new device to the planner. One moment please.\n\n")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".\n\n")
        time.sleep(1)
        print("Thank you for waiting, the necessary files have been created. Welcome to the Quick Planner!\n")
        new_user()

    # after this point, password has been received
    attempts = 4
    while attempts > 0:
        guess = input(
            "Please enter the password for user " + str(current_user) + ".\nPlease note you currently have " + str(
                attempts) + " attempts left and running out of attempts will end the system, causing you to start over\n")
        if guess == current_password:
            break
        else:
            print("Incorrect password, attempt used.\n")
            attempts -= 1
    if attempts == 0:
        print("You've run out of attempts, the system will now close.")
        time.sleep(1)
        print("Goodbye.")
        exit()
    print("\nWelcome, user " + str(current_user) + ", with password \"" + str(current_password) + "\"")
    print_curr_dir()
    admin_command()
    print("aight, peace out")


def new_user():
    global total_users
    total_users += 1
    cs()
    print("Your user ID is now:", total_users)
    global current_user
    current_user = total_users
    print("Make sure you remember your id for future logins\n")
    time.sleep(2)
    while True:
        new_pass = input("\nTime to set your password. Please enter your desired password.\nThis cannot be changed "
                         "after it is set: ")
        if new_pass.isprintable():
            while True:
                chkpt = input("Your new password is currently: \"" + str(
                    new_pass) + "\"\nAre you sure you want it to be this? Please respond with Y or N.\n")
                if chkpt.isalpha():
                    chkpt = chkpt.lower()
                    if chkpt == "y" or chkpt == "yes" or chkpt == "ye" or chkpt == "no" or chkpt == "n":
                        # break for checkpoint
                        break
                    else:
                        print("That's not an actual response, try again.\n")
                else:
                    print("That's not an actual response, try again.\n")
            if chkpt == "y" or chkpt == "yes" or chkpt == "ye":
                global current_password
                current_password = new_pass
                print("Your password is now set to \"" + str(new_pass) + "\" and cannot be changed. Please remember "
                                                                         "it so that you may log\nback in at later "
                                                                         "points as needed.")
                daphne_blake = open(get_curr_dir(), "x")
                if total_users == 1:
                    print("Also, because you are the first user for this system, you get admin access to delete it "
                          "all!\n")
                    daphne_blake.write("admin command\n")
                daphne_blake.write("create new planner\n")
                daphne_blake.close()
                frederick_jones = open("vault.txt", "a")
                frederick_jones.write("\n" + new_pass)
                frederick_jones.close()
                break
        else:
            print("The password you entered contains illegal characters. Please try again\n")


def print_curr_dir():
    daphne_blake = open(get_curr_dir())
    count = 1
    for line in daphne_blake:
        line = line.lstrip()
        line = line.rstrip()
        print(str(count) + " - " + line)
        count += 1

def get_curr_dir():
    return str(current_user) + "directory.txt"


def admin_command():
    while True:
        chkpt = input("\nWanna wipe the system?\n")
        if chkpt.isalpha():
            chkpt = chkpt.lower()
            if chkpt == "y" or chkpt == "yes" or chkpt == "ye" or chkpt == "no" or chkpt == "n":
                # break for checkpoint
                break
            else:
                print("That's not an actual response, try again.\n")
        else:
            print("That's not an actual response, try again.\n")
    if chkpt == "y" or chkpt == "yes" or chkpt == "ye":
        for x in range(0, (total_users + 1)):
            global current_user
            current_user = x
            if os.path.exists(get_curr_dir()):
                os.remove(get_curr_dir())
        os.remove("vault.txt")
        print("Everything's deleted.")


def cs():
    for x in range(100):
        print("\n")


main()
