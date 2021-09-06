from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


LINKEDIN_WEB = "LINKEDIN_WEBSITE"
LINKEDIN_USERNAME = "YOUR_EMAIL"
LINKEDIN_PASSWORD = "YOUR_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"

driver = webdriver.Chrome(r"D:\chromedriver.exe")
driver.get(LINKEDIN_WEB)
driver.maximize_window()

sing_in_button = driver.find_element_by_class_name("cta-modal__primary-btn")
time.sleep(1)
sing_in_button.click()

linkedin_username = driver.find_element_by_id("username")
linkedin_username.send_keys(LINKEDIN_USERNAME)

linkedin_password = driver.find_element_by_id("password")
linkedin_password.send_keys(LINKEDIN_PASSWORD)

sign_in_button = driver.find_element_by_class_name("btn__primary--large")
sign_in_button.click()

available_jobs = driver.find_elements_by_class_name("jobs-search-results__list-item")
for job in available_jobs:
    try:
        time.sleep(2)
        easy_apply_button = driver.find_element_by_class_name("jobs-apply-button--top-card")
        easy_apply_button.click()

        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            time.sleep(1)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application skipped")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()
    except NoSuchElementException:
        print("No application found")
        continue
