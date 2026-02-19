from cart.cart import Cart
from data.create_devices import create_devices


def main():
    devices = create_devices()
    cart = Cart()

    while True:
        print("\n====== ELECTRONIC STORE ======")
        print("1. Show Devices")
        print("2. Show Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose option: ")

        try:
            if choice == "1":
                for index, device in enumerate(devices):
                    print(f"{index + 1}. {device}")

                selection = int(input("Select device number (0 to cancel): "))
                if selection == 0:
                    continue

                amount = int(input("Enter quantity: "))
                cart.add_device(devices[selection - 1], amount)

            elif choice == "2":
                cart.print_items()

            elif choice == "3":
                cart.checkout()

            elif choice == "4":
                print("Goodbye!")
                break

            else:
                print("Invalid option. Please choose 1-4.")

        except ValueError as e:
            print(f"Error: {e}")

        except IndexError:
            print("Invalid device number.")

        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
