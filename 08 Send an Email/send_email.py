import smtplib

SENDER_EMAIL = '<your email>@gmail.com'  # replace with your email address
SENDER_PASSWORD = '<your password>'  # replace with your email password/app password if 2FA is enabled(needs to be setted up)

def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)


# commands used in solution video for reference
if __name__ == '__main__':
    # replace receiver email address
    send_email('<your email>@gmail.com', 'Notification', 'Everything is awesome!')
