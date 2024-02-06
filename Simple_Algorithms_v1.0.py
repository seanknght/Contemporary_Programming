#SEAN KNIGHT 2304773
#JAN 31, 2024

from curses.ascii import isdigit
import pyfiglet

#DISPLAY ASCII BANNER ART AT THE START OF THE CODE.

ascii_banner = pyfiglet.figlet_format("SIMPLE ALGORITHMS")
print(ascii_banner)

#//////////////////////////SQUARE STARTS HERE//////////////////////////

def square():

    while True:

        side_length_str = input("Enter the side length of the square: ")

        if side_length_str.isdigit():

            side_length = float(side_length_str)
            break

        else:

            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
            print("Side length should be a positive number. Try again.")
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")

    #CALCULATE PERIMETER AND AREA OF SQUARE.            

    perimeter = 4 * side_length
    area = side_length ** 2

    print("////////////////////////////////////////////")
    print(f"        The perimeter is: ({perimeter})")
    print("////////////////////////////////////////////")
    print(f"        The area is: ({area})")
    print("////////////////////////////////////////////")

#YES OR NO LOOP TO ENTER ANOTHER SIDE LENGTH.

    while True:

        another_side_length = input("Would you like to enter another number for square? (y/n): ")
        
        if another_side_length.lower() != 'y':
            break
        else:
            square()
        
#/////////////////////////SQUARE ENDS HERE./////////////////////////

#/////////////////////////RECTANGLE STARTS HERE.////////////////////

def rectangle():

    while True:
        
        length_str = input("Enter the length of the rectangle: ")
        width_str = input("Enter the width of the rectangle: ")

        if length_str.isdigit() and width_str.isdigit():
           
            length = float(length_str)
            width = float(width_str)
            
            break
        else:
            
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
            print("Length and width should be positive numbers. Try again.")
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")


    #CALCULATE PERIMETER AND AREA OF THE RECTANGLE.

    perimeter = 2 * (length + width)
    area = length * width

    #PRINT THE PERIMETER AND AREA OF THE RECTANGLE

    print("////////////////////////////////////////////")
    print(f"        The perimeter is: ({perimeter})")
    print("////////////////////////////////////////////")
    print(f"        The area is:({area})")
    print("////////////////////////////////////////////")

    #YES OR NO LOOP TO ENTER ANOTHER LENGTH AND WIDTH.

    while True:

        another_length_and_Width = input("Would you like to enter another number for rectangle? (y/n): ")
        
        if another_length_and_Width.lower() != 'y':
            break
        else:
            rectangle()

#/////////////////////////RECTANGLE ENDS HERE./////////////////////////
            
#/////////////////////////AVERAGE STARTS HERE.////////////////////////

def calculate_average(grade1, grade2, grade3):
    total_grades = grade1 + grade2 + grade3
    average_grade = (total_grades / 3)
    return average_grade

def average():
    while True:
        try:
            # Input grades from the user
            print("////////////////////////////////////////////")
            grade1 = float(input("      Enter grade for course 1: "))
            print("////////////////////////////////////////////")
            grade2 = float(input("      Enter grade for course 2: "))
            print("////////////////////////////////////////////")
            grade3 = float(input("      Enter grade for course 3: "))
            
            # Calculate and display the average
            avg = calculate_average(grade1, grade2, grade3)

            print("////////////////////////////////////////////")
            print(f"        The average grade is: ({avg})")
            print("////////////////////////////////////////////")

            # Ask the user if they want to enter another set of grades

            another_set = input("Would you like to enter another set of grades? (y/n): ")

            if another_set.lower() != 'y':
                break  # Exit the loop if the user doesn't want to enter another set of grades

        except ValueError:
            print("Invalid input. Please enter numeric values.")


#//////////////////////////AVERAGE ENDS HERE./////////////////////////

if __name__ == '__main__':
    
    program_functions = {
        "1": square,
        "2": rectangle,
        "3": average,
    }

    while True:
        print("Select a program:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Average Grade of three (3) course grades")
        program_choice = input("Enter the program number (1 - 3): ")

        selected_program = program_functions.get(program_choice)
        if selected_program:
            selected_program()
        else:
            print("Invalid choice. Please enter 1 - 3.")

        another = input("Would you like to run another program? (y/n): ")
        print("/////////////////////////////////////////////////")
        if another.lower() != 'y':
            break
        
    
#TO DISPLAY AUTHOR ASCII NAME WHEN CODE IS STOPPED.    

ascii_banner = pyfiglet.figlet_format("Made by T3KK5")
print(ascii_banner)
    
