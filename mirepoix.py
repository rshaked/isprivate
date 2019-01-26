""" Takes user input and prints results """

import getpass
from apscheduler.schedulers.background import BackgroundScheduler
import boiling
import consomme

def bool_to_private_text(private_bool):
    """ If is_name_private returns false, return 'public', if true return 'public' """
    if private_bool:
        return "Private"
    return "Public"

def check_insta(list_current_state, username, email, password):
    """ Checks current is_private against old is_private """
    try:
        new_state = boiling.is_name_private(username[0])
        if new_state != list_current_state[0]:
            list_current_state[0] = new_state
            consomme.send_email(bool_to_private_text(new_state), email, password)
            print("State is now: " + bool_to_private_text(new_state))
        else:
            print("No change. Checking again in <interval>.")

    except TypeError:
        print("Check if a valid instagram username was used.")


def start_checks():
    """ Initializes and runs advanced scheduler """
    username = [input("Input a valid instagram username: ")]
    intervallength = input("Interval length (in minutes) between checks: ")
    email = input("Input gmail: ")
    password = getpass.getpass()
    list_current_state = [boiling.is_name_private(username[0])]

    kwargs = {'username': username,
              'list_current_state': list_current_state,
              'email': email,
              'password': password}
    sched = BackgroundScheduler()
    sched.start()
    print("Checks have begun. \nPress ENTER to stop script. ")
    print("State is initially: " + bool_to_private_text(list_current_state[0]))
    check_insta(list_current_state, username, email, password)
    sched.add_job(check_insta, 'interval', minutes=int(intervallength), kwargs=kwargs)
    #sched.print_jobs()
    line = input()
    while line:
        if line == "state":
            print("\t" + bool_to_private_text(list_current_state[0]))
        if line == "username":
            print("\t" + username)
        line = input()


# print(boiling.is_name_private('thechristinap'))
start_checks()
