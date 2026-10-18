from smartphone import Smartphone

catalog = [
    Smartphone('Honor', 'X9b', '+79182153365'),
    Smartphone('Xiaomi', '11 Ultra', '+79521255568'),
    Smartphone('Samsung', 'Galaxy S15', '+79992996555'),
    Smartphone('Google', 'Pixel 10 Pro', '+79205541235'),
    Smartphone('Nokia', 'C100', '+79045548712')
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
