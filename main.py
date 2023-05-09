import datetime
import random
import pandas
import smtplib

data = pandas.read_csv("sensitive_data.csv")
# Not forgetting to remove my email this time
my_email = data.email.iloc[0]
password = data.password.iloc[0]
recipient = data.recipient.iloc[0]
SENDER_SMTP = data.sender_smtp.iloc[0]

def send_email(email=my_email, smtp_url=SENDER_SMTP, body="This email sent to you by tuesday python gang"):
    """Takes sending email, SMTP of sender, and email body as parameters."""
    global password, recipient
    rec = recipient
    pw = password
    subject = "Your weekly inspirational quote!"
    with smtplib.SMTP(SENDER_SMTP, port=smtplib.SMTP_PORT) as connection:
        connection.starttls()
        connection.login(user=email, password=pw)
        connection.sendmail(from_addr=email, to_addrs=rec, msg=f"subject:{subject}\n\n{body}")

# Obtain the current day of the week

current_day = datetime.datetime.now()
current_weekday = current_day.weekday()

# get the quotes from quotes.txt

with open("quotes.txt") as quotes_file:
    weekly_quote = random.choice(quotes_file.readlines())

if current_weekday == 1:
    send_email(body=weekly_quote)