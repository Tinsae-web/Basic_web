from flask import Flask, render_template, url_for, flash, redirect # allow rendering of html code rather than printing it raw
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
#import secrets
from forms import RegistrationForm
from contact_form import ContactForm
from flask_sqlalchemy import SQLAlchemy
from audio import printWAV
import time, random, threading
from turbo_flask import Turbo
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

interval=10
FILE_NAME = "Break Bad Habits.wav"
turbo = Turbo(app)

@app.route("/") # this tells you the URL the method below is related to


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
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form_contact = ContactForm()
    if form_contact.validate_on_submit():
        user = User(username=form_contact.username.data, email=form_contact.email.data, message=form_contact.message.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form_contact.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('contact.html', title='Contact', form_contact=form_contact)

@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page')

@app.route("/about")
def about():
    return render_template('about.html', subtitle="This is Tinsae's web, you can message Tinsae through contact, also there is a resume page you can look on it. \nFull name: Tinsae Dejene  \nemail: tens2009et@gmail.com")
@app.route("/captions")
def captions():
    TITLE = "Break Bad Habits"
    FILE_NAME = "Break Bad Habits.wav"
    return render_template('captions.html', subtitle=TITLE, file=FILE_NAME)
@app.route("/resume")
def resume():
    TITLE1 = "resume"
    FILE_NAME1 = "resume.pdf"
    return render_template('resume.html', subtitle=TITLE1, file=FILE_NAME1)
@app.before_first_request
def before_first_request():
    #resetting time stamp file to 0
    file = open("pos.txt","w") 
    file.write(str(0))
    file.close()

    #starting thread that will time updates
    threading.Thread(target=update_captions).start()

@app.context_processor
def inject_load():
    # getting previous time stamp
    file = open("pos.txt","r")
    pos = int(file.read())
    file.close()

    # writing next time stamp
    file = open("pos.txt","w")
    file.write(str(pos+interval))
    file.close()

    #returning captions
    return {'caption':printWAV(FILE_NAME, pos=pos, clip=interval)}

def update_captions():
    with app.app_context():
        while True:
            # timing thread waiting for the interval
            time.sleep(interval)

            # forcefully updating captionsPane with caption
            turbo.push(turbo.replace(render_template('captionsPane.html'), 'load'))



if __name__ == '__main__':               # this should always be at the end avoids the need for environment variables
    app.run(debug=True, host="0.0.0.0")

#to run set environment variable:export FLASK_APP=demo unless you can use the command above