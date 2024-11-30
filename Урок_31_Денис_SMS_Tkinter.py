import smtplib
from email.message import EmailMessage
from tkinter import *


def send_email():
    sender_email = 'Python24new@yandex.ru' # Отправитель
    recipient_email = 'Iskander_ekb@mail.ru' # Получатель
    password = 'sguswkmmaoiwwbhh' # Пароль в Яндексе для почты
    subject = 'Проверка связи!' # Тема письма
    body = 'Привет из программы на Python' # Тело письма, сообщение

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
        print('Письмо отправлено успешно!')
    except Exception as e:
        print(f'Ошибка: {e}')
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
result_label.grid(row=5, column=1, sticky=W)

window.mainloop()
