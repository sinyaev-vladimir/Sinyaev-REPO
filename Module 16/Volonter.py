class volonter:
    def __init__(self, name, city, role):
        self.name = name
        self.city = city
        self.role = role

    def Volonter(self):
        return self.name, self.city, self.role


yesno = input("Вы наставник? +/- : ")

if yesno == "+":
    status = (''' "Наставник" ''')
else:
    status = (''' "Пользователь" ''')

newVolonter = volonter('"' + input('Введите ваше имя: '), "г." + input('Введите ваш город: '), status)
text = str(newVolonter.Volonter()).replace("'", "")[1:-1]
f = open('Volonter_List.txt', 'a', encoding='utf8')
f.write(f"\n {text}")
f.close()

f = open('Volonter_List.txt', 'r', encoding='utf8')
print(f.read())
f.close()