##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import random
from datetime import datetime
import pandas
import smtplib

my_email = "kalenamdev168@gmail.com"
my_password = "fceeomaaeolnbfsa"

now = datetime.now()
today = (now.month,now.day)



data = pandas.read_csv("birthdays.csv")
new_dict = {(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.iterrows()}
if today in new_dict:
    birthday_person = new_dict[today]

    letter_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter_path) as l_file:
        content = l_file.read()
        content = content.replace("[NAME]",birthday_person["name"])



    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user = my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{content}"
        )