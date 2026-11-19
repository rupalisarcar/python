from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://appbrewery.github.io/fake-newsletter-signup/")
fName = driver.find_element(By.NAME, value="fName")
lName = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
fName.send_keys("Rupali")
lName.send_keys("Sarkar")
email.send_keys("abc@gmail.com")
submit_btn = driver.find_element(By.TAG_NAME, value="button")
submit_btn.click()




