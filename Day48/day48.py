from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = r"C:\Users\m_j21\Desktop\Git\geckodriver.exe"
driver = webdriver.Firefox(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.ca/Instant-Pot-6QT-Duo-Plus/dp/B07W55DDFB/ref=sr_1_9?crid=37LCH7BYG116B&keywords=instant+pot&qid=1677811358&sprefix=instant+pot%2Caps%2C119&sr=8-9")
# feedback = driver.find_elements(By.ID, "corePriceDisplay_desktop_feature_div")
# price = feedback[0].text.replace('\n', '.')
# print(price)

# driver.get("https://www.python.org/")
# search_bar = driver.find_elements(By.NAME, "q")

# Challenge to Scrap event from python.org
driver.get("https://www.python.org/")
feedback = driver.find_elements(By.XPATH, "/html/body/div/div[3]/div/section/div[2]/div[2]/div/ul")[0].text
upcoming_event = feedback.split("\n")
print(len(upcoming_event)/2)
event = {}

for row in range(0, int(len(upcoming_event)/2)):
    event[row] = {upcoming_event[row]: upcoming_event[row+1]}

print(event)
driver.close()