#SEAN KNIGHT
#FFEB 13, 2024
#2304773

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Python Programming")
print(ascii_banner)

print("\nI am your Programmer Sean Knight.\n")

def print_options():

    while True:

        print("\nWhat shall I stream next?\n ")

        print("a) Days Gone")
        print("b) Resident Evil 2")
        print("c) Fortnite")
        print("d) Apex Legends")
        print("e) Death Stranding")
        print("f) Surprise Us!")

        def get_user_choice():

            while True:

                valid_choices = ['a', 'b', 'c', 'd', 'e', 'f']
                user_input = input("\nEnter your choice (a-f): ").lower()

                if user_input in valid_choices:

                    return user_input
                    
            
                else:

                    print("Invalid choice. Please select a valid option (a-f).")
        
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
        break 

#//////////////////////////////////////// CHOICE STARTS HERE ///////////////////////////////////////////

#//////////////////////////////////////// INFO STARTS HERE ///////////////////////////////////////////

def check_admission_eligibility(overall_score):
    return overall_score >= 60

def check_scholarship_eligibility(test_score):
    return test_score >= 80

def info():

    #PROMPT USER TO ENTER FIRST NAME

    while True:

        first_name_str = input("Enter First Name: ")
        
        if first_name_str.isdigit():

            print("//////////////////// ERROR //////////////////////")
            print("First Name should not be a number. Try again")
            print("//////////////////// ERROR //////////////////////")
        
        else:

            break

    #PROMPT USER TO ENTER LAST NAME    

    while True:

        print("/////////////////////////////////////////////////")
        last_name_str = input("Enter Last Name: ")

        if last_name_str.isdigit():
            
            print("//////////////////// ERROR //////////////////////")
            print("Last Name should not be a number. Try again")

        else:
        
            break

    #PROMPT USER TO ENTER AGE
                
    while True:
        
        print("/////////////////////////////////////////////////")
        age_int = input("Enter Age: ")
     
        if age_int.isdigit():
        
            break
        
        else:
        
            print("//////////////////// ERROR ////////////////////////")
            print("Age should be a number. Try again")

    while True:

        print("/////////////////////////////////////////////////")    
        score = input("Enter the overall score: ")
    

        if score.isdigit():
        
            score_str = float(score)
            break
        
        else:
        
            print("//////////////////// ERROR ////////////////////////")
            print("Overall Score should be a number. Try again")

    # Calculate overall results
    
    overall_results = (score_str / 600) * 100
    print("/////////////////////////////////////////////////")
    print(f"Overall Results: {overall_results}%")

    # Check Admission Eligibility
    
    if check_admission_eligibility(overall_results):
        
        print("/////////////////////////////////////////////////")
        print("Admission: Eligible")
    
    else:
        
        print("//////////////////////////////////////////////////////////////////////////")
        print("Admission: Not Eligible")
        print("//////////////////////////////////////////////////////////////////////////")
        
    # Check Scholarship Eligibility
    
    if check_scholarship_eligibility(overall_results):

        print("/////////////////////////////////////////////////")
        print("Scholarship: Eligible")
    
    else:
        
        print("/////////////////////////////////////////////////")
        print("Scholarship: Not Eligible")
        print("/////////////////////////////////////////////////")

#//////////////////////////////////////// INFO ENDS HERE ///////////////////////////////////////////

#//////////////////////////////////////// SCHOLARSHIP START HERE ///////////////////////////////////////////
        
def students_data():

    def check_admission_eligibility(overall_results):  # Fix: Use overall_results instead of student['overall_score']

        return overall_results >= 60

    def check_scholarship_eligibility(overall_results):  # Fix: Use overall_results instead of student['overall_score']

        return overall_results >= 80
     
    students_data = [

        {"first_name": "Student1", "age": 18, "overall_score": 471},
        {"first_name": "Student2", "age": 20, "overall_score": 354},
        {"first_name": "Student3", "age": 22, "overall_score": 502}
    ]

    for student in students_data:

        overall_results = (student['overall_score'] / 600) * 100

        print(f"\nStudent: {student['first_name']}")
        print(f"Age: {student['age']}")
        print(f"Overall Results: {overall_results}%")

        # Check Admission Eligibility

        if check_admission_eligibility(overall_results):  # Fix: Use overall_results instead of student['overall_score']

            print("Admission: Eligible")

        else:

            print("Admission: Not Eligible")

        # Check Scholarship Eligibility
            
        if check_scholarship_eligibility(overall_results):  # Fix: Use overall_results instead of student['overall_score']

            print("Scholarship: Eligible")

        else:

            print("Scholarship: Not Eligible")

