from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\m_j21\Desktop\Git\geckodriver.exe"
driver = webdriver.Firefox(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# # article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# # article_count.click()

# # all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# # all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie_button = driver.find_element(By.ID, "cookie")
for click in range(1, 100):
    cookie_button.click()
