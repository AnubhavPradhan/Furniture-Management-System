from read import read_inventory
from operation import sales, purchases

# Printing header and welcome message 
print("\t \t \t \t  _-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_       ")
print("\t \t \t \t***                                               ***     ")
print("\t \t \t \t*** \t \t    Furniture Store             ***            ")
print("\t \t \t \t*** \t \t Gyaneshwor, Kathmandu            ***            ")
print("\t \t \t \t*** \t \t  Phone No.9844321549             ***            ")
print("\t \t \t \t***                                               ***     ")
print("\t \t \t \t  -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-       ")
print("\t \t \t \t \t      Welcome to the system Admin!")
print("------------------------------------------------------------------------------------------------------------------------")
print("\n")

# Making a function called main()
def main():
    # Putting try caatch exception for error
    try:
        inventory = read_inventory("stock.txt")
        loop = True
        while loop == True:
            # Putting try catch exception for ValueError
            try:
                print("Choose one of the options given below.")
                print("------------------------------------------------")
                print("Press 1 to Purchase furniture from manufacturer.")
                print("Press 2 to Sell furniture to the customer.")
                print("Press 3 to Exit from the system.")
                print("------------------------------------------------")
                user_input = int(input("Enter the option to continue: "))
                print("\n")

                # If Else loop for user input 
                if user_input == 1:
                    purchases(inventory)
                elif user_input == 2:
                    sales(inventory)
                elif user_input == 3:
                    loop = False
                    print("Thank you for using the system!")
                    print("\n")
                else:
                    print("Option", user_input, "does not seem to match our requirements. Please look at the options and try again.")
                    print("\n")
            except ValueError:
                print("Please look at the options and try again.")
                print("\n")

    except Exception as e:
        print("An error occurred:", e)

main()
