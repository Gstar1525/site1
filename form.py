from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField
from wtforms.validators import DataRequired, Length

class RegisterName(FlaskForm):
    userName = StringField('Enter Your Name', validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Create Quiz')

class SubmitOwn(FlaskForm):
    submitOwn = SubmitField('Create your own questions')

class SubmitReady(FlaskForm):
    submitReady = SubmitField('Ready-made questions')

class ReadMade(FlaskForm):
    question = StringField("What is gourav's fav Color ?", validators=[DataRequired()])
    option = RadioField('OPTION NO 1', choices=['OPTION NO 1', 'OPTION NO 2', 'OPTION NO 3', 'OPTION NO 4'])
    submitReady = SubmitField('SUBMIT')
    skip = SubmitField('SKIP')
    done = SubmitField('DONE')

class OwnMade(FlaskForm):
    question = StringField(validators=[DataRequired()])
    option_1 = StringField(validators=[DataRequired()])
    option_2 = StringField(validators=[DataRequired()])
    option_3 = StringField(validators=[DataRequired()])
    option_4 = StringField(validators=[DataRequired()])
    submitReady = SubmitField('NEXT')
    done = SubmitField('DONE')