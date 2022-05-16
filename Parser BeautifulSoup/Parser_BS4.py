from bs4 import BeautifulSoup
import requests
from emails import em

# def main():
#     base = 'https://ru.stackoverflow.com'
#     html = requests.get(base).content
#     soup = BeautifulSoup(html, 'lxml')
#     div = soup.find('div', id='question-mini-list')
#     a = div.find_all('a', class_='s-link')
#
#     for _ in a:
#         print(_.getText())
#         print(base + _.get('href'), '\n')
#
# if __name__ == '__main__':
#     main()


# вывод инф-ции в консоль
# for i in em:
#     def main():
#         base = "https://haveibeenpwned.com/account/"+i
#         html = requests.get(base).content
#         soup = BeautifulSoup(html, 'lxml')
#         div = soup.find('div', id='pwnedSites')
#         a = div.find_all('div', class_='col-sm-10')
#         print(i)
#         for _ in a:
#             print(_.getText())
#         print("="*20)
#
#
#     if __name__ == '__main__':
#         main()


# запись инф-ции в файл
f = open("result.txt", "a")
for i in em:
    print(i)
    f.write(i+"\n")
    def main():
        base = "https://haveibeenpwned.com/account/"+i
        html = requests.get(base).content
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', id='pwnedSites')
        ar = div.find_all('div', class_='col-sm-10')

        for _ in ar:
            if _.getText() != 0:
                f.write(_.getText())
            else:
                f.write("Good news - no pwnage found!")

        f.write("=" * 50+"\n")


    if __name__ == '__main__':
        main()
f.close()
