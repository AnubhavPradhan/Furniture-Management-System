from read import display_inventory
from write import write_inventory, employee_invoice, customer_invoice
        
# Function for purchase from employee
def purchases(inventory):
    try:
        employee_purchased_items = []
        display_inventory()

        while True:
            employee_name = input("Enter the name of the Employee: ")
            if employee_name.isalpha():
                break # Exit loop if name contains only alphabetic characters
            else:
                print("Please enter a valid name.")
        
        continue_loop = True
        while continue_loop:
            # valid id
            try:
                valid_id = int(input("Please Provide the ID of the Item you want to purchase: "))
                while valid_id <= 0 or valid_id > len(inventory):
                    print("Please provide a valid Item ID !!!")
                    print("\n")
                    valid_id = int(input("Please Provide the ID of the item you want to purchase:"))
                user_quantity = int(input("Please Provide the number of quantity of the item you want to purchase: "))
            except ValueError:
                print("Please enter numeric value")

            # Valid Quantity
            try:
                get_quantity_of_selected_item = inventory[str(valid_id)][2]
                #print(get_quantity_of_selected_item)
                while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_item):
                    print("Dear User, the quantity is not available. Please enter available quantity.")
                    user_quantity = int(input("Please Provide the number of quantity of the item you want to purchase: "))
            except ValueError:
                print("Please enter numeric value")

            # Updating the text file
            inventory[str(valid_id)][2] = str(int(inventory[str(valid_id)][2]) + user_quantity)
            write_inventory(inventory)
            
            # getting user purchased items
            product_id = str(valid_id)
            name_of_brand = inventory[product_id][0]
            name_of_product = inventory[product_id][1]
            price_of_selected_item = inventory[product_id][3].replace("$", '')
            total_price = int(price_of_selected_item) * user_quantity

            #Creating the list to store the purchase details
            employee_purchased_items.append([valid_id, name_of_brand, name_of_product, user_quantity, price_of_selected_item, total_price])

            more_items = input("Do you want to add more items? (Y/N): ").upper()
            if more_items == "Y":
                continue_loop = True
            else:
                continue_loop = False

        #Using for loop to get total cost   
        total = 0
        for i in employee_purchased_items:
            total+=int(i[5])
        vat=total*0.13
        total_with_vat=total+vat
        grand_total =total_with_vat

        employee_invoice(employee_name, employee_purchased_items, total, vat, grand_total)

        print("------------------------------------------------------------------------------------------------------------------\n")
        print("\t \t \t \t -Thank you for purchasing the Item-")
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("\n")
    except Exception as e:
        print("An error occurred:", e)
        

# Function for sales to customers
def sales(inventory):
    try:
        customer_purchased_items = []
        display_inventory()

        while True:
            customer_name = input("Enter the name of the Customer: ")
            if customer_name.isalpha():
                break  # Exit loop if name contains only alphabetic characters
            else:
                print("Please enter a valid name.")

        while True:
            phone_number = input("Enter the phone number of the Customer: ")
            try:
                phone_number = int(phone_number)  # Converting to integer
                if len(str(phone_number)) != 10:
                    print("Phone number must be of 10 digits!!")
                else:
                    break  # Exit loop 
            except ValueError:
                print("Please enter a valid phone number.")
  
        continue_loop = True
        while continue_loop:
            # valid id
            try:
                valid_id = int(input("Please Provide the ID of the Item you want to sell: "))
                while valid_id <= 0 or valid_id > len(inventory):
                    print("Please provide a valid Item ID !!!")
                    print("\n")
                    valid_id = int(input("Please Provide the ID of the item you want to sell:"))
                user_quantity = int(input("Please Provide the number of quantity of the item you want to sell: "))
            except ValueError:
                print("Please enter numeric value")

            # Valid Quantity
            try:
                get_quantity_of_selected_item = inventory[str(valid_id)][2]
                #print(get_quantity_of_selected_item)
                while user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_item):
                    print("Dear User, the quantity is not available. Please enter available quantity.")
                    user_quantity = int(input("Please Provide the number of quantity of the item you want to sell: "))
            except ValueError:
                print("Please enter numeric value")

            # Updating the text file
            inventory[str(valid_id)][2] = str(int(inventory[str(valid_id)][2]) - user_quantity)
            write_inventory(inventory)
            
            # getting user purchased items
            product_id = str(valid_id)
            name_of_brand = inventory[product_id][0]
            name_of_product = inventory[product_id][1]
            price_of_selected_item = inventory[product_id][3].replace("$", '')
            total_price = int(price_of_selected_item) * user_quantity

            #Creating the list to store the selling details
            customer_purchased_items.append([valid_id, name_of_brand, name_of_product, user_quantity, price_of_selected_item, total_price])

            more_items = input("Do you want to add more items? (Y/N): ").upper()
            if more_items == "Y":
                continue_loop = True
            else:
                continue_loop = False

        #printing bills in the screen
        shipping_cost = input("Dear user do you want your furniture to be shipped?(Y/N)").upper()

        #Calculating vat and adding shipping amount
        if shipping_cost=="Y":
            shipping_cost = 500
        else:
            shipping_cost = 0

        #Using for loop to get the total cost   
        total = 0
        for i in customer_purchased_items:
            total+=int(i[5])
        vat=total*0.13
        total_with_vat=total+vat
        grand_total =total_with_vat+shipping_cost

        customer_invoice(customer_name, phone_number, customer_purchased_items, total, vat, shipping_cost, grand_total)
        
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("\t \t \t \t -Thank you for purchasing the Item-")
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("\n")
    except Exception as e:
        print("An error occurred:", e)
