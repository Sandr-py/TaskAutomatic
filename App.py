import re
from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import requests
course_list = []
con = requests.get("https://cbr.ru/currency_base/daily/")

print(con.status_code)

soup = BeautifulSoup(con.text, "html.parser")
alldata = soup.findAll('tr')
for data in alldata:
    course_list.append(data.text)
# print(course_list)

for data in course_list:
    course_list[course_list.index(data)] = data.split('\n')

# print(course_list)
# (i[5].split(','))[0]
for i in course_list:
    if i[2] == 'USD':
        US_course = float(re.sub(r',', '.', string=i[5]))
    elif i[2] == 'EUR':
        EU_course = float(re.sub(r',', '.', i[5]))

print(US_course, EU_course)
# print(alldata)
# print(USD)



def disk_t():
    a = summa.get()
# Обработка исключений
# (возникла ошибка ввиду невозможности корректного прерывания функции в случае ввода неправильных данных)
# Решение данной проблемы будет представлено ниже.
    try:
        a = int(a)
    except ValueError:
        sale_label.configure(text='Некорректная форма записи', fg='red')
        accept_button.configure(command=disk_t)

    def sale(k):
        t = k * US_course
        sale_label.configure(text=f'{t} руб.', fg='black')
# Условием повторно проверяется правильность введённых данных, в противном случае в поле вывода выбивается ошибка.
    if type(a) != int:
        sale_label.configure(text=f'Некорректная форма записи', fg='red')

    elif a < 0:
        sale_label.configure(text=f'Число не должно быть отрицательным', fg='red')

    else:
        sale(a)


# Инициализация корневого окна приложения.

root = Tk()
root.title('Конвертер доллара в рубли')
root.geometry('390x190')
root.configure(bg='#FFF8DC')

main_frame = LabelFrame(root, text='Конвертер', bd=5, bg='#FFF8DC')
main_frame.grid(pady=5, padx=5)

# Добавление подписи к полю ввода с указанием единиц измерения.

main_label = Label(master=main_frame, text='Введите сумму:', font=('Arial', 20), bg='#FFF8DC')
main_label.grid(row=0, columnspan=2, sticky=W + E, pady=5)

meas_system = Label(master=main_frame, text='usd.', font=('Arial', 14), bg='#FFF8DC')
meas_system.grid(row=1, column=1, sticky=W)

# Добавление кнопки отправления данных в функцию-обработчик.

accept_button = Button(master=main_frame, text='Принять', font=('Arial', 10), command=disk_t, bg='#F4A460', bd=1,
                       relief=FLAT, activebackground="#8B4513")
accept_button.grid(row=2, columnspan=2, sticky=E + W, pady=7)

# Добавление поля ввода необходимых данных

summa = Entry(master=main_frame, width='20', font=('Arial', 14), bg='#FFDEAD')
summa.grid(row=1, column=0, sticky=E)

# Добавление изменяемого текстового поля-вывода.

sale_label = Label(main_frame, font=('Arial', 15), bg='#FFDEAD')
sale_label.grid(row=3, columnspan=2, sticky=E + W)

root.mainloop()
