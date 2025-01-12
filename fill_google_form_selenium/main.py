import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests

response=requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_text=response.text
soup=BeautifulSoup(web_text, "html.parser")
# print(soup)
link=soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
# ***********************************links***********************************
zillo_link=[]
for links in link:
    z_link=links.get("href")
    zillo_link.append(z_link)
# print(zillo_link)
# ****************************************************************************************
price=soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
# print(price.text.replace("+/mo", ""))
actual_price=[]
for prices in price:
    price_=prices.text.replace("+/mo", "")
    cleaned_price = price_.replace('/mo', '').replace('+ 1 bd', '').replace('+ 1bd', '')
    actual_price.append(cleaned_price)
# print(actual_price)
# ****************************************************************************************
address=soup.find_all(name="address")
actual_address=[]

for addresses in address:
    cleaned_address=(addresses.text.replace("\n ","").replace("\n","").strip())
    actual_address.append(cleaned_address)
# print(actual_address)


# *******************************web scrapping**************************************

google_form_link="https://docs.google.com/forms/d/e/1FAIpQLSc8n_42_MdojPOxxGm0AK-WB6nuqDTcdlkRAHBlYOFsCkjxJg/viewform?usp=header"

PATH="C:/Users/ASUS/PycharmProjects/capstone_selenium/chromedriver.exe"
chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get(google_form_link)



assert len(actual_address)==len(actual_price)==len(zillo_link)
for address,price,link in zip(actual_address,actual_price,zillo_link):
    # driver.execute_script("arguments[0].scrollIntoView();", what_address)
    what_address = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    what_price = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    what_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input'))
    )
    click_submit = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        )
    )
    driver.execute_script("arguments[0].scrollIntoView();", what_address)
    what_address.send_keys(address)
    # time.sleep(2)
    what_price.send_keys(price)
    # time.sleep(2)
    what_link.send_keys(link)
    # time.sleep(2)
    click_submit.click()
    # time.sleep(4)
    click_new = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        )
    )

    click_new.click()



driver.get("https://docs.google.com/forms/d/1BkCZHhhCygucwoEfeBqLjHRYPEg-uvGsGI-sb7CRcOY/edit#responses")
click_link_tp_sheets=driver.find_element(By.XPATH,'//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div/span/span[2]')
click_link_tp_sheets.click()








