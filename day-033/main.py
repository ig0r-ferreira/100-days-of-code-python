import time
import requests
import smtplib
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from dotenv import dotenv_values


config = dotenv_values(".env")

SMTP_SERVER_ADDRESS: str = config["SMTP_SERVER_ADDRESS"]
SMTP_SERVER_PORT: int = int(config["SMTP_SERVER_PORT"])
USERNAME: str = config["EMAIL_USERNAME"]
PASSWORD: str = config["EMAIL_PASSWORD"]
SENDER_EMAIL: str = config["SENDER_EMAIL"]
RECIPIENT_EMAILS: list[str] = config["RECIPIENT_EMAILS"].split(";")


def get_iss_coordinates() -> dict[str, float]:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    iss_position = response.json()["iss_position"]

    return {"lat": float(iss_position["latitude"]), "lng": float(iss_position["longitude"])}


def is_iss_overhead(lat: float, lng: float) -> bool:
    iss_coordinates: dict[str, float] = get_iss_coordinates()
    return abs(iss_coordinates["lat"] - lat) <= 5 and abs(iss_coordinates["lng"] - lng) <= 5


def is_night(lat: float, lng: float) -> bool:
    response = requests.get(url="https://api.sunrise-sunset.org/json", params={
        "lat": lat,
        "lng": lng,
        "formatted": 0
    })
    response.raise_for_status()
    results = response.json()["results"]

    sunset = datetime.fromisoformat(results["sunset"])
    sunrise = datetime.fromisoformat(results["sunrise"])
    now = datetime.now(timezone.utc)

    return now >= sunset or now <= sunrise


def send_email(to: list[str]) -> None:
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = ",".join(to)
    msg["Subject"] = "ISS is passing now 🛰️🌃"
    html = f"""\
        <body style="text-align:center; font-family:Arial; font-size:28px; margin-top:30px;">
            <p>Look up! ☝</p>
            <br>
            <img src="cid:gif">
        </body>
    """

    html_content = MIMEText(html, "html")
    msg.attach(html_content)

    img_path = "look-up.gif"
    with open(img_path, "rb") as file:
        img = MIMEImage(file.read())

    img.add_header('Content-ID', '<gif>')
    img.add_header('Content-Disposition', 'inline', filename=img_path)
    msg.attach(img)

    with smtplib.SMTP(SMTP_SERVER_ADDRESS, SMTP_SERVER_PORT) as server:
        server.starttls()
        server.login(user=USERNAME, password=PASSWORD)
        server.sendmail(from_addr=SENDER_EMAIL, to_addrs=to, msg=msg.as_string())


def main() -> None:
    my_coordinates = {
        "lat": -12.254806,
        "lng": -38.965541
    }

    while True:
        time.sleep(60)
        if is_night(**my_coordinates) and is_iss_overhead(**my_coordinates):
            send_email(to=RECIPIENT_EMAILS)


if __name__ == "__main__":
    main()
