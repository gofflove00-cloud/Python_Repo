from address import Address
from mailing import Mailing

sender_address = Address('323000', 'Сочи', 'Армянская', '78', '15')
reciever_address = Address('353500', 'Краснодар', 'Партизан', '112', '45')

mail = Mailing(
    to_address=reciever_address,
    from_address=sender_address,
    cost=750.00,
    track='PR323000353500'
)

print(
    f'Отправление {mail.track} из'
    f'{mail.from_address.index}, {mail.from_address.city}, '
    f'{mail.from_address.street}, {mail.from_address.house} - '
    f'{mail.from_address.appartment} в '
    f'{mail.to_address.index}, {mail.to_address.city}, '
    f'{mail.to_address.street}, {mail.to_address.house} - '
    f'{mail.to_address.appartment}. '
    f'Стоимость {mail.cost} рублей.'
)
