from models.smartphone import Smartphone

def test_discount():
    phone = Smartphone("Test Phone", 1000, 5, 24, 6.1, 15)
    phone.apply_discount(10)
    assert phone.price == 900
