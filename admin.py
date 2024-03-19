import pickle

# Sample admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "password"


def authenticate():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
        return True
    else:
        print("Invalid username or password.")
        return False


def display_menu():
    print("\n_______ADMIN MENU_______")
    print("1. Update Delivery Status")
    print("2. Delete Order")
    print("3. View All Orders")
    print("4. Exit")


def order_exists(orders, order_number):
    for order in orders:
        if order["order_number"] == order_number:
            return True
    return False


def load_orders():
    try:
        with open("orders.pkl", "rb") as file:
            orders = pickle.load(file)
    except FileNotFoundError:
        print("No orders found.")
        orders = []
    return orders


def save_orders(orders):
    with open("orders.pkl", "wb") as file:
        pickle.dump(orders, file)


def update_delivery_status():
    order_number = get_valid_order_number()
    orders = load_orders()

    if order_exists(orders, order_number):
        new_status = input("Enter the new delivery status: ")
        for order in orders:
            if order["order_number"] == order_number:
                order["delivery_status"] = new_status

        save_orders(orders)
        print("Delivery status updated successfully.")
    else:
        print("Order not found.")


def delete_order():
    order_number = get_valid_order_number()
    orders = load_orders()

    if order_exists(orders, order_number):
        orders = [order for order in orders if order["order_number"] != order_number]

        save_orders(orders)
        print("Order deleted successfully.")
    else:
        print("Order not found.")


def view_all_orders():
    orders = load_orders()
    for order in orders:
        print(f"Order Number: {order['order_number']}")
        print("Order Details:")
        bill = "Name                Quantity      Cost       Price\n\n"
        for item in order["bill"]:
            bill += "{:<20} {:<12} {:<10} {}\n".format(
                item[0], item[1], item[2], item[3]
            )
        print(bill)
        print(f"Delivery Status: {order['delivery_status']}")
        print("-" * 40)


def get_valid_order_number():
    while True:
        try:
            order_number = int(input("Enter the order number: "))
            if order_number < 0:
                print("Order number must be a positive integer.")
            else:
                return order_number
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    if not authenticate():
        exit()

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            update_delivery_status()
        elif choice == "2":
            delete_order()
        elif choice == "3":
            view_all_orders()
        elif choice == "4":
            print("Exiting admin panel.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
