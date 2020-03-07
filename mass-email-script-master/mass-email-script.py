import smtplib, ssl
import csv

sender_email = "SENDER_EMAIL@EMAIL.COM"
# password = "SECRET PASSWORD"
password = input("Enter password: ")

server = smtplib.SMTP("smtp.gmail.com", 587)

server.starttls()
server.login(sender_email, password)

msg = """
Hi {first_name},
"""

subject = "EMAIL SUBJECT HERE"
body = "Subject: {}\n\n{}".format(subject, msg)

with open("email-list.csv") as file:
    reader = csv.reader(file)
    next(reader) #skip header row
    for first_name,last_name,email in reader:
        print(f"Sending email to {first_name}")
        server.sendmail(
                sender_email,
                email,
                body.format(first_name = first_name)
            )

server.quit