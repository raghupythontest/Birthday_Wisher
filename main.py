##################### Hard Starting Project ######################
import pandas
import datetime as dt
import smtplib
import random
# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.

data=pandas.read_csv("birthdays.csv")
print(data)
# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
birthdays_dict={(row.month,row.day):row for (index,row) in data.iterrows()}

now=dt.datetime.now()
today=(now.month,now.day)
def sendemail(email,letter):
    MY_EMAIL = "raghupythontest@gmail.com"
    MY_PASSWORD = "Raghu1234"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=email,
            msg=f"Subject:Birthday Wish\n\n{letter}"
        )

if today in birthdays_dict:
    row=birthdays_dict[today]
    name=row["name"]
    email=row.email
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter=file.read()
        letter=letter.replace("[NAME]",name)
        print(letter)
    sendemail(email,letter)
    print("message sent success")
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)



