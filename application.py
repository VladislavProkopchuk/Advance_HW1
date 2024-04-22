import os

os.makedirs("application")

# Создание файлов salary.py и people.py
with open("application/salary.py", "w") as file:
    file.write("# Файл salary.py\n\nprint('Это файл salary.py')")

with open("application/people.py", "w") as file:
    file.write("# Файл people.py\n\nprint('Это файл people.py')")

print("Пакет application успешно создан!")


#Для заполнения файлов salary.py и people.py данными
# Заполнение файла salary.py
salaries = [2500, 3000, 3500, 4000, 4500]

with open('salary.py', 'w') as file:
    file.write('salaries = ' + str(salaries))

# Заполнение файла people.py
people = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

with open('people.py', 'w') as file:
    file.write('people = ' + str(people))