import os

def get_order_details(items, add_item):
    # Check if the user wants to stop adding items
    if add_item == 'n':
        return
        
    # Get product details from user input
    product_name = input("\nEnter product name: ")
    product_price = float(input("Enter product price: "))
    product_quantity = int(input("Enter product quantity: "))
    total = product_price * product_quantity
        
    # Append item details to the list
    items.append([product_name, product_price, product_quantity, total])
        
    # Ask user if they want to add another item
    add_item = input("\nDo you want to add another item?(y/n): ").lower()
        
    # Recursively call the function to continue adding items
    return get_order_details(items, add_item)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    
    items = [] # list of items/products
    add_item = "y" # sentinel variable for adding another item
    grand_total = 0 # variable for the grand_total
    # customer_name will be used to store customer name
    # senior_id will be used to store senior ID no.

    # TODO(Caya): Implement get_order_details function

    # TODO(Condino): Add get customer name, and senior id input handling

    # TODO(Cordova): Implement calculate_grand_total function

    # TODO(Arguelles): Implement display_order_summary function

    # TODO(Gutierrez): Implement display_order_summary function