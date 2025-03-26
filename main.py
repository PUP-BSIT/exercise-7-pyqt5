import os

def get_order_details(items):
    # Loop to continuously get order details from the user
    while True:
        # Get product details from the user
        product_name = input("\nEnter product name: ")
        product_price = float(input("Enter product price: "))
        product_quantity = int(input("Enter product quantity: "))
        total = product_price * product_quantity
        
        # Append item details to the list
        items.append([product_name, product_price, product_quantity, total])
        
        # Ask the user if they want to add another item
        add_item = input("\nDo you want to add another item?(y/n): ").lower()

        # If the user enters anything other than 'y', exit the loop
        if add_item != 'y':
            break
    
    # Return the updated list of items
    return items

def calculate_grand_total(items, senior_id):
    grand_total = 0
    # Iterate through the item list
    for product in items:
        grand_total += product[3]

    # Checks if senior_id is empty (spaces)
    if senior_id.strip():
        discount_rate = grand_total * 0.10
        return grand_total - discount_rate
    
    return grand_total

def display_order_summary(items, customer_name, senior_id, grand_total):
    print("\n=================== ITEMS ====================")
    print("Product Name\t Price\t Quantity\t Total")

    for item in items:
        print("----------------------------------------------")
        if len(item[0]) > 8:
            print(f"{item[0]}\t {item[1]}\t {item[2]}\t\t {item[3]}")
        else:
            print(f"{item[0]}\t\t {item[1]}\t {item[2]}\t\t {item[3]}")
    
    print("==============================================")
    print(f"Customer Name: {customer_name}")
    print(f"Senior Citizen ID: {senior_id}")
    print(f"Grand Total: {grand_total}")
    
if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    items = [] # list of items/products
    grand_total = 0 # variable for the grand_total
    # customer_name will be used to store customer name
    # senior_id will be used to store senior ID no.

    get_order_details(items)

    customer_name = input("\nEnter your name: ")
    senior_id = input("Enter your senior id no. (Leave blank if N/A): ")
    
    grand_total = calculate_grand_total(items, senior_id)
    
    display_order_summary(items, customer_name, senior_id, grand_total)