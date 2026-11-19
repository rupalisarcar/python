from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep, time

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)
driver.get("https://ozh.github.io/cookieclicker/")

sleep(3)

select_language = driver.find_element(By.ID, value="langSelect-EN")
print("Langulage selected")
select_language.click()
sleep(3)

cookie = driver.find_element(By.ID, value="bigCookie")

wait_time = 5
time_out= time() + wait_time
print(time_out)
five_min= time()+60*5
print(five_min)
while True:
    cookie.click()

    if time() > time_out:
        try:
            cookies_title = driver.find_element(By.ID, value="cookies")
            cookie_num = int(cookies_title.text.split(' ')[0])
            print(cookie_num)

            # Find all available products in the store
            products = driver.find_elements(by=By.CSS_SELECTOR, value="div[id^='product']")
            print(products)
            print(len(products))
        
            best_item = None
            for product in reversed(products):
                # Check if item is available and affordable (enabled class)
                if "enabled" in product.get_attribute("class"):
                    best_item = product
                    break

            # Buy the best item if found
            if best_item:
                best_item.click()
                print(f"Bought item: {best_item.get_attribute('id')}")

        except (NoSuchElementException, ValueError):
                    print("Couldn't find cookie count or items")
        
        # Reset timer
        time_out = time()+wait_time

    if time() > five_min:
        try:
            cookies_title = driver.find_element(By.ID, value="cookies")
            cookie_num = int(cookies_title.text.split(' ')[0])
            print(f"Cookies/second : {cookie_num}")
            
        except NoSuchElementException:
            print("Couldn't get final cookie count")             
        break
