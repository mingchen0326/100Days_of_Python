from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import requests
import time
import os

req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

zillow_url = os.environ.get("ZILLOW_LINK")
response = requests.get(zillow_url, headers=req_headers)
web_content = response.text
soup = BeautifulSoup(web_content, "html.parser")
a_tag = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")
div_tag = soup.find_all(name="div", class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 bqsBln")
href_tag = soup.find_all(name="a", class_="StyledPropertyCardDataArea-c11n-8-85-1__sc-yipmu-0 gdfTyO property-card-link")

houses = []
link = None

for address, price, url in zip(a_tag, div_tag, href_tag):
    if url['href'].startswith("https"):
        link = url['href']
    else:
        link = "https://www.zillow.com" + url['href']
    houses.append(
        {'address': address.getText(),
         'price': price.getText(),
         'url': link}
    )

# access firefox webdriver
ser = Service(r"C:\Users\m_j21\Desktop\Git\geckodriver.exe")
driver = webdriver.Firefox(service=ser)
driver.get(os.environ.get("GOOGLE_FORM_LINK"))
time.sleep(2)

for house in houses:
    address_input = driver.find_element(By.CSS_SELECTOR,
                                        value="div.Qr7Oae:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    price_input = driver.find_element(By.CSS_SELECTOR,
                                      value="div.Qr7Oae:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    link_input = driver.find_element(By.CSS_SELECTOR,
                                     value="div.Qr7Oae:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)")
    submit_button = driver.find_element(By.CSS_SELECTOR, value=".Y5sE8d > span:nth-child(3) > span:nth-child(1)")

    address_input.send_keys(house['address'])
    price_input.send_keys(house['price'])
    link_input.send_keys(house['url'])
    submit_button.click()
    another_response = driver.find_element(By.CSS_SELECTOR, value=".c2gzEf > a:nth-child(1)")
    another_response.click()
    time.sleep(1)
