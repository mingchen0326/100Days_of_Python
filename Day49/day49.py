from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

chrome_driver_path = r"C:\Users\m_j21\Desktop\Git\geckodriver.exe"
driver = webdriver.Firefox(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/")

# environment variable
load_dotenv()

username = driver.find_element(By.ID, "session_key")
username.send_keys(os.getenv("EMAIL"))
password = driver.find_element(By.ID, "session_password")
password.send_keys(os.getenv("PASSWORD"))
sign_in = driver.find_element(By.CSS_SELECTOR, "button.btn-md:nth-child(3)")
sign_in.click()

job_input = driver.find_element(By.CSS_SELECTOR, "#jobs-search-box-keyword-id-ember23")
job_input.send_keys("chemical Engineer")
job_input.send_keys(Keys.ENTER)
# location_input = driver.find_element(By.CSS_SELECTOR, '[aria-label="City, state, or zip code"]')
# location_input.send_keys("hamilton, ON")

time.sleep(3)
easy_apply = driver.find_element(By.CSS_SELECTOR, '[aria-label="Easy Apply filter."]')
easy_apply.click()

apply_button = driver.find_element(By.CLASS_NAME, "artdeco-button__text")
apply_button.click()

driver.close()