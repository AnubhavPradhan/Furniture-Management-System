# Creating a function read_inventory to read the stock.txt file
def read_inventory(filename):
    file = open("stock.txt", "r")
    inventory = {}
    for line in file:
        line = line.replace("\n", "")
        # Split the line into a list of strings based on comma
        line = line.split(",")
        # Initialize an empty list to store item features
        item_features=[]
        for i in range (1, len(line)):
            item_features.append(line[i].strip())
        inventory[line[0]] = item_features
    file.close()
    return inventory

# Creating a function display_inventory to display the furniture stock when called
def display_inventory():
    print("-------------------------------------------------------------------------------------------------------------------------")
    print("S.N. \tCompany Name \tItem Name \tQuantity Price")
    print("-------------------------------------------------------------------------------------------------------------------------")
    file = open("stock.txt", "r")
    for line in file:
        print(line.replace(",", "\t"))
    print("-------------------------------------------------------------------------------------------------------------------------")
    file.close()
