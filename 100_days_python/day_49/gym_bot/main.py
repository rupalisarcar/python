from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
import time

ACCOUNT_EMAIL = "rupali@test.com"  # The email you registered with
ACCOUNT_PASSWORD = "rupali1234"      # The password you used during registration
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
print(user_data_dir)
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
# Navigate to site
driver.get(GYM_URL)

wait = WebDriverWait(driver, timeout=2)

def retry(func, retries = 7, description=None):
    for i in range(retries):
        print(f"Trying {description} : {i+1} times")
        try:
            return func()
        except TimeoutError:
            if i == retries - 1:
              raise
            time.sleep(1)

def login():
    home_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Home_heroButton__3eeI3")))
    home_btn.click()

    email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
    email.clear()
    password = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    password.clear()
    email.send_keys(ACCOUNT_EMAIL)
    password.send_keys(ACCOUNT_PASSWORD)

    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "submit-button")))
    login_btn.click()

    wait.until(EC.presence_of_element_located((By.ID, "schedule-page")))

def book_class(booking_button):
    booking_button.click()
    wait.until(lambda d: booking_button.text == "Booked" or booking_button.text == "Waitlisted")

retry(login, description='login')

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
booked_count = 0
already_booked_count = 0
waitlist_count = 0
processed_classes = []

for card in class_cards:
    card_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    card_title = card_group.find_element(By.TAG_NAME, 'h2').text
    time.sleep(1)

    if 'Tue' in card_title or 'Fri' in card_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "Time: 6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text

            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button_text = button.text

            card_info = f"{class_name} on {card_title}"

            if button_text == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                print(f"✓ Joined waitlist: {class_name} on {card_title} 🤗")
                waitlist_count +=1
                processed_classes.append(f"[new Waitlist] {card_info}")

            elif button_text == "Booked":
                already_booked_count +=1
                print(f"✓ Already booked: {card_info} 🤗")
                processed_classes.append(f"[Booked] {card_info}")

            elif button_text == "Book Class":
                # Book the class
                
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Successfully booked: {class_name} on {card_title}")
                booked_count +=1
                # Wait a moment for the button state to update
                processed_classes.append(f"[New Booking] {card_info}")

            else:
                already_booked_count +=1
                print(f"✓ Already on waitlist: {class_name} on {card_title} 🤗")
                processed_classes.append(f"[Waitlisted] {card_info}")

# print("--- BOOKING SUMMARY --- ")
# print(f"New bookings: {booked_count}")
# print(f"New waitlist entries: {waitlist_count}")
# print(f"Already booked/waitlisted: {already_booked_count}")
# print(f"Total Tuesday & Thursday 6pm classes: {booked_count + already_booked_count + waitlist_count}")
total_class = 0
total_class = booked_count + already_booked_count + waitlist_count
print(f"--- Total Tuesday/Thursday 6pm classes: {total_class} ---")

# print("--- DETAILED CLASS LIST ---")
# for process in processed_classes:
#     print(process)

def get_my_bookings():
    booking_page_btn = driver.find_element(By.ID, "my-bookings-link")
    booking_page_btn.click()

    wait.until(EC.presence_of_element_located((By.ID,"my-bookings-page")))

    booking_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
    if not booking_cards:
        raise TimeoutException("No booking cards found - page may not have loaded")
    else:
        return booking_cards
    
verified_count = 0

all_cards = retry(get_my_bookings, description="Get my Bookings")

for card in all_cards:
    try:
        when_card = card.find_element(By.XPATH,".//p[strong[text()='When:']]")
        when_card_text=when_card.text
        print(when_card_text)
        if ('Fri' in when_card_text or 'Tue' in when_card_text) and '6:00 PM' in when_card_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(class_name)
            print(f"  ✓ Verified: {class_name}")
            verified_count+=1
    except NoSuchElementException:
        pass

print("--- VERIFICATION RESULT ---")
print(f"Expected : {total_class} bookings")
print(f"Found : {total_class} bookings")
if total_class == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing -{total_class-verified_count} bookings")