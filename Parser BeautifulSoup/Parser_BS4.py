from bs4 import BeautifulSoup
import requests
from emails import emails

# def main():                                               #
#     base = 'https://ru.stackoverflow.com'                 #
#     html = requests.get(base).content                     #
#     soup = BeautifulSoup(html, 'lxml')                    #
#     div = soup.find('div', id='question-mini-list')       #
#     a = div.find_all('a', class_='s-link')                #
#                                                           #  парсер из видеоурока
#     for _ in a:                                           #
#         print(_.getText())                                #
#         print(base + _.get('href'), '\n')                 #
#                                                           #
# if __name__ == '__main__':                                #
#     main()                                                #



# вывод инф-ции в консоль                                   #
# for email in emails:                                      #
#     def main():                                           #
#         base = "https://haveibeenpwned.com/account/"+email#
#         html = requests.get(base).content                 #
#         soup = BeautifulSoup(html, 'lxml')                #
#         div = soup.find('div', id='pwnedSites')           #
#         div2 = div.find_all('div', class_='col-sm-10')    #   парсер из kwork
#         print(email)                                      #
#         for _ in div2:                                    #
#             print(_.getText())                            #
#         print("="*20)                                     #
#                                                           #
#     if __name__ == '__main__':                            #
#         main()                                            #




# запись инф-ции в файл                                     #
f = open("result.txt", "a")                                 #
for email in emails:                                        #
    print(email)                                            #
    f.write(email+"\n")                                     #
    def main():                                             #
        base = "https://haveibeenpwned.com/account/"+email  #
        html = requests.get(base).content                   #
        soup = BeautifulSoup(html, 'lxml')                  #
        div = soup.find('div', id='pwnedSites')             #
        div2 = div.find_all('div', class_='col-sm-10')      #   парсер из kwork
        if len(div2) == 0:                                  #
            f.write("\nGood news - no pwnage found!\n")     #
        for _ in div2:                                      #
            f.write(_.getText())                            #
        f.write("=" * 50+"\n")                              #
                                                            #
    if __name__ == '__main__':                              #
        main()                                              #
f.close()                                                   #