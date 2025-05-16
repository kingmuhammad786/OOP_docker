import os


# Define the Shoe class with attributes and methods
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f"{self.product} ({self.code}) from {self.country}: ${self.cost} " \
               f"- {self.quantity} units available"


# Initialize the shoes list
shoes_list = []


# Function to read shoes data from the file
def read_shoes_data():
    file_path = "inventory.txt"
    
    if not os.path.exists(file_path):
        print("Error: Inventory file not found. Please ensure 'inventory.txt' exists.")
        return
    
    try:
        with open(file_path, "r") as file:
            next(file)  # Skip the first line (header)
            for line in file:
                data = line.strip().split(',')
                if len(data) == 5:
                    try:
                        shoe = Shoe(data[0], data[1], data[2], float(data[3]), int(data[4]))
                        shoes_list.append(shoe)
                    except ValueError:
                        print(f"Warning: Invalid data format in line - {line.strip()}")
    except Exception as e:
        print(f"Error reading file: {e}")


# Function to capture shoe data from the user
def capture_shoes():
    while True:
        country = input("Enter the country of the shoe: ").strip()
        code = input("Enter the shoe code: ").strip()
        product = input("Enter the product name: ").strip()

        try:
            cost = float(input("Enter the cost of the shoe: "))
            quantity = int(input("Enter the quantity of the shoe: "))
        except ValueError:
            print("Error: Cost must be a number, and quantity must be an integer.")
            continue

        if not country or not code or not product:
            print("Error: Country, code, and product name cannot be empty.")
            continue

        shoe = Shoe(country, code, product, cost, quantity)
        shoes_list.append(shoe)
        break


# Function to search for a shoe by code
def search_shoe():
    code = input("Enter the shoe code to search: ").strip()
    found = False

    for shoe in shoes_list:
        if shoe.code == code:
            print(shoe)
            found = True
            break

    if not found:
        print(f"Error: No shoe found with code '{code}'. Please check 'inventory.txt' for available options.")


# Function to restock the shoe with the lowest quantity
def re_stock():
    if not shoes_list:
        print("Error: No shoes available in inventory.")
        return

    min_quantity_shoe = min(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"Lowest quantity shoe: {min_quantity_shoe}")
    
    while True:
        try:
            add_quantity = int(input("Enter the quantity to add: "))
            if add_quantity < 0:
                print("Error: Quantity cannot be negative.")
                continue
            break
        except ValueError:
            print("Error: Quantity must be a positive integer.")

    min_quantity_shoe.quantity += add_quantity

    # Update the file
    with open("inventory.txt", "w") as file:
        file.write("Country,Code,Product,Cost,Quantity\n")  # Re-write header
        for shoe in shoes_list:
            file.write(f"{shoe.country},{shoe.code},{shoe.product},{shoe.cost},{shoe.quantity}\n")


# Function to calculate and print the value per item
def value_per_item():
    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()
        print(f"{shoe.product} ({shoe.code}): Total value = ${value}")


# Function to find and print the shoe with the highest quantity
def highest_qty():
    if not shoes_list:
        print("Error: No shoes available in inventory.")
        return

    max_quantity_shoe = max(shoes_list, key=lambda shoe: shoe.get_quantity())
    print(f"Shoe with highest quantity for sale: {max_quantity_shoe}")


# Function to view all shoes
def view_all():
    if not shoes_list:
        print("Error: No shoes available in inventory.")
        return
    
    for shoe in shoes_list:
        print(shoe)


# Create a menu to execute each function
def menu():
    while True:
        print("\nShoe Inventory Management")
        print("1. Read shoes data")
        print("2. Capture shoe data")
        print("3. View all shoes")
        print("4. Re-stock shoes")
        print("5. Search for a shoe")
        print("6. Calculate value per item")
        print("7. Show shoe with highest quantity")
        print("0. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            read_shoes_data()
        elif choice == '2':
            capture_shoes()
        elif choice == '3':
            view_all()
        elif choice == '4':
            re_stock()
        elif choice == '5':
            search_shoe()
        elif choice == '6':
            value_per_item()
        elif choice == '7':
            highest_qty()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    menu()

