import time

from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
USERNAME="abc@gmail.com"
PASSWORD="abcdef"
chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)

driver=webdriver.Chrome(options=chrome_option)

driver.get("https://tinder.com/")

#reject cookies
time.sleep(2)
cookies=driver.find_element(By.XPATH ,'//*[@id="q1029118820"]/div/div[2]/div/div/div[1]/div[2]/button')
cookies.click()
time.sleep(2)

login=driver.find_element(By.LINK_TEXT,'Log in')

login.click()

#login with facebook
time.sleep(1)
facebook_login=driver.find_element(By.XPATH,'//*[@id="q-699262256"]/div/div/div/div[1]/div/div/div[2]/div[2]'
                                            '/span/div[2]/button')
facebook_login.click()
time.sleep(1)

#facebook login window popup
fb_window=driver.window_handles[1]
basewindow=driver.window_handles[0]
driver.switch_to.window(fb_window)

time.sleep(2)
username=driver.find_element(By.ID,"email")
print(username.text)
username.send_keys(USERNAME)
password=driver.find_element(By.NAME,"pass")
password.send_keys(PASSWORD)
submit=driver.find_element(By.NAME,"login")
submit.send_keys(Keys.ENTER)
time.sleep(4)

# authorization=driver.find_element(By.LINK_TEXT,"Continue as Sam")
authorization=driver.find_element(By.CSS_SELECTOR,'div[aria-label="Continue as Sam"]')
authorization.click()


driver.switch_to.window(basewindow)
try:
    verification=driver.find_element(By.ID,"FunCaptcha")
    print("captacha detetced ,solve it manually")
    input("press enter after solving captche")

except Exception as e:
    print("no captcha found")

time.sleep(4)
location_allow=driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Allow"]')

location_allow.click()

time.sleep(3)
notification=driver.find_element(By.CSS_SELECTOR,'button[aria-label="I’ll miss out"]')
notification.click()

time.sleep(5)
#100 LIKES PER DAY ON BASIC PLAN
for i in range(100):
    time.sleep(2)

    try:
        like_button = driver.find_element(By.XPATH, '//button[.//span[text()="Like"]]')
        like_button.click()

        # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value=".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()