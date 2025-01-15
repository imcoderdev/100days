from http.client import responses

from flask import Flask, render_template
import random
from datetime import datetime
import requests



app = Flask(__name__)


@app.route('/')
def home():

    this_year = datetime.today().year
    random_num=random.randint(1,100)
    return render_template("home.html",num=random_num,year=this_year)

@app.route('/<name>')
def find(name):
    params = {"name": f"{name}"}
    agify_response = requests.get("https://api.agify.io", params=params)
    Agify_age= agify_response.json()["age"]
    genderize_response = requests.get("https://api.genderize.io", params=params)
    genderize_age= genderize_response.json()["gender"]
    return render_template("index.html",age=Agify_age,gender=genderize_age,name=name)

@app.route('/blog/<num>')
def get_blog(num):
    response=requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blog=response.json()
    return render_template("blog.html",blogs=all_blog)


if __name__ == "__main__":
    app.run(debug=True)


