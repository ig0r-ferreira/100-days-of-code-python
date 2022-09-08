import pandas as pd
from datetime import datetime
import smtplib
import os
import random


SMTP_SERVER_ADDRESS: str = "smtp.mailtrap.io"
PORT: int = 587
USERNAME: str = "xxxxxxxxxxxxxx"
PASSWORD: str = "xxxxxxxxxxxxxx"
SENDER_EMAIL: str = "Private Person <from@example.com>"

BIRTHDAYS_CSV_FILE_PATH: str = "birthdays.csv"
LETTER_TEMPLATES_PATH: str = "letter_templates/"


def get_todays_birthdays() -> list[dict]:
    birthdays_df = pd.read_csv(BIRTHDAYS_CSV_FILE_PATH)
    today = datetime.today().date()
    is_birthday_today = f"month == {today.month} and day == {today.day}"

    return pd.DataFrame(birthdays_df.query(is_birthday_today)).to_dict(orient="records")


def send_email(to, subject, msg) -> None:
    with smtplib.SMTP(SMTP_SERVER_ADDRESS, PORT) as server:
        server.starttls()
        server.login(user=USERNAME, password=PASSWORD)
        server.sendmail(
            from_addr=SENDER_EMAIL,
            to_addrs=to,
            msg=f"From: {SENDER_EMAIL}\n"
                f"To: {to}\n"
                f"Subject: {subject}\n\n"
                f"{msg}"
        )


def get_random_template() -> str:
    template_name = random.choice(os.listdir(LETTER_TEMPLATES_PATH))
    with open(f"{LETTER_TEMPLATES_PATH}{template_name}", encoding="utf-8") as file:
        return file.read()


def main() -> None:
    birthdays = get_todays_birthdays()
    if len(birthdays) > 0:
        for birthday_person in birthdays:
            letter_template = get_random_template()
            birthday_wishes = letter_template.replace("[NAME]", birthday_person["name"].title())

            send_email(to=birthday_person["email"], subject="Happy Birthday!", msg=birthday_wishes)

            print(f"Email successfully sent to {birthday_person['email']}.")
    else:
        print("No birthdays today!")


if __name__ == "__main__":
    main()
