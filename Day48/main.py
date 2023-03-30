from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

## this method has been depreciated.
# chrome_driver_path = r"C:\Users\m_j21\Desktop\GitGithub\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.amazon.ca/Instant-Pot-6QT-Duo-Plus/dp/B07W55DDFB/ref=sr_1_1?crid=1FZX7CRO47D8K&keywords=Instant+Pot+Duo+Evo+Plus+10-in-1&qid=1661904473&sprefix=instant+pot+duo+evo+plus+10-in-1%2Caps%2C76&sr=8-1")
element = driver.find_element(By.ID, "apex_desktop_newAccordionRow")
element = element.text.split("\n")
price = float(element[0][1:] + "." + element[1])
print(f"the price is {price}")

# close only close particular tab, driver.quit() will close the entire brower
driver.quit()