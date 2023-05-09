D A Y T H I R T Y T W O
# Overview
The goal of this project was to practice using the smtplib and datetime modules,
in order to send an email with a python script. The scripts checks the day of
the week, and if it is the value assigned to `day_to_send`, chooses a random 
quote from `quotes.txt` to send.

# Lesson Notes
## Email SMTP and the datetime module

## project goal:
* send email using python code, using datetime module to determine when to send
* automate happy birthday email

### automated birthday wisher
* start with spreadsheet of birthdays
* choose a random template to send happy birthday

# What's email SMTP?
* a standard library module that makes it easy to send email with python
``` import smptplib```
*  ## potential error:
  * `connection unexpectedly closed`
* make sure you have the correct smtp address


| Provider | SMTP Adress |
|----------|-------------|
| Gmail    | smtp.gmail.com |
| Hotmail  | smtp.live.com |
| Outlooks | outlook.office365.com |
| Yahoo    | smtp.mail.yahoo.com |

## Gmail fixes:
1. Enable less secure apps if sending `from` a gmail account
2. attempt Gmail captcha while logged in to the Gmail account:
   * https://accounts.google.com/DisplayUnlockCaptcha
3. Add a port number: `"smtp.gmail.com, port=587`


# what's datetime?
* another module that helps us figure out the date
* how to format it
* is today `day of particular event`?

# How Does Email Work?
* sender -> recipient
* Sender Mail Server receives sent message, Receiver Mail Server stores message until 
recipient logs in to read it
`SMTP = Simple Mail Transfer Protocol`
# import smtplib

* create a SMTP object: `obj_name = smtplib.SMTP(host=str)`
* {email} @ {provider}

# TLS - Transport Layer Security

* a way of securing connection to email server. if email is intercepted, message
will be encrypted
* `obj_name.starttls()`
* login: `obj_name.login(user=email, password=pw)`
* send: `connection.sendmail(from_addr=, to_addrs=, msg=)`
* close connection: `connection.close()`
  * use with to avoid manual closing

* gmail no longer allows the use of less secure apps, so we must also 
import the gmail module and use MIMEText
* will create a MIMEText object called email_message
  * `email_message = email.MIMEText()`

* Do you have to use SMTP_SSL() ? 
* I don't know, but I did.
* I had to make an app password
* BUT it went to spam

# Reduce Spam Positives
* Add a subject:
  * `msg="subject: Hello\n\nThis is the email body`

# import datetime
* getting the date from the computer
* use the datetime class:
  * datetime.datetime()
  * use the now() method to get time
    * `datetime.datetime.now()`
* datetime() class has attributes for year, month, day, hour, minutes, etc

## Create a datetime object
* date_of_birth = dt.datetime(year=, month=, day=)
# Project Goal:
1. Use the datetime module to obtain the current day of the week.
2.  Open `quotes.txt` and obtain a list of quotes
3. use the random module to pick a random quote
4. use smtplib to send the email
