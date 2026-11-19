from selenium import webdriver
from selenium.webdriver.common.by import By

 # create webdriver object first
driver = webdriver.Chrome()
driver.get("https://www.python.org/")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_titles = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
print(event_times[0].text)
print(event_titles[0].text)
event = {}
for n in range(len(event_times)):
    event[n] = {
        "time" : event_times[n].text,
        "title": event_titles[n].text
    }

print(event)

driver.quit()