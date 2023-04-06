import requests
import datetime as dt
import smtplib
import time
my_email = "tpython02@gmail.com"
password = "emjoacmqipomxuao"
MY_LAT = 19.240330
MY_LNG = 73.130539


def is_iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG - 5 <= iss_longitude <= MY_LNG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]
    sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_close() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg="Subject:Look Up \n\nThe ISS is above you in "
                                    "the sky")
