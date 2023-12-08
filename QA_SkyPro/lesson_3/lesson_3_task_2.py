from smartphone import Smartphone
catalog = [
    Smartphone('iPhone', '7', '+7 947 678 75 93'),
    Smartphone('Samsung', 'Galaxy Note', '+7 945 937 05 77'),
    Smartphone('Nokia', '3310', '8 800 555 35 35'),
    Smartphone('Xiaomi', 'Redmi 200', '+7 968 850 37 69'),
    Smartphone('SonyEricsson', 'w810', '+7 590 089 89 90')
]
for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.number)