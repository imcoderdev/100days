from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def first_message():
    return '''
    <h1 style="text-align:left;">GUESS THE NUMBER B/W 0 TO 9</h1>
    <img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />
    '''



@app.route('/<int:no>')
def user_input_more(no):
    number=random.randint(0,9)
    print(number)
    if no>9:
            return '''
                       <h1 style="text-align:left;">Number out of range!!</h1>
                       <img src="https://media1.tenor.com/m/edUPIhhDnO4AAAAd/neil-primrose-travis.gif" />
                       '''
    elif number>no:
        return '''
            <h1 style="text-align:left;">Too small!</h1>
            <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExbTUwdXYzM2FmODJpbTVqdGs4YndtdGZ1bGE4OGh5cjl2OXN6a2x3YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/14pKVNqXY40EVi/giphy.gif" />
            '''
    elif number==no:
        return '''
                   <h1 style="text-align:left;">You guessed it correct!</h1>
                   <img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />
                   '''

    elif number<no:
        return '''
                   <h1 style="text-align:left;">Too big!</h1>
                   <img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />
                   '''




if __name__ == "__main__":
    app.run(debug=True)