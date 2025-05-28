from datetime import datetime

# Creating a function write_inventory 
def write_inventory(inventory):
    with open("stock.txt", "w") as file:
        for key, values in inventory.items():
            file.write(f"{key},{','.join(values)}\n")

# Creating a function employee_invoice
def employee_invoice(employee_name, employee_purchased_items, total, vat, grand_total):
    try:
        today_date_and_time = datetime.now()
        # Printing Bill
        print("\n")
        print("\t \t \t \t  BRJ Furniture Shop Bill")
        print("\t \t \t \t   Gyaneshwor, Kathmandu")
        print("\t \t \t \t    Phone No:9844321549")
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("Name of the Employee: "+str(employee_name))
        print("Date and time of purchase: "+str(today_date_and_time))
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("Purchase Details are: ")
        print("\n")
        print("ID \t Item Brand \t\t\t Item Name \tQuantity \t Price \t\tTotal\n")
        print("------------------------------------------------------------------------------------------------------------------\n")
        for item in employee_purchased_items:
            print(str(item[0])+"\t"+str(item[1])+"\t\t\t"+str(item[2])+"\t"+str(item[3])+"\t\t"+"$"+str(item[4])+"\t\t"+"$"+str(item[5]))
        print("Total Amount: "+str(total))
        print("13% VAT: "+str(vat))
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("Total with 13% VAT: "+str(total + vat))
        print("Grand Total: "+str(grand_total))

        # Writing bill on the .txt file
        filename = f"{employee_name}_{today_date_and_time.strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        with open(filename, "w") as file:
            file.write("\n")
            file.write("\t \t \t \t  BRJ Furniture Shop Bill\n")
            file.write("\n")
            file.write("\t \t \t Gyaneshwor, Kathmandu | Phone No: 9844321549\n")
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Name of the Employee: "+str(employee_name))
            file.write("\n")
            file.write("Date and time of purchase: "+str(today_date_and_time))
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Purchase Details are: ")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("ID \t Item Brand \t\t\t Item Name \tQuantity \t Price \t \tTotal\n")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            for item in employee_purchased_items:
                file.write(str(item[0])+"\t"+str(item[1])+"\t\t\t"+str(item[2])+"\t"+str(item[3])+"\t\t"+"$"+str(item[4])+"\t\t"+"$"+str(item[5]))
                file.write("\n")
                file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Total Amount: "+str(total))
            file.write("\n")
            file.write("13% VAT: "+str(vat))
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Total with 13% VAT: "+str(total + vat))
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Grand Total: "+str(grand_total))
            file.write("\n")
            file.close()
    except Exception as e:
        print("An error occurred:", e)


# Creating a function customer_invoice
def customer_invoice(customer_name, phone_number, customer_purchased_items, total, vat, shipping_cost, grand_total):
    try:
        today_date_and_time = datetime.now()
        # Printing Bill
        print("\n")
        print("\t \t \t \t  BRJ Furniture Shop Bill")
        print("\t \t \t \t   Gyaneshwor, Kathmandu")
        print("\t \t \t \t    Phone No:9844321549")
        print("-------------------------------------------------------------------------\n")
        print("Name of the Customer: "+str(customer_name))
        print("Contact number: "+str(phone_number))
        print("Date and time of purchase: "+str(today_date_and_time))
        print("-------------------------------------------------------------------------\n")
        print("Purchase Details are: ")
        print("\n")
        print("ID \t Item Brand \t\t\t Item Name \tQuantity \t Price \t\tTotal\n")
        print("------------------------------------------------------------------------------------------------------------------\n")
        for item in customer_purchased_items:
            print(str(item[0])+"\t"+str(item[1])+"\t\t\t"+str(item[2])+"\t"+str(item[3])+"\t\t"+"$"+str(item[4])+"\t\t"+"$"+str(item[5]))
        print("Total Amount: "+str(total))
        print("13% VAT: "+str(vat))
        print("------------------------------------------------------------------------------------------------------------------\n")
        print("Total with 13% VAT: "+str(total + vat))
        print("Your Shipping Cost is: "+str(shipping_cost))
        print("Grand Total: "+str(grand_total))
        
        # Writing bill on the .txt file
        filename = f"{customer_name}_{phone_number}_{today_date_and_time.strftime('%Y_%m_%d_%H_%M_%S')}.txt"
        with open(filename, "w") as file:
            file.write("\n")
            file.write("\t \t \t \t  BRJ Furniture Shop Bill\n")
            file.write("\n")
            file.write("\t \t \t Gyaneshwor, Kathmandu | Phone No: 9844321549\n")
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Name of the Customer: "+str(customer_name))
            file.write("\n")
            file.write("Contact number: "+str(phone_number))
            file.write("\n")
            file.write("Date and time of purchase: "+str(today_date_and_time))
            file.write("\n")
            file.write("-------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Purchase Details are: ")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("ID \t Item Brand \t\t\t Item Name \tQuantity \t Price \t \tTotal\n")
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            for item in customer_purchased_items:
                file.write(str(item[0])+"\t"+str(item[1])+"\t\t\t"+str(item[2])+"\t"+str(item[3])+"\t\t"+"$"+str(item[4])+"\t\t"+"$"+str(item[5]))
                file.write("\n")
                file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Total Amount: "+str(total))
            file.write("13% VAT: "+str(vat))
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Total with 13% VAT: "+str(total + vat))
            file.write("Your Shipping Cost is: "+str(shipping_cost))
            file.write("\n")
            file.write("------------------------------------------------------------------------------------------------------------------\n")
            file.write("\n")
            file.write("Grand Total: "+str(grand_total))
            file.write("\n")
            file.close()
    except Exception as e:
        print("An error occurred:", e)


 