#//////////////////////////////////////// SCHOLARSHIP ENDS HERE ///////////////////////////////////////////
            
#//////////////////////////////////////// PATTERNS STARTS HERE ///////////////////////////////////////////
            
def pattern():

    # Pattern 1
    for i in range(5):
        print('*' * (i + 1))

    print()  # Blank line separator

    # Pattern 2
    for i in range(5, 0, -1):
        print('*' * i)

    print()  # Blank line separator

    # Pattern 3
    for i in range(5):
        print(' ' * i + '*' * (5 - i))

    print()  # Blank line separator

    # Pattern 4
    for i in range(4, 0, -1):
        print(' ' * (5 - i) + '*' * i)

        
#//////////////////////////////////////// PATTERNS ENDS HERE ///////////////////////////////////////////
            
#//////////////////////////////////////// SERVICES STARTS HERE ///////////////////////////////////////////
            
def calculate_class_average():
    # Initialize an empty list to store grades
    
    grades = []

    # Input grades for ten students
    
    for i in range(1, 11):

        while True:

            try:
            
                grade = int(input(f"Enter the grade for student {i} (0-100): "))
                
                if 0 <= grade <= 100:
                
                    grades.append(grade)
                
                    break
                
                else:
                
                    print("Invalid input. Grade must be in the range 0-100.")
            
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

            # Calculate and return the class average
            class_average = sum(grades) / len(grades)
            return class_average

        # Call the function and print the result
        average_result = calculate_class_average()
        print(f"\nThe class average on the quiz is: {average_result:.2f}")

#//////////////////////////////////////// SERVICES ENDS HERE ///////////////////////////////////////////
        
def dental_services_menu():

    services = {
        'a': {'name': 'Root Canal Therapy', 'cost': 250},
        'b': {'name': 'Oral Hygiene Check', 'cost': 50},
        'c': {'name': 'Emergency Injury Treatment', 'cost': 100},
        'd': {'name': 'Post-Procedure Check-up', 'cost': 150},
        'e': {'name': 'Routine Check-ups and Consultation', 'cost': 75}
    }
    return services

def display_services(services):
    
    print("\nDental Services:")
    for key, value in services.items():
        print(f"{key}) {value['name']} - ${value['cost']}")

def calculate_total(selected_services, services, advanced_payment):
    
    total = 0
    for service_key in selected_services:
        service = services[service_key]
        total += service['cost']

    if advanced_payment:
        total *= 0.5  # 50% discount for advanced payments

    return total

def main():
    services = dental_services_menu()
    selected_services = []

    while True:
        display_services(services)

        user_choice = input("\nEnter the letter(s) corresponding to the service(s) you want (press 'q' to quit): ").lower()

        if user_choice == 'q':
            break

        for choice in user_choice:
            if choice in services:
                selected_services.append(choice)
            else:
                print(f"Invalid choice: {choice}. Please choose a valid option.")

    advanced_payment = input("Would you like to make an advanced payment? (y/n): ").lower() == 'y'

    total_amount = calculate_total(selected_services, services, advanced_payment)

    print(f"\nSelected Services:")
    for service_key in selected_services:
        service = services[service_key]
        print(f"{service['name']} - ${service['cost']}")

    print(f"\nTotal Amount Payable: ${total_amount:.2f}")


if __name__ == '__main__':
    program_function = {

        "1": print_options,
        "2": info,
        "3": students_data,
        "4": pattern,
        "5": calculate_class_average,
        "6": main,
    }
    
    while True:

        print("Select a program:")
        print()
        print("1. Choice")
        print("2. info")
        print("3. Students data")
        print("4. Patterns")
        print("5. Class Average")
        print("5. Dentist")
        print()
        
        #PROMPT USER TO ENTER PROGRAM NUMBER

        program_choice = input("Enter the program number (1 - 6): ")
        print("/////////////////////////////////////////////////")

        selected_program = program_function.get(program_choice)

        if selected_program:

            selected_program()
        
        else:
            print("Invalid choice. Please Enter (1 - 6).")

        #YES OR NO ANOTHER PROGRAM LOOP
        
        print("/////////////////////////////////////////////////")    
        another = input("Would you like to run another program? (y/n): ")
        print("//////////////////////////////////////////////////////////////////////////")

        if another.lower() != 'y':

            break

#TO DISPLAY AUTHOR ASCII NAME

ascii_banner = pyfiglet.figlet_format("Made by T3KK5")
print(ascii_banner)