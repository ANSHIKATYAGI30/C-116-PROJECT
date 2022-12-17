# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# default route or 'URL'
@app.route("/me")
def home():

    name = "Anshikaaa" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route('/father')
def father():
    name = "Kuldeep"
    age = '42'

    return render_template('father.html', name=name, age=age)


@app.route('/mother')
def father():
    name = "Shweta"
    age = '43'

    return render_template('mother.html', name=name, age=age)

@app.route('/friend')
def father():
    name = "Unnati"
    age = '16'

    return render_template('friend.html', name=name, age=age)


# run the file
if __name__  ==  '__main__':
  app.run(debug=True)
