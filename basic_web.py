from flask import Flask, render_template, url_for
app = Flask(__name__) # this gets the name of the file so Flask knows it's name
@app.route("/") # this tells you the URL the method below is related to
@app.route("/home")
@app.route("/second_page")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')
@app.route("/second_page")
def second_page():
    return render_template('second_page.html', subtitle='Second Page', text='This is the second page')
#this code to pass manual enviroment variable setting
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")