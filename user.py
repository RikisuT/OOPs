import re
import pickle
import time
from datetime import datetime


class ShoppingBot:
    def __init__(self):
        self.load_products()
        self.product_pattern = re.compile(
            r"\b(\d+)\s*([^\d,]+(?:\s+[^\d,]+)*)\b",
            re.IGNORECASE,
        )

    def load_products(self):
        try:
            with open("products.pkl", "rb") as file:
                self.products = pickle.load(file)
        except FileNotFoundError:
            print("Products file not found. Please check if the file exists.")
            self.products = {}
        except (IOError, EOFError, pickle.PickleError) as e:
            print("Error occurred while loading products:", e)

    def process_order(self, user_input):
        matched_products = self.product_pattern.findall(user_input)
        order_details = []

        for quantity, product_name in matched_products:
            product_name = product_name.strip().title()
            if product_name in self.products:
                try:
                    quantity = int(quantity)
                    if quantity <= 0:
                        print(
                            f"Invalid quantity '{quantity}' for product '{product_name}'. Please enter a positive integer."
                        )
                        continue
                except ValueError:
                    print(
                        f"Invalid quantity '{quantity}' for product '{product_name}'. Please enter a valid integer."
                    )
                    continue

                cost = self.products[product_name] * quantity
                order_details.append(
                    (product_name, quantity, self.products[product_name], cost)
                )
            else:
                print(
                    f"Invalid product '{product_name}'. Please enter a valid product name."
                )

        return order_details

    def display_menu(self):
        print("Welcome tothe Shopping Bot!")
        while True:
            print("\n_______MENU_______")
            print("1. Order Products")
            print("2. Check Order Details")
            print("3. Exit")
            choice = input("Enter your choice (1/2/3): ")
            if choice == "1":
                self.order_products()
            elif choice == "2":
                self.check_order_details()
            elif choice == "3":
                print("Thank you for using the Shopping Bot. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    def order_products(self):
        user_input = input("Enter your order (e.g., '1 Hand Wash, 3 Ketchup'): ")
        billing = self.process_order(user_input)
        if not billing:
            print("No valid products found in the order.")
            return

        self.print_bill(billing)
        proceed = input("Do you want to proceed to checkout? (yes/no): ").lower()
        if proceed == "yes":
            self.checkout(billing)
        else:
            print("Returning to the main menu.")

    def print_bill(self, billing):
        bill = "Name                Quantity      Cost       Price\n\n"
        for number in billing:
            bill += "{:<20} {:<12} {:<10} {}\n".format(
                number[0], number[1], number[2], number[3]
            )
        print(bill)

    def checkout(self, order_details):
        order_number = int(datetime.now().strftime("%d%H%M%S"))
        order_data = {
            "order_number": order_number,
            "bill": order_details,
            "delivery_status": "Pending",
        }

        orders = self.load_orders()
        orders.append(order_data)

        try:
            with open("orders.pkl", "wb") as file:
                pickle.dump(orders, file)
        except (IOError, pickle.PickleError) as e:
            print("Error occurred while saving order:", e)
            return

        print(f"Order placed successfully! Your order number is: {order_number}")
        print("Redirecting to main menu...")
        time.sleep(2)

    def load_orders(self):
        try:
            with open("orders.pkl", "rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            print("Orders file not found.")
            return []
        except (IOError, EOFError, pickle.PickleError) as e:
            print("Error occurred while loading orders:", e)
            return []

    def check_order_details(self):
        try:
            order_number = int(input("Enter your order number: "))
        except ValueError:
            print("Invalid input. Please enter a valid order number.")
            return

        if order_number <= 0:
            print("Order number must be a positive integer.")
            return

        orders = self.load_orders()
        found = False
        for order in orders:
            if order["order_number"] == order_number:
                self.print_order_details(order)
                found = True
                break

        if not found:
            print("Order not found.")

    def print_order_details(self, order):
        print(f"Order Number: {order['order_number']}")
        print("Order Details:")
        bill = "Name                Quantity      Cost       Price\n\n"
        for item in order["bill"]:
            bill += "{:<20} {:<12} {:<10} {}\n".format(
                item[0], item[1], item[2], item[3]
            )
        print(bill)
        print(f"Delivery Status: {order['delivery_status']}")


if __name__ == "__main__":
    shopping_bot = ShoppingBot()
    shopping_bot.display_menu()
