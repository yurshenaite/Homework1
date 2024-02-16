blind_radius = int(input('Введите радиус слепой зоны: '))
far_radius = int(input('Введите радиус дальности приема: '))
territory_s = ((far_radius ** 2) * 3.14) - ((blind_radius ** 2) * 3.14)
print(f'Площадь покрываемой территории равна {territory_s}')