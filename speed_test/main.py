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
        self.driver.get("https://x.com/home")
        time.sleep(5)
        sign_up = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[4]/a')
        sign_up.click()
        time.sleep(3)
        email_ = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email_.send_keys(self.EMAIL, Keys.ENTER)
        time.sleep(3)
        username = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        username.send_keys(self.USERNAME, Keys.ENTER)
        time.sleep(3)
        password = self.driver.find_element(By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
        password.send_keys(self.PASSWORD, Keys.ENTER)
        time.sleep(3)
        write = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        write.send_keys(f"what is these @vi why my internet speed is {self.up} and {self.down}", Keys.ENTER)
        time.sleep(2)
        post = self.driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/button/div/span/span')
        post.click()

bot = InternetSpeedTwitterBot(DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()
