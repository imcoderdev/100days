import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

LINKEDIN_EMAIL="mistyraju0@gmail.com"
LINKEDIN_PASSWORD="Namdev@123"

chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4117276611&f_LF=f_AL&geoId=102257491&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")
# time.sleep(4)

google_button = driver.find_element(By.XPATH, '//*[@id="base-contextual-sign-in-modal"]/div/section/div/div/div/div[2]/button')
google_button.click()
# time.sleep(5)
# *******************************login*****************************
username_button=driver.find_element(By.ID,"base-sign-in-modal_session_key")
username_button.click()
username_button.send_keys(LINKEDIN_EMAIL,Keys.ENTER)
username_pass=driver.find_element(By.ID,"base-sign-in-modal_session_password")
username_pass.click()
username_pass.send_keys(LINKEDIN_PASSWORD,Keys.ENTER)
# ***********************************************click easy apply***************************************
time.sleep(5)
click_apply=driver.find_element(By.ID,"ember54")
click_apply.click()
click_next=driver.find_element(By.XPATH,"//button[@aria-label='Continue to next step']")
click_next.click()
click_next=driver.find_element(By.XPATH,"//button[@aria-label='Continue to next step']")
click_next.click()
# ***********************************Enter experince**************************************
first_input=driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175122-numeric")
first_input.click()
first_input.send_keys("0",Keys.ENTER)
second_input=driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175130-numeric")
# second_input.click()
second_input.send_keys("1",Keys.ENTER)
third_input=driver.find_element(By.ID,"single-line-text-form-component-formElement-urn-li-jobs-applyformcommon-easyApplyFormElement-4117276611-12027175114-numeric")
# third_input.click()
third_input.send_keys("0",Keys.ENTER)
# ********************************************click review and submit application*******************************
click_review=driver.find_element(By.XPATH,"//button[@aria-label='Review your application']")
click_review.click()
click_submit=driver.find_element(By.XPATH,"//button[@aria-label='Submit application']")
click_submit.click()


driver.quit()







