import smtplib
from email.message import EmailMessage
from tkinter import *


def save():
    with open('save.txt', 'w') as file: # Открываем файл с именем "save" c параметром "w" на запись
        file.write(sender_email_entry.get() + '\n') # Если файла нет, то создаётся автоматически
        file.write(recipient_email_entry.get() + '\n')
        file.write(password_entry.get() + '\n')


def load():
    try:
        with open('save.txt', 'r') as file: # Открываем файл для чтения
            info = file.readlines() # Читаем все строки файла и загружаем в переменную info
            sender_email_entry.insert(0, info[0].strip()) # С помощью команды insert вставляем на 0 место из 3-строк 1 строку индекс ноль
            recipient_email_entry.insert(0, info[1].strip())
            password_entry.insert(0, info[2].strip()) # Команда .strip удаляет переносы и в начале и в конце, оставляет только суть
    except FileNotFoundError: # Если файла нет, то ошибки об этом не будет, программа отработает и создаст файл, для этого и нужен pass
        pass


def send_email():
    save()
    sender_email = sender_email_entry.get() # Отправитель
    recipient_email = recipient_email_entry.get() # Получатель
    password = password_entry.get() # Пароль в Яндексе для почты
    subject = subject_entry.get() # Тема письма
    body = body_text.get(1.0, END) # С первого места текста до конца

    msg = EmailMessage() # msg - message, сообщение
    msg.set_content(body) # Что будет являться для отправки письма
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    server = None
    try:
        server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) # Порт для отправки сообщения, как морской
        server.login(sender_email, password)
        server.send_message(msg)
        result_label.config(text='Письмо отправлено!') # Связали метку для проверки результата
    except Exception as e:
        result_label.config(text=f'Ошибка: {e}')
    finally:
        if server:
            server.quit() # Сервер закрываем, если был открытым

window = Tk()
window.title('Отправка Email')
window.geometry('500x300')

Label(text="Отправитель:").grid(row=0, column=0, sticky=W) # Растягиваем в одну сторону
sender_email_entry = Entry() #
sender_email_entry.grid(row=0, column=1, sticky=W)

Label(text="Получатель:").grid(row=1, column=0, sticky=W)
recipient_email_entry = Entry()
recipient_email_entry.grid(row=1, column=1, sticky=W)

Label(text="Пароль приложения:").grid(row=2, column=0, sticky=W)
password_entry = Entry()
password_entry.grid(row=2, column=1, sticky=W)

Label(text="Тема письма:").grid(row=3, column=0, sticky=W)
subject_entry = Entry()
subject_entry.grid(row=3, column=1, sticky=W)

Label(text="Сообщение:").grid(row=4, column=0, sticky=W)
body_text = Text(width=45, height=10)
body_text.grid(row=4, column=1, sticky=W)

Button(text='Отправить письмо', command=send_email).grid(row=5, column=1, sticky=W)

result_label = Label(text='') # Метка для замены принта, сообщение об отправке
result_label.grid(row=6, column=1, sticky=W)

load()

window.mainloop()
