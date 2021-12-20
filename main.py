# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import sys


def send_email(user, pwd, recipient, subject, body, port=587):
    msg = MIMEMultipart()
    msg['From'] = user
    msg['Subject'] = subject
    msg.attach(MIMEText(body))
    toaddrs = recipient if isinstance(recipient, list) else [recipient]

    try:
        server = smtplib.SMTP("smtp.gmail.com", port)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(user, toaddrs, msg.as_string())
        server.quit()
        print('Successfully sent the mail')
    except:
        print("failed to send mail")


def main(argv):
    print(argv)
    mapping = {}
    #assume for simplicity it is [-arg command] therefore it is multiple of 2
    for i in range(0, len(argv), 2):
        arg = argv[i]
        val = argv[i+1]
        mapping[arg] = val

    print(mapping)
    send_email(mapping['-u'], mapping['-p'], mapping['-r'], mapping['-s'], mapping['-b'], mapping.get('-po', int(587)))




if __name__ == "__main__":
    main(sys.argv[1:])


