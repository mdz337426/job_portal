from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField, SubmitField,  PasswordField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class JobForm(FlaskForm):
    company = StringField('Company', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    date_applied = DateField('Date Applied', format='%Y-%m-%d', validators=[DataRequired()])
    status = SelectField('Status', choices=[('Pending', 'Pending'), ('Interview', 'Interview Scheduled'),
                                            ('Rejected', 'Rejected'), ('Hired', 'Hired')])
    submit = SubmitField('Save Job')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
