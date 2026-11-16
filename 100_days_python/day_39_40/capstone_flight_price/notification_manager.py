import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self._email = os.environ["MY_EMAIL"]
        self.password = os.environ["MY_PASSWORD"]

    def send_email(self, email_list, email_body):
        for email in email_list : 
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=self._email, password=self.password)
                connection.sendmail(from_addr=f"{self._email}", to_addrs=email, msg=f"Subject:New Low Price Flight!\n\n{email_body}".encode('utf-8'))