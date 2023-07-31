import requests
from datetime import datetime
import smtplib
import time

my_email = "kagisele@outlook.com"
my_password = "kazeGisele011"
my_lat = 51.507351
my_lng = -0.127758


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if my_lat-5 <= iss_latitude <= my_lat+5 and my_lng-5 <= iss_longitude <= my_lng+5:
        return True


def night():
    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now_time = datetime.now().hour
    if now_time >= sunset or now_time <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_overhead() and night():
        connection = smtplib.SMTP("smtp-mail.outlook.com")
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Look Up\n\nThe ISS is above you in the sky."
        )
