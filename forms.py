from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, SubmitField, URLField
from wtforms.validators import URL, InputRequired



class URLForm(FlaskForm):
    userinput_url = URLField(
        "Please input a URL",
        validators=[InputRequired()]
    )

    submit=SubmitField()
