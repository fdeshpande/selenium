import time
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
path = r"C:\Users\deshp\OneDrive\Desktop\PracticePython projects\PracticePython projects\webdriver automation selenium\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(path)
driver = webdriver.Chrome(service=service,options=chrome_options)

url = "https://quotes.toscrape.com/"
driver.get(url)
driver.maximize_window()
time.sleep(1)
driver.find_element(By.XPATH,'//a[@href="/login"]').click()
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,"#username").click()
time.sleep(1)
user = 0000000000
paswd = "name@123"
driver.find_element(By.CSS_SELECTOR,"#username").send_keys(str(user))
driver.find_element(By.CSS_SELECTOR,"#password").click()
driver.find_element(By.CSS_SELECTOR,"#password").send_keys(paswd)
driver.find_element(By.CSS_SELECTOR,".btn-primary").click()

print("logIn Successful")

driver.close()

