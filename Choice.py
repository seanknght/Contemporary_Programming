#SEAN KNIGHT
#2304773
#FEB 7, 2024

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Choice")
print(ascii_banner)
def print_options():

    print("\nWhat shall I stream next?\n ")

    print("a) Days Gone")
    print("b) Resident Evil 2")
    print("c) Fortnite")
    print("d) Apex Legends")
    print("e) Death Stranding")
    print("f) Surprise Us!")

def get_user_choice():
    valid_choices = ['a', 'b', 'c', 'd', 'e', 'f']

    while True:
        user_input = input("\nEnter your choice (a-f): ").lower()

        if user_input in valid_choices:
            return user_input
        else:
            print("Invalid choice. Please select a valid option (a-f).")


if __name__ == '__main__':
    print_options()
    user_choice = get_user_choice()

    options_dict = {
        'a': 'Days Gone',
        'b': 'Resident Evil 2',
        'c': 'Fortnite',
        'd': 'Apex Legends',
        'e': 'Death Stranding',
        'f': 'Surprise Us!'
    }

    selected_option = options_dict.get(user_choice, 'Unknown Option')

    print(f"\nYou have chosen {selected_option}.\n")
    print("I appreciate your time and hope to see you in the next one!")
