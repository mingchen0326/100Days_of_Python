import smtplib

my_email = "mingchen218@hotmail.com"
password = "youcan159777"

connection = smtplib.SMTP("smtp.live.com", port=587)
# starttls secures the connection, and encrypt the email content
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="mingchen0321@gmail.com", msg="Hello")
connection.close()
