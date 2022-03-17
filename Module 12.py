per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
vklad = (float(input("Программа для рассчета накоплений на депозитах разных банков.\nВведите сумму желаемого вклада:")))/100
list_deposit = list(per_cent.values())
deposit = list(map(lambda x: int(x*vklad), list_deposit))

print(deposit)

max_element = max(deposit)

print("Максимальная сумма, которую вы можете заработать:", max_element, "рублей")