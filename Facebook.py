'''
Created on 05-Feb-2020

@author: GokulaKrishnanSengod
'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

# Step 1) Open Google Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:\Workspace\PyCharm\Development\Selenium\Selenium-git\drivers\chromedriver.exe")
# Step 2) Navigate to Facebook
driver.get("http://www.facebook.com")
# Step 3) Search & Enter the Email or Phone field & Enter Password
username = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
submit = driver.find_element_by_id("loginbutton")
username.send_keys("gokulsen@hotmail.com")
password.send_keys("")
# Step 4) Click Login
submit.click()
wait = WebDriverWait(driver, 5)
print(driver.title)
driver.close()
driver.quit()
print("Test Completed 10 Feb 2020, 07:00 PM")
