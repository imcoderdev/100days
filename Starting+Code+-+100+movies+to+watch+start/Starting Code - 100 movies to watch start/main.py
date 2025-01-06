from http.client import responses

import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response=requests.get(URL)
movies_text=response.text
soup=BeautifulSoup(movies_text,"html.parser")
find_name=soup.find_all(name="h3",class_="title")
movie_title=[movie.getText() for movie in find_name]
movie=movie_title[::-1]
with open("movies.txt",mode="w",encoding="utf-8") as file:
    for movies in movie:
        file.write(f"{movies}\n")