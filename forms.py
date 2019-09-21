from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,DateField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class registrationform(FlaskForm):
    
  age = StringField('Age',validators = [DataRequired(), Length(min = 1, max = 3)])

  VehicleValue = StringField('Vehicle Value',validators = [DataRequired(), Length(min = 1, max = 8)])

  middlename = StringField('Middle Name',validators = [Length(min = 2, max = 40)])

  lastname = StringField('Last Name',validators = [DataRequired(), Length(min = 2, max = 40)])

  email = StringField('Email',validators = [DataRequired(),Email()])

  dateofbirth  = DateField('Date of Birth',format = '%Y-%m-%d')

  policyexpirationdate  = DateField('Current Policy Expiration Date',format = '%Y-%m-%d')

  currentautocarrier = StringField('Current Auto Carrier',validators = [DataRequired(), Length(min = 2, max = 40)])

  submit = SubmitField('Get your Quote')


