from bs4 import BeautifulSoup
import requests

response=requests.get(url="https://news.ycombinator.com/news")
yc_text=response.text

soup = BeautifulSoup(yc_text,"html.parser")
# print(soup)
anchor=(soup.find_all(name="span",class_="titleline"))
# get_a = anchor.find_all(name="a")
article=[]
link=[]
for anchor_tag in anchor:
    article_text=anchor_tag.getText()
    article.append(article_text)
    get_a = anchor_tag.find(name="a")
    if get_a:
        article_link = get_a.get("href")
        link.append(article_link)


number=[int(score.getText().split()[0]) for score in soup.find_all(name="span",class_="score")]
largest_number=max(number)
largest_number_index=number.index(largest_number)
print(largest_number_index)
print(article[largest_number_index])
print(link[largest_number_index])
# print(article)
# print(link)
# print(number)





















# with open("website.html") as file:
#     contents=file.read()
#
# soup=BeautifulSoup(contents,"html.parser")
#
# all=soup.find_all(name="a")
# print(all)
# for text in all:
#     print(text.getText())

