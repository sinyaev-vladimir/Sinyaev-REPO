count = int(input("Сколько билетов вы хотите купить?:\t"))
age =[]
price = 0

for i in range(count):
    while True:
        try:
            age.append(int(input(f"Введите возраст {i + 1}-го посетителя:\t")))
        except ValueError:
            print("Error! Это не число, попробуйте снова.")
        # age.append(int(input(f"Введите возраст {i + 1}-го посетителя:\t")))
        else:
            break
for i in range(count):
    if 17 < age[i] < 25:
        price += 990
    elif 24 < age[i]:
        price += 1390

print(f"стоимость {count} билетов: {price} руб.")