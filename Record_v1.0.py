#SEAN KNIGHT 
#2304773

import pyfiglet

ascii_banner = pyfiglet.figlet_format("Record")
print(ascii_banner)

def info():

    #PROMPT USER TO ENTER FIRST NAME

    while True:

        first_name_str = input("Enter First Name: ")

        if first_name_str.isdigit():

            print("First Name should not be a number. Try again")
        
        else:

            break

    #PROMPT USER TO ENTER LAST NAME

    while True:

        last_name_str = input("Enter Last Name: ")

        if last_name_str.isdigit():

            print("Last Name should not be a number. Try again")
        
        else:

            break

    #PROMPT USER TO ENTER AGE

    while True:

        age_int = input("Enter Age: ")

        if age_int.isdigit():
            break

        else:

            print("Age should be a number. Try again")

    #PROMPT USER TO ENTER OVERALL SCORE ON THE LATEST TEST
            
    while True:

        score =  input("Enter the overall score: ")
        
        if score.isdigit():

            score_str = float(score)
            break

        else:

            print("Overall Score should be a number. Try again")

    #CALCULATE OVRALL RESULTS
            
        overall_results = (score_str / 600) * 100
        print(overall_results)



if __name__ == '__main__':
    info()