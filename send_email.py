import smtplib
import config
import scrape_kicksonfire
from datetime import datetime
import schedule


def send(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        message = f"Subject: {subject}\n\n{msg}"
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("Email sent.")
    except:
        print("Email failed to send.")


def main():
    date = datetime.now()
    subject = f"Sneaker Updates for {date}"
    msg = scrape_kicksonfire.main()
    send(subject, msg)


while True:
    schedule.every().monday.do(main)
