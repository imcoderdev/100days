import datetime
from pickletools import read_stringnl
from venv import create
import requests
import datetime
# *************************************create account on pixela************************************
pixela_endpoint="https://pixe.la/v1/users"
TOKEN="ahfwae8uhuiehgws89"
USERNAME="dev007"
GRAPH_ID="first1"
user_params={
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
response=requests.post(url=pixela_endpoint,json=user_params)
print(response.text)
# **************************************create_graph*****************************************
graph_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id":GRAPH_ID,
    "name":"book reading",
    "unit":"min",
    "type":"int",
    "color":"ajisai",
}
header={
    "X-USER-TOKEN":TOKEN
}
response=requests.post(url=graph_endpoint,json=graph_config,headers=header)
print(response.text)

# ********************************create_pixel*****************************
now = datetime.datetime.now()
print(now.strftime("%Y%m%d"))

pixel_endpoint=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_config={
    "date":now.strftime("%Y%m%d"),
    "quantity":input("How much minutes you red book?:  "),
}
response=requests.post(url=pixel_endpoint,json=pixel_config,headers=header)
print(response.text)

# *****************************put(update_pixel)****************************************

update_pixel=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now.strftime('%Y%m%d')}"
update_config={
    "quantity":"120",
}

response=requests.put(url=update_pixel,json=update_config,headers=header)
print(response.text)

# *********************************delete_pixel**************************************
delete_pixel=f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{now.strftime('%Y%m%d')}"
response=requests.delete(url=delete_pixel,json=update_config,headers=header)
print(response.text)