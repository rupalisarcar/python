import requests
import datetime
import smtplib
import time

MY_LAT = 18.598372
MY_LONG = 73.915728
MY_EMAIL = "rupalisarkar12@gmail.com"
password = "rkrj xorl ncrp woec"

def iss_position_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    data = iss_response.json()
    iss_latitude = float(data['iss_position']['latitude'])
    iss_longitude = float(data['iss_position']['longitude'])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5 and nowHour>=sunset:
        return True

def is_night():
    parameters = {
        "lat" : MY_LAT,
        "lng" : MY_LONG
    }

    response = requests.get(url="https://api.sunrise-sunset.org/v2?lat=36.7201600&lng=-4.4203400", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = int(data['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['sunset'].split('T')[1].split(':')[0])
    print(sunrise, sunset)

    time_now = datetime.datetime.now()
    nowHour = time_now.hour
    print("now =",nowHour)

    if nowHour >= sunset or nowHour <= sunrise:
        return True

while True:
    time.sleep(60)
    if iss_position_overhead() and is_night():
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=password)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg='Subject:Look Up\n\nThe ISS is above you in the sky.')
