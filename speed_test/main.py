import time
from sys import executable

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
DRIVER_PATH = ("C:/XboxGames/100days/PythonProject/speed_test/chromedriver.exe")

class InternetSpeedTwitterBot:
    def __init__(self,chrome_driver_path):
        self.up = 10
        self.down=150
        self.upload=0
        self.download=150
        self.driver=webdriver.Chrome()
        self.USERNAME="factt80"
        self.EMAIL="factt80@gmail.com"
        self.PASSWORD="factt@x.com"



    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        continue_=self.driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]')
        continue_.click()
        time.sleep(5)

        go=self.driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()
        time.sleep(60)
        download_speed=self.driver.find_element(By.CLASS_NAME,"download-speed")
        self.down=float(download_speed.text)
        print(self.down)
        upload_speed=self.driver.find_element(By.CLASS_NAME,"upload-speed")
        self.up=float(upload_speed.text)
        print(self.up)


    def tweet_at_provider(self):
        print(self.upload)
        print(self.down)

bot = InternetSpeedTwitterBot(DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()