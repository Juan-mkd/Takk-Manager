# tasks/forms.py
from django import forms
from wtforms import Form, StringField, TextAreaField, BooleanField
from wtforms.validators import DataRequired

class TaskForm(Form):
    title = StringField('Título', validators=[DataRequired()])
    description = TextAreaField('Descripción')
    completed = BooleanField('Completada')
