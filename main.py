import smtplib

sender_email = "you@gmail.com"
receiver_emails = ["recipient1@gmail.com","recipient2@gmail.com","recipient3@gmail.com"]

message = f"Subject: insert_subject\n\ninsert_email_body"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, "your_account_id")

for email in receiver_emails:
        server.sendmail(sender_email, email, message)
