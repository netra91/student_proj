import smtplib, ssl


def send_mail(message):
    host = "smtp.gmail.com"
    port = 465
    username = "netra91ab@gmail.com"
    password = "pgdo bdjt pqpn thnc"
    receiver = "netra91ab@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)