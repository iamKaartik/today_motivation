import datetime as dt
import smtplib
import random

now = dt.datetime.now()

weekday = now.weekday()
if weekday == 0:

    with open("qoutes.txt","r") as qoute_file:
        all_quotes = qoute_file.readline();
        qoute = random.choice(all_quotes)
    print(qoute)

    my_email = ""
    password = "kyu_bataye"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmai(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject: Hello\n Today's Motivation:\n\n {qoute}"
        )
