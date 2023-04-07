from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Replace with the path to your chromedriver executable
driver = "/drivers/chromedriver.exe"

# Replace with the URL of the website you want to log in to
login_url = "************"
updates_url = "************"

# Replace with your login credentials
username = "user"
password = "pass"

# Launch Chrome browser using chromedriver
driver = webdriver.Chrome(driver)

# Navigate to login page
driver.get(login_url)

# Locate username and password fields by name, ID or CSS selector
username_field = driver.find_element(By.NAME,"LoginForm[email]")
password_field = driver.find_element(By.NAME,"LoginForm[password]")

# Enter username and password
username_field.send_keys(username)
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

#Go to click on the page for updating the post
time.sleep(5)
while True:
    driver.get(updates_url+f"?page=3")
    upd_date = driver.find_element(By.CLASS_NAME,'updt-date')
    upd_date.click()
    driver.refresh()
    driver.get(updates_url+f"?page=3")
    time.sleep(61)

