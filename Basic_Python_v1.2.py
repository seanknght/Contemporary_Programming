# Sean Knight 2304773 (Contemporary Programing) Wednesday 11am, January 24, 2024.

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#////////////////////////////////////////PRINT_HI STARTS HERE.//////////////////////////////////////////////

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

#////////////////////////////////////////PRINT_HI ENDS HERE.//////////////////////////////////////////////

#///////////////////////////////////////GVNMAN STARTS HERE.///////////////////////////////////////////////

def gvnman():

    amt_Tend = 1000
    gct = 0.15


    while True:

        print("/////////////////////////////////////////////")
        itemName = input("Enter item name: ")

        if itemName.isdigit():

            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
            print("Item Name should not be a number. Try again.")
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")

        else:

            break
        
    while True:

        print("/////////////////////////////////////////////")
        item_Price_str = input("Enter item price: ")
    
        if item_Price_str.isdigit():

            item_Price = float(item_Price_str)
            break

        else:

            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
            print("Item Price should be a number. Try again.")
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
    

    amt_Tend = 1000
    gct = 0.15

    total_Due = item_Price + gct * item_Price
    
    change = amt_Tend - total_Due

    if item_Price > amt_Tend:

        print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
        print("Amount Tendered is $1000")
        print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")

    else:

        print("/////////////////////////////////////////////////////////////////")
        print("(Item Name)",itemName,"(Total After Tax)", total_Due, "(Change)", change)
        print("/////////////////////////////////////////////////////////////////")

    while True:

        another_itemName = input("Would you like to enter another item? (y/n)  ")

        if another_itemName.lower() != 'y':
            break
        
        gvnman()

#///////////////////////////////////////GVNMAN ENDS HERE.///////////////////////////////////////////////

#///////////////////////////////////////CALC STARTS HERE.//////////////////////////////////////////////
        
def calc():

    #Prompt user to enter a number.
    
    while True:
    
        print("////////////////////////////////////////////")
        num = input("Enter a number: ")

        if num.isdigit():

            num = float(num)
            break

        else:

            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")
            print("Please enter a number. Try again.")
            print("<<<<<<<<<<<<<<<<ERROR>>>>>>>>>>>>>>>>>")


    # Calculate the square and cube of the number

    square = num * num
    cube = num * num * num

    # Output the square and cube of the number

    print("////////////////////////////////////////////")
    print("Square", square, "Cube", cube)
    print("////////////////////////////////////////////")

    while True:

        another_num = input("Would you like to enter another number? (y,n) ")

        if another_num.lower() != "y":
            break
        
        calc()

#///////////////////////////////////////CALC ENDS HERE.//////////////////////////////////////////////

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('HUMAN')
    gvnman()
    calc()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



