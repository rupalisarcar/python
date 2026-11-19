from selenium import webdriver
from selenium.webdriver.common.by import By

#keep Chrome browser open after program finishes
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
 
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

articles = driver.find_element(By.ID, value="mwDw")
print(articles.text)

driver.quit()

