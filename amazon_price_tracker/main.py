import os
import smtplib
from turtledemo.penrose import start

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
load_dotenv()
Email= os.environ["MY_MAIL"]
PASSWORD=os.environ["MY_PASSWORD"]
URL="https://www.amazon.in/Lava-Segments-Secondary-Dimensity-Processor/dp/B0DNMJQQV1/ref=sr_1_1_sspa?sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY"
response=requests.get(URL,headers=({"Accept-Language":"en-US,en;q=0.9"}))
az=response.text
soup=BeautifulSoup(az,"html.parser")
# print(soup)
product_name=soup.find(id="productTitle").getText().strip()
title=product_name
print(title)
find_price=soup.find(name="span",class_="a-price-whole")
price_now=find_price.text.replace(",","").split(".")[0]
price=float(price_now)
print(price)
if price<17000:

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=Email,password=PASSWORD)
        connection.sendmail(
            from_addr=Email,
            to_addrs="mistyraju0@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\nProduct={title},\ncurrent price:{price},\nlink for the product:{URL}".encode("utf-8")
        )
