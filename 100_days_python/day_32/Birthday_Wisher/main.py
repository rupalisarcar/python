import smtplib
import datetime
import random

my_email = "rupalisarkar12@gmail.com"
password = "rkrj xorl ncrp woec"
another_email = "rikirock.012@gmail.com"

now = datetime.datetime.now()
weekday = now.weekday()
if weekday ==2:
    with open("D:/python/100_days_python/day_32/Birthday_Wisher/quotes.txt",'r') as file:
        data = file.readlines()
        quote_text = random.choice(data)
       

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #make it secure
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,to_addrs=my_email,msg=f"Subject:Motivation\n\n{quote_text}")
