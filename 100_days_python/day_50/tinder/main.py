from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

URL = "https://app.100daysofpython.dev/services/tindog/u/lqrcigX3x5TcNUdYV50bKcNJdsjfPsEH"
EMAIL = "rupalisarkar12@gmail.com"
PASSWORD = "Sarcar2026"

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)
login_btn = driver.find_element(By.XPATH, value="//*[text()='Log in']")
login_btn.click()

time.sleep(1)
facebark_btn = driver.find_element(By.CSS_SELECTOR, "button[class^='btn-facebark ']")
print(facebark_btn)
facebark_btn.click()

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_email = driver.find_element(By.NAME, value="email")
fb_email.clear()
fb_email.send_keys(EMAIL)

fb_password = driver.find_element(By.NAME, value="pass")
fb_password.clear()
fb_password.send_keys(PASSWORD)

fb_login_btn = driver.find_element(By.TAG_NAME, value="button")
fb_login_btn.click()


time.sleep(1)
driver.switch_to.window(base_window)
print(driver.title)



allow_btn = driver.find_element(By.XPATH, value="//*[text()='Allow']")
allow_btn.click()

time.sleep(1)
enable_btn = driver.find_element(By.XPATH, value="//button[text()='Enable']")
enable_btn.click()

accept_btn = driver.find_element(By.XPATH, value="//button[text()='I Accept']")
accept_btn.click()



for n in range(20):
    time.sleep(1)
    try:
        like_btn = driver.find_element(By.XPATH, value="//button[@class='btn-like']")
        like_btn.click()
    except ElementClickInterceptedException:
        try:
            driver.find_element(By.CSS_SELECTOR, value='.match-popup a').click()
        except NoSuchElementException:
            time.sleep(2)
    except NoSuchElementException:
        time.sleep(2)