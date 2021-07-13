# from flask import Flask, render_template, url_for, flash, redirect
# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField, BooleanField
# from wtforms.validators import DataRequired, Length, Email, EqualTo
# import secrets
# from forms import RegistrationForm
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__) # this gets the name of the file so Flask knows it's name
# app.config['SECRET_KEY'] = '691516e90a6d7a1a30aede7a18e0c82d'

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# db = SQLAlchemy(app)

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(20), unique=True, nullable=False)
#   email = db.Column(db.String(120), unique=True, nullable=False)
#   password = db.Column(db.String(60), nullable=False)

#   def __repr__(self):
#     return f"User('{self.username}', '{self.email}')"
  
    
# @app.route("/") # this tells you the URL the method below is related to



  

# # @app.route("/second_page")
# # def second_page():
# #     return render_template('second_page.html', subtitle='Second Page', text='This is the second page')
# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():# checks if entries are valid
#         user = User(username=form.username.data, email=form.email.data, password=form.password.data)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home')) # if so - send to home page
#         return render_template('register.html', title='Register', form=form)

# @app.route("/home")     
# def home():
#     return render_template('home.html', subtitle='Home Page', text='This is the home page') 
# @app.route("/about")
# def about():
#     return render_template('about.html', subtitle='About Page')
# #this code to pass manual enviroment variable setting
# if __name__ == '__main__':
#     app.run(debug=True, host="0.0.0.0")

from flask import Flask, render_template, url_for, flash, redirect # allow rendering of html code rather than printing it raw
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#import secrets
from forms import RegistrationForm
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name
app.config['SECRET_KEY'] = '07a23504284a9c906b04ca2b83fa0db5' # be sure to use only the most recent key generated
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(60), nullable=False)
  
  def __repr__(self):
    return f"User('{self.username}', '{self.email}')"

@app.route("/")                          # this tells you the URL the method below is related to
# def hello_world():
#     return "<p>Hello, SEO Tech Developers!</p>"        # this prints HTML to the webpage

# # Let’s add an About page to our simple website.
# # First, pick the URL you want the page to be at – for example, website.com/about is pretty standard:
# @app.route("/about")
# def about():
#     return "<p>About SEO!</p>"

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle='About Page')




if __name__ == '__main__':               # this should always be at the end avoids the need for environment variables
    app.run(debug=True, host="0.0.0.0")

#to run set environment variable:export FLASK_APP=demo unless you can use the command above
