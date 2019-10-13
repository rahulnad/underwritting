from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateField,IntegerField,RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class registrationform(FlaskForm):
    

  firstname = StringField('First Name',validators = [Length(min = 2, max = 40)])

  lastname = StringField('Last Name',validators = [DataRequired(), Length(min = 2, max = 40)])

  email = StringField('Email',validators = [DataRequired(),Email()])

  dob = DateField('Date of birth',format='%Y-%m-%d',render_kw={"placeholder": "yyyy-mm-dd"})
  
  zipcode = StringField('Zip code',validators = [DataRequired(), Length(min = 1, max = 8)])

  brand = StringField('Brand',validators = [DataRequired(), Length(min = 1, max = 50)])

  make = StringField('Make',validators = [DataRequired(), Length(min = 1, max = 50)])

  yearofcar = DateField('Year of car',format='%Y',render_kw={"placeholder": "yyyy"})

  mileage = StringField('Mileage',validators = [DataRequired(), Length(min = 1, max = 6)])

  commute = RadioField('Are you using this car for daily commute?',choices=[('yes','Yes'),('no','No')])

  storage = RadioField('Do you store your vehicle in a garage?',choices=[('yes','Yes'),('no','No')])

  drivinghistory = DateField('When did you get your license?',format='%Y-%m-%d',render_kw={"placeholder": "yyyy-mm-dd"})

  accidenthistory = RadioField('Any Accident History?',choices=[('yes','Yes'),('no','No')])

  currentautocarrier = StringField('Who is your Current Auto Carrier?',validators = [DataRequired(), Length(min = 2, max = 40)])

  submit = SubmitField('Get your Quote')


