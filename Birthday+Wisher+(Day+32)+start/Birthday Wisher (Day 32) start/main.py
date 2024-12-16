import smtplib


import datetime as dt
from random import choice
now = dt.datetime.now()

weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt","r") as file:
        q = file.readlines()
        r_q=choice(q)
    print(r_q)

    my_email = "kalenamdev168@gmail.com"
    password = "fceeomaaeolnbfsa"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="mistyraju0@gmail.com",
            msg=f"Subject:motivational_quote\n\n{r_q}"
        )

# import datetime as dt

from pandas import DataFrame
#
# now = dt.datetime.now()
# day = now.day
# print(day)
# day_week = now.weekday()
# print(day_week)
# if day == 16:
#     print("ready for braces??")