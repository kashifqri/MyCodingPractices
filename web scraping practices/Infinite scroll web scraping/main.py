from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service("C:/Users/basit/Downloads/New folder/chromedriver-win64/chromedriver.exe")
driver=webdriver.Chrome(service=s)

# driver.set_script_timeout(30)



driver.get("https://www.ajio.com/men-flip-flop-slippers/c/830207001")
time.sleep(6)

height=driver.execute_script("return document.body.scrollHeight")
# print(height)
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(3)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if height==new_height:
        break

    height=new_height