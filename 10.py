flight_nmb = int(input('номер рейса: '))
ru_airline_name = input('название авиакомпании (на русском): ')
eng_airline_name = input('название авиакомпании (на англиском): ')
ru_city = input('город прилета (на русском): ')
eng_city = input('город прилета (на английском): ')
print(f'Заканчивается посадка на рейс {flight_nmb} авиакомпании'
      f' {ru_airline_name} в город {ru_city}')
print(f'This is the final boarding call for {eng_airline_name} '
      f'flight {flight_nmb} to {eng_city}')