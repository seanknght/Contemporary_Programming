#SEAN KNIGHT
#2304773
#FEB 20. 2024

from pyfiglet import Figlet
from colorama import init, Fore
import sys

#//////////////////////////////////////////////////////////////////////////////////////////////

#DISPLAY ASCII BANNER

init(autoreset=True)

def print_colored_banner(text, color):
    colored_text = f"{color}{text}"
    print(colored_text)

fig = Figlet()

banner_text = fig.renderText("Temperature Conversion")
print_colored_banner(banner_text, Fore.RED,)

#////////////////////////////////////////////////////////////////////////////////////////////

#DISPLAY WELCOME

print(f"{Fore.RED}\n[+] Welcome to the Temperature Conversion Program!\n")

#/////////////////////////// CELSIUS TO FAHRENHEIT STARTS HERE /////////////////////////////

def celsius_fahrenheit():

    while True:

        #PROMPT USER FOR TEMPERATURE TO BE CONVERTED

        print()
        Celsius = input("Enter Temperature in Celsius: ")

        #FORMULA TO CONVERT

        C = int(Celsius)
        Fahrenheit = 32 + (C * 1.8)
        print(f"\n{Celsius} C to Fahrengeir is: {Fahrenheit} F\n")
        break

#///////////////////////////// CELSIUS TO FAHRENHEIT ENDS HERE /////////////////////////////
        
#//////////////////////////// FAHRENHEIT TO CELSIUS STARTS HERE /////////////////////////////
        
def fahrenheit_celsius():

    while True:

        #PROMPT USER FOR TEMPERATURE TO BE CONVERTED

        print()
        Fahrenheit = input("Enter Temperature in Fahrenheit: ")
        
        #FORMULA TO CONVERT

        F = int(Fahrenheit)
        Celsius = 5 / 9 * (F - 32)
        print(f"\n{Fahrenheit} F to Celsius is: {Celsius} C\n")
        break

#//////////////////////////// FAHRENHEIT TO CELSIUS ENDS HERE /////////////////////////////
        
def exit():

    print("Exiting....")
    sys.exit()


if __name__ == '__main__':

    program_function = {

        "c": celsius_fahrenheit,
        "f": fahrenheit_celsius,
        "x": exit,
    }
    
    while True:

        init(autoreset=True)

        print(f"{Fore.RED}[+] Select a program:")
        print()
        print(f"{Fore.GREEN}[C] Celsius to Fahrenheit")
        print(f"{Fore.YELLOW}[F] Fahrenheit to Celsius")
        print(f"{Fore.RED}[X] Exit",)
        print()

        #PROMPT USER TO ENTER PROGRAM NUMBER

        program_choice = input(f"{Fore.RED}[+] Enter your choice: ")
        print()
        print(f"{Fore.RED}/////////////////////////////////////////////////")

        selected_program = program_function.get(program_choice)

        if selected_program:

            selected_program()

        else:

            print("Error. Please enter a valid choice.")

        #YES OR NO ANOTHER PROGRAM LOOP
        
        print(f"{Fore.RED}//////////////////////////////////////////////////////////")    
        print()
        another = input(f"{Fore.RED}[+] Would you like to run another program again? (y/n): ")
        print()
        print(f"{Fore.RED}//////////////////////////////////////////////////////////")
        print()

        if another.lower() != 'y':

            break
