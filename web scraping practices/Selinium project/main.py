from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


__path__ = "C:/Users/basit/Downloads/New folder/chromedriver-win64/chromedriver.exe"

s = Service(__path__)

driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com/")
box = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
box.send_keys("House of Dragon")
box.send_keys(Keys.ENTER) 


box = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[13]/div[4]/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div[3]/div[8]/div/div/div/div/div/div[1]/div/div/span/a/h3").click()
driver.save_screenshot("C:/Users/basit/Downloads/Selinium project/dragon1.png")
