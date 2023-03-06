from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import os
import time


class InsFollowBot:

    def __init__(self):
        self.ser = Service(r"C:\Users\m_j21\Desktop\Git\geckodriver.exe")
        # self.firefox_driver_path = r"C:\Users\m_j21\Desktop\Git\geckodriver.exe"
        self.driver = webdriver.Firefox(service=self.ser)
        self.username = None
        self.password = None
        self.login = None

    def instagram_login(self):
        # open Instagram web page
        self.driver.get("https://www.instagram.com/")

        # enter username, password and login
        time.sleep(3)
        self.username = self.driver.find_element(By.CSS_SELECTOR, value="div._ab32:nth-child(1) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)")
        self.username.send_keys(os.environ['EMAIL'])
        self.password = self.driver.find_element(By.NAME, value="password")
        self.password.send_keys(os.environ['PASSWORD'])
        self.login = self.driver.find_element(By.CSS_SELECTOR, value="div._abak:nth-child(3)")
        self.login.click()

        # click button: no save personal info and no notification
        time.sleep(3)
        no_save = self.driver.find_element(By.CSS_SELECTOR, value="button._acan:nth-child(1)")
        no_save.click()
        time.sleep(2)
        no_notification = self.driver.find_element(By.CSS_SELECTOR, value="button._a9--:nth-child(2)")
        no_notification.click()
        time.sleep(3)

    def add_nasa_follower(self):
        nasa_page = self.driver.find_element(By.LINK_TEXT, value="nasa")
        nasa_page.click()
        time.sleep(2)

        # open the follower window
        see_followers = self.driver.find_element(By.CSS_SELECTOR, value="li.xl565be:nth-child(2) > a:nth-child(1) > div:nth-child(1)")
        see_followers.click()

        time.sleep(2)
        # start click on "Follow" button
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, value="button._acan._acap._acas._aj1-")
        for button in follow_buttons:
            button.click()


insFollowBot = InsFollowBot()
insFollowBot.instagram_login()
insFollowBot.add_nasa_follower()
