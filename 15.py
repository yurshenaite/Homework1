distance_sm = float(input('Введите расстояние в сантиметрах: '))
inch = round(2.54 * distance_sm, 1)
foot = round(12 * (2.54 * distance_sm), 1)
yard = round(36 * (2.54 * distance_sm), 1)
mile = round(1760 * 36 * (2.54 * distance_sm), 1)
print(f'{yard} ярдов',
      f'{mile} мили',
      f'{foot} футов',
      f'{inch} дюймов', sep='\n')
