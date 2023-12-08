from address import Address
from mailing import Mailing

ex_to = Address(236000, "Kaliningrad", "Mira", 19, 4)
ex_from = Address(858034, "Moskow", "Lenina", 95, 32)
example = Mailing(ex_to, ex_from, 42, "UI-319")

print("Отправление", example.track, "из", example.from_address.index, 
      example.from_address.city, example.from_address.strit, 
      example.from_address.build, - example.from_address.flat, "в",
        example.to_address.index,
         example.to_address.city,
          example.to_address.strit,
      example.to_address.build, "-", example.to_address.flat, ".",
      "Стоимость", example.cost, "рублей."
      )