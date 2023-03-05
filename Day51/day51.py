from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

# environment variable
load_dotenv(".env")

provider_down = 100
provider_up = 50

class InternetSpeedTweetterBot():

    def __init__(self, provider_down, provider_up):
        # load firefox webdriver
        self.chrome_driver_path = r"C:\Users\m_j21\Desktop\Git\geckodriver.exe"
        self.driver = webdriver.Firefox(executable_path=self.chrome_driver_path)
        self.provider_down = provider_down
        self.provider_up = provider_up
        self.test_down = 0
        self.test_up = 0

    def get_internet_speed(self):
        # Open the speed test web page and click Go button to test webpage# 
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_button.click()

        # wait for internet speed testing 
        time.sleep(30)
        self.test_down = self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text
        self.test_up = self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text

        return self.test_down, self.test_up

    def login_twitter(self, email, password):
        self.driver.get("https://twitter.com/home")

        # Enter username
        username_input = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
        time.sleep(2)
        username_input.send_keys(email)

        # Click Next button
        next_button = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]')
        next_button.click()

        # Enter Password
        password_input = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        time.sleep(2)
        password_input.send_keys(password)

        # Click Next button
        login_button = self.driver.find_element(By.XPATH, value='/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
        login_button.click()
    
    def tweet_internet_provider(self, message):
        # Enter message into tweet message box
        tweet_msg_box = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        tweet_msg_box.send_keys(message)

        # Post tweet by click "Tweet" button
        tweet_button = self.driver.find_element(By.XPATH, value='/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div/div/span/span')
        tweet_button.click()

tweeterBot = InternetSpeedTweetterBot()
test_down, test_up = tweeterBot.get_internet_speed()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
tweeterBot.login_twitter(email, password)
message = f"I was promised {provider_down} m/s download speed and {provider_up} m/s upload speed, but I only get {test_down} m/s and {test_up} m/s"
tweeterBot.tweet_internet_provider(message)