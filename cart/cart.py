class Cart:
    def __init__(self):
        self.items = []
        self.total_price = 0

    def add_device(self, device, amount):
        if amount <= 0:
            raise ValueError("Quantity must be greater than 0.")

        if not device.is_available(amount):
            raise ValueError("Not enough stock available.")

        self.items.append((device, amount))
        self.total_price += device.price * amount
        print(f"{amount} x {device.name} added to cart.")

    def remove_device(self, device, amount):
        for item in self.items:
            if item[0] == device:
                if amount <= 0:
                    raise ValueError("Quantity must be positive.")

                if amount >= item[1]:
                    self.total_price -= item[0].price * item[1]
                    self.items.remove(item)
                else:
                    self.total_price -= item[0].price * amount
                    self.items.remove(item)
                    self.items.append((device, item[1] - amount))

                print("Item removed from cart.")
                return

        raise ValueError("Item not found in cart.")

    def apply_cart_discount(self):
        if self.total_price > 5000:
            discount = self.total_price * 0.10
            print("10% discount applied!")
        elif self.total_price > 2000:
            discount = self.total_price * 0.05
            print("5% discount applied!")
        else:
            discount = 0

        self.total_price -= discount
        return discount

    def get_total_price(self):
        return self.total_price

    def print_items(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n--- CART ITEMS ---")
        for device, amount in self.items:
            print(f"{device.name} x {amount} = ${device.price * amount:.2f}")

        print(f"Subtotal: ${self.total_price:.2f}")

    def checkout(self):
        if not self.items:
            raise ValueError("Cart is empty.")

        for device, amount in self.items:
            if not device.is_available(amount):
                raise ValueError(f"{device.name} does not have enough stock.")

        discount = self.apply_cart_discount()

        for device, amount in self.items:
            device.reduce_stock(amount)

        print("\n--- RECEIPT ---")
        self.print_items()
        print(f"Discount: -${discount:.2f}")
        print(f"Final Total: ${self.total_price:.2f}")
        print("Purchase successful!")

        self.items.clear()
        self.total_price = 0
