from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome("C:/Users/Hafid/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://ttsmp3.com/text-to-speech/French/")
# assert "Python" in driver.title
i=97
downloadenbutton=driver.find_element(By.ID,"downloadenbutton")
element=driver.find_element(By.ID,"voicetext")
print(element)
while i<903:
    element.clear()
    key = "on appelle le ticket numero "+str(i)
    element.send_keys(key)
    downloadenbutton.click()
    print(i)
    i=i+1
    time.sleep(5)
assert "No results found." not in driver.page_source
driver.close()