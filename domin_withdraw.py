from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time,sys

btc = "3MUT2imvKa2V4BZ6cBGAfZFeQ5PS9kopdk"


chrome_options = Options()  
chrome_options.binary_location = r"/app/.apt/usr/bin/google-chrome"
# chrome_options.add_argument("--headless")

print("------------------------------------------------------\nDOMINIUMPRO.com BOT || VERSION 1.0 \n------------------------------------------------------\nBY - AHMAD TAHA || CONTACT - ahmadtahaco@gmail.com\n======================================================\n")
print ("\n>> Opening Browser")

#driver = webdriver.Chrome(executable_path="chromedriver.exe",chrome_options=chrome_options)
driver = webdriver.Chrome(chrome_options=chrome_options)
#driver.maximize_window()

driver.get("http://www.dominiumpro.com/index.php")

print (">> Website Opened, Logging in with Bitcoin Address : " + btc)

inputbtc = driver.find_element_by_name("address")
inputbtc.send_keys(btc)
inputbtc.send_keys(Keys.RETURN)

while True:
    driver.get("http://www.dominiumpro.com/index.php")
    driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/form/button').click()

    driver.get("http://www.dominiumpro.com/account.php")

    driver.find_element_by_xpath('/html/body/div/div[2]/div[2]/div/form/button').click()
    print(">> Withdrawn")
    time.sleep(1196)

print(">> Current Claimed : " + str("lol") + " || Total Claimed : " + str("lol"))


