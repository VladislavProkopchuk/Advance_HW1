from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()

from datetime import datetime   # Для вывода текущей даты при вызове функций в файле main.py можно использовать модуль datetime

def my_function():
    print("Current date:", datetime.now())

if __name__ == '__main__':
    my_function()


                            # расчет зарплаты
def calculate_salary():   # тут наверное лучше или надо в отдельном файле сделать реализацию, просто в задании
                            # не написано сколько файлов отправлять.

    print("Calculating salary...")


def get_employees(): # получение данных о сотрудниках из базы данных
    print("Getting employees...")

                                    #Это основная структура программы "Бухгалтерия", где в main.py импортированы функции calculate_salary из модуля salary.py и get_employees из модуля people.py.
                                    #При запуске программы будет вызываться расчет зарплаты и получение данных о сотрудниках.



requests==2.26        # package_name==version
pip install -r requirements.txt # установка всех пакетов из requirements.txt


# example.py
import requests

response = requests.get("https://api.github.com")    # пакет requests для отправки HTTP-запросов.
print(response.status_code)                          #отправит GET-запрос на API GitHub и выведет статус ответа.
