##################### Extra Hard Starting Project ######################


import pandas
import smtplib
import datetime as dt
import random

data = pandas.read_csv("birthdays.csv")
data_dict = data.to_dict(orient="records")
# print(data_dict)

now = dt.datetime.now()
day_of_the_month = now.day
month = now.month

# print(day_of_the_month, month)
letters = []

for i in range(1,4):
    with open(f"letter_templates/letter_{i}.txt", "r") as d:
        string_d = ""
        for lines in d:
            string_d += lines
        letters.append(string_d)


my_email = "youremail@gmail.com"
password = "randomcode"


for person in data_dict:
    if person["day"] == day_of_the_month and person["month"] == month:
        chosen_letter = random.choice(letters)
        new_letter = chosen_letter.replace("[NAME]", person["name"])
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()

        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person["email"],
            msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter}"
            )

        connection.close()

