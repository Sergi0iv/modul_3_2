def send_email(message, recipient,
               sender='university.help@gmail.com'):
    if "@" not in recipient or "@" not in sender \
            or not recipient.endswith((".com", ".ru", ".net"))\
            or not sender.endswith((".com", ".ru", ".net")):
        print('Невозможно отправить письмо с адреса',
              sender, 'на адрис', recipient + '.')
    elif sender == recipient:
        print("Нельзя отправить письмо самому себе!")
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса',sender,'на адрес', recipient + '.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено'
              'с адреса', sender ,'на адрес', recipient + '.')


send_email(input('Введите сообщение: '), input('Введите E-mail получателя: '))