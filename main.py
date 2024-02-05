import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 41.010700 # Your latitude
MY_LONG = 28.638081 # Your longitude

MY_EMAIL = "YOUR EMAIL HERE"
MY_PASSWORD = "YOUR PASSWORD HERE"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


def iss_overhead():
    if MY_LAT -5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG +5 and time_now >= sunset or time_now <= sunrise:
        with smtplib.SMTP("smtp.gmail.com",587 ) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="RECEİVER EMAİL",
                                msg="Subject:Look Up👆\n\nThe ISS is above you in the sky.")
            connection.close()
    return True

while True:
    time.sleep(60)
    iss_overhead()





