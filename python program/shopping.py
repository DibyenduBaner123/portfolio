class ShoppingApp:
    def __init__(self):
        self.products = {
            1: {"name": "Laptop", "price": 1000},
            2: {"name": "Smartphone", "price": 800},
            3: {"name": "Headphones", "price": 200},
            4: {"name": "Smartwatch", "price": 150},
        }
        self.cart = {}

    def display_products(self):
        """Display available products."""
        print("\nAvailable Products:")
        for product_id, details in self.products.items():
            print(f"{product_id}. {details['name']} - ${details['price']}")

    def add_to_cart(self):
        """Add a product to the cart."""
        try:
            product_id = int(input("\nEnter the product ID to add to the cart: "))
            if product_id in self.products:
                quantity = int(input("Enter the quantity: "))
                if product_id in self.cart:
                    self.cart[product_id]["quantity"] += quantity
                else:
                    self.cart[product_id] = {
                        "name": self.products[product_id]["name"],
                        "price": self.products[product_id]["price"],
                        "quantity": quantity,
                    }
                print(f"{quantity} {self.products[product_id]['name']}(s) added to the cart.")
            else:
                print("Invalid product ID.")
        except ValueError:
            print("Please enter a valid number.")

    def view_cart(self):
        """View the cart."""
        if not self.cart:
            print("\nYour cart is empty.")
        else:
            print("\nYour Cart:")
            total = 0
            for item in self.cart.values():
                subtotal = item["price"] * item["quantity"]
                total += subtotal
                print(f"{item['name']} - ${item['price']} x {item['quantity']} = ${subtotal}")
            print(f"Total: ${total}")

    def checkout(self):
        """Checkout and calculate total."""
        if not self.cart:
            print("\nYour cart is empty. Add items to proceed.")
        else:
            self.view_cart()
            confirm = input("\nDo you want to checkout? (yes/no): ").lower()
            if confirm == "yes":
                print("Checkout successful! Thank you for shopping.")
                self.cart.clear()
            else:
                print("Checkout canceled.")

    def run(self):
        """Run the shopping app."""
        while True:
            print("\n--- Shopping App ---")
            print("1. View Products")
            print("2. Add to Cart")
            print("3. View Cart")
            print("4. Checkout")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.display_products()
            elif choice == "2":
                self.add_to_cart()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                self.checkout()
            elif choice == "5":
                print("Thank you for using the shopping app. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = ShoppingApp()
    app.run()
