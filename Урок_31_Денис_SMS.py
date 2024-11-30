import smtplib
from email.message import EmailMessage

sender_email = 'Python24new@yandex.ru' # Отправитель
recipient_mail = 'Iskander_ekb@mail.ru' # Получатель
password = 'sguswkmmaoiwwbhh' # Пароль в Яндексе для почты
subject = 'Проверка связи!' # Тема письма
body = 'Привет из программы на Python' # Тело письма, сообщение

msg = EmailMessage() # msg - message, сообщение
msg.set_content(body) # Что будет являться для отправки письма
msg['Subject'] = subject
msg['From'] = sender_email
msg['To'] = recipient_mail

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