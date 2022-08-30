from bs4 import BeautifulSoup
import requests
import email
import smtplib

product_url = "https://www.amazon.ca/Instant-Pot-6QT-Duo-Plus/dp/B07W55DDFB/ref=sr_1_1?crid=39LY51YOXJ1Z6&keywords=Instant+Pot+Duo+Evo+Plus+10-in-1+Pressure+Cooker&qid=1661826156&sprefix=instant+pot+duo+evo+plus+10-in-1+pressure+cooker%2Caps%2C439&sr=8-1"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
accept_language = "en-US,en;q=0.5"
response = requests.get(product_url, headers={"User-Agent": user_agent, "Accept-Language":accept_language}).text

soup = BeautifulSoup(response, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()[1:]
price = float(price)

target_price = 150

msg = email.message_from_string('this is a test email')
msg['From'] = "mingchen2189@hotmail.com"
msg['To'] = "mingchen0321@gmail.com"
msg['Subject'] = "Test email"

s = smtplib.SMTP("smtp.live.com", 587)
s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
s.starttls() #Puts connection to SMTP server in TLS mode
s.ehlo()
s.login('mingchen2189@hotmail.com', 'youcan159777')

s.sendmail("mingchen2189@hotmail.com", "mingchen0321@gmail.com", msg.as_string())

s.quit()