from models.smartphone import Smartphone
from models.laptop import Laptop
from models.tablet import Tablet


def create_devices():
    devices = []

    for i in range(1, 8):
        devices.append(Smartphone(
            f"Smartphone {i}", 500 + i * 50,
            10 + i, 24, 6.5, 20))

    for i in range(1, 8):
        devices.append(Laptop(
            f"Laptop {i}", 900 + i * 100,
            5 + i, 36, 16, 3.2))

    for i in range(1, 7):
        devices.append(Tablet(
            f"Tablet {i}", 300 + i * 40,
            8 + i, 18, "2048x1536", 500))

    return devices
