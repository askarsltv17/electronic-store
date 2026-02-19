from models.device import Device


class Smartphone(Device):
    def __init__(self, name, price, stock, warranty_period,
                 screen_size, battery_life):
        super().__init__(name, price, stock, warranty_period)
        self.screen_size = screen_size
        self.battery_life = battery_life

    def __str__(self):
        return (super().__str__() +
                f" | Screen: {self.screen_size}\""
                f" | Battery: {self.battery_life}h")

    def make_call(self):
        print(f"{self.name} is making a call...")

    def install_app(self):
        print(f"Installing app on {self.name}...")
