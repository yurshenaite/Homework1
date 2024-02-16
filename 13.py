blind_radius = int(input('Введите радиус слепой зоны: '))
far_radius = int(input('Введите радиус дальности приема: '))
territory_s = abs(((far_radius ** 2) * 3.14) - ((blind_radius ** 2) * 3.14))
print(f'Площадь покрываемой территории равна {round(territory_s, 1)}')
