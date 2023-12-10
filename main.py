import os
import time

'''
Reference sheet for anyone that doesn't watch Scooby-Doo:
*Note the first letter similarities for simplicity

federick_jones - file handler
raggy - referencer
daphne_blake - directory handler
velma_dinkly - decision handler

vault is the password manager
any file with the name "dir" is the menu for the user's planners
filenames should be in this format "user_id"-"planner name".txt
'''
# Global variables
total_users = 0
current_user = 0
current_password = ""
current_dir_len = 0


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
                    raggy = truncate(raggy)
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
    # logged in at this point
    set_curr_dir_len(get_curr_dir())
    cs()
    cs()
    print_curr_dir()
    print("Alrighty, bye for now! :D")


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
                                                                         "points as needed.\n")
                daphne_blake = open(get_curr_dir(), "x")
                if total_users == 1:
                    print("Also, because you are the first user for this system, you get admin access to delete it "
                          "all!\n")
                    daphne_blake.write("Admin command\n")
                daphne_blake.write("Create new planner\n")
                daphne_blake.close()
                frederick_jones = open("vault.txt", "a")
                frederick_jones.write("\n" + new_pass)
                frederick_jones.close()
                break
        else:
            print("The password you entered contains illegal characters. Please try again\n")


def run_choice(choice: int):
    daphne_blake = open(get_curr_dir())
    for x in range(0, choice - 1):
        daphne_blake.readline()
    velma_dinkley = daphne_blake.readline()
    daphne_blake.close()
    velma_dinkley = truncate(velma_dinkley)
    if velma_dinkley == "Admin command":
        admin_command()
    elif velma_dinkley == "Create new planner":
        create_routine()
    else:
        run_routine(velma_dinkley)
    '''
    After getting the choice, from here, execute either admin command, create routine, or run routine
    '''


def create_routine():
    while True:
        routine_name = input("\nPlease enter the name you'd like for this routine: ")
        if routine_name.isprintable():
            while True:
                chkpt = input("Your new routine is currently named: \"" + str(
                    routine_name) + "\"\nAre you sure you want it to be this? Please respond with Y or N.\n")
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
                print("Your routine is now named \"" + str(routine_name) + "\" and cannot be changed.\n")
                count = 1
                while True:
                    filename = str(current_user) + str(routine_name) + str(count) + ".txt"
                    try:
                        velma_dinkly = open(filename, "x")
                        break
                    except:
                        count += 1
                velma_dinkly.close()
                daphne_blake = open(get_curr_dir(), "a")
                daphne_blake.write((routine_name + str(count)) + "\n")
                daphne_blake.close()
                break
        else:
            print("The password you entered contains illegal characters. Please try again\n")
    print("You may now enter what you'd like this routine to say.")
    print("To enter text, just type away and press enter when you want to go to the next line.")
    print("There is no deleting lines so type carefully. <3")
    print("Simply type \"stop\" to finish your writing.")
    print("Enjoy!")
    time.sleep(2)
    print("\n\n")
    velma_dinkly = open(filename, "a")
    while True:
        user_feed = input("")
        checker = user_feed.lower()
        if checker != "stop" and checker.isprintable():
            velma_dinkly.write(user_feed + "\n")
        else:
            break
    velma_dinkly.close()
    print("\nWriting for routine is finished")

def run_routine(filename):
    # if ... contains "routine" then pass it here
    print("Running routine \"" + str(filename) + "\":\n")
    full_file_name = str(current_user) + filename + ".txt"
    scooby_doo = open(full_file_name)
    for line in scooby_doo:
        line = truncate(line)
        print(" - " + line)
        time.sleep(0.75)
    scooby_doo.close()
    print("\n\n\n")


def get_dir_choice():
    while True:
        choice = input("\nPlease enter the number for the task you'd like to do: ")
        if choice.isnumeric() and choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= current_dir_len:
                break
            else:
                print("Please enter a number that is available.\n")
        else:
            print("Please enter a number that is available.\n")
    run_choice(choice)


def print_curr_dir():
    daphne_blake = open(get_curr_dir())
    count = 1
    print("Options:")
    for line in daphne_blake:
        line = truncate(line)
        print(str(count) + " - " + line)
        count += 1
    daphne_blake.close()
    get_dir_choice()


def get_curr_dir():
    return str(current_user) + "directory.txt"


def set_curr_dir_len(input):
    frederick_jones = open(input)
    count = 0
    for line in frederick_jones:
        count += 1
    global current_dir_len
    current_dir_len = count
    frederick_jones.close()


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
        for x in range(1, (total_users + 1)):
            global current_user
            current_user = x
            set_curr_dir_len(get_curr_dir())
            daphne_blake = open(get_curr_dir())
            for y in range(0, current_dir_len + 1):
                temp_holder = str(current_user) + truncate(daphne_blake.readline()) + ".txt"
                if os.path.exists(temp_holder):
                    os.remove(temp_holder)
            daphne_blake.close()
            if os.path.exists(get_curr_dir()):
                os.remove(get_curr_dir())
        os.remove("vault.txt")
        print("Everything's deleted.")


def truncate(snip):
    snip = snip.lstrip()
    snip = snip.rstrip()
    return snip


def cs():
    for x in range(100):
        print("\n")


main()
