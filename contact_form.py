from flask_wtf import FlaskForm
import secret
from wtforms import StringField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask import Flask, render_template, url_for, flash, redirect
#create some fields

class ContactForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    message = TextAreaField('Message',
                        validators=[DataRequired()])
    submit = SubmitField('Send')