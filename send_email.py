import smtplib, ssl
# import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "dzheng@terpmail.umd.edu"
    password = "abnplxgfhtacnoet"
    # password = os.getenv("PASSWORD")

    recipient = "dzheng@terpmail.umd.edu"

    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, recipient, message)
