from models.device import Device


class Laptop(Device):
    def __init__(self, name, price, stock, warranty_period,
                 ram_size, processor_speed):
        super().__init__(name, price, stock, warranty_period)
        self.ram_size = ram_size
        self.processor_speed = processor_speed

    def __str__(self):
        return (super().__str__() +
                f" | RAM: {self.ram_size}GB"
                f" | CPU: {self.processor_speed}GHz")

    def run_program(self):
        print(f"{self.name} is running a program...")

    def use_keyboard(self):
        print(f"Typing on {self.name}...")
