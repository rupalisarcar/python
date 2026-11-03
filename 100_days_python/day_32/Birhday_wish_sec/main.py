##################### Extra Hard Starting Project ######################
import smtplib
import pandas
import datetime
import random

# 1. Update the birthdays.csv
file_path = "D:/python/100_days_python/day_32/Birhday_wish_sec/birthdays.csv"
EMAIL = "rupalisarkar12@gmail.com"
PASSWORD = "rkrj xorl ncrp woec"

data = pandas.read_csv(file_path)
birthday_file = data.to_dict(orient="records") 
print(birthday_file[0]["month"])

now = datetime.datetime.now()
month = now.month
day = now.day
birthday_data = [item for item in birthday_file if month==item["month"] and day==item["day"]]

if birthday_data:
    letter = f"D:/python/100_days_python/day_32/Birhday_wish_sec/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(letter,'r') as letter_file:
        birthday_letter = letter_file.read()

    for person in birthday_data:
        print("person", person)
        new_birthday_letter = birthday_letter.replace("[NAME]", person["name"])    
        print(new_birthday_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=person["email"],msg=f"Subject:Happy Birthday!\n\n\n{new_birthday_letter}")


# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




