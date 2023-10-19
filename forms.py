from wtforms import Form, BooleanField, IntegerField, StringField, PasswordField
from wtforms import SubmitField, TextAreaField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, InputRequired
from shop.models import User, Addproduct
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired

class CheckoutForm(Form):
    name = StringField('Name', [validators.Length(min=6, max=35),validators.DataRequired(),validators.Email()])
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email(),validators.EqualTo('name', message='Emails must match')])
    delivery = StringField('Delivery Address ', [validators.Length(min=6, max=35)])
    postcode = StringField('Postcode', [validators.length(min=6,max=7)])
    city = StringField('City', [validators.DataRequired()])
    card_name = StringField('Name on Card',[validators.Length(min=6, max=35),validators.DataRequired()])
    password = PasswordField('Card Number', [validators.Length(min=12, max=19),
        validators.DataRequired()])
    confirm = PasswordField('CVV',[validators.Length(min=3, max=4)])

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address is already associated with an account.')

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=25)])
    username = StringField('Email Address', [validators.Length(min=6, max=35),validators.DataRequired(),validators.Email()])
    email = StringField('Confirm Email Address', [validators.Length(min=6, max=35),validators.Email(),validators.EqualTo('username', message='Emails must match')])
    password = PasswordField('New Password', [
        validators.DataRequired(),
    ])
    confirm = PasswordField('Repeat Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')
    ])

    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Email address is already associated with an account.')

class LoginForm(FlaskForm):
  email = StringField('email',validators=[DataRequired(),Email()])
  password = PasswordField('password',validators=[DataRequired()])

class ProfileForm(FlaskForm):
  name = StringField('Name', [validators.Length(min=1, max=35),validators.DataRequired()])
  email = StringField('Email', [validators.Length(min=6, max=35),validators.DataRequired(),validators.Email()])
  password = PasswordField('Password',[validators.Length(min=6, max=35)], render_kw={"placeholder": "Unchanged"})

class UserRegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=1, max=35),validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=35),validators.DataRequired(),validators.Email()])
    password = PasswordField('Password',[validators.Length(min=6, max=35),validators.DataRequired()])
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('That email address is already associated with an account.')

class Addproducts(Form):
    name = StringField('Name',[validators.DataRequired()])
    price = IntegerField('Price',[validators.DataRequired()])
    description = TextAreaField('Description',[validators.DataRequired()])
    stock = IntegerField('Stock',[validators.DataRequired()])
    picture = FileField('Image',[validators.DataRequired()])

    image_1 = FileField('Image 1', validators=[FileRequired(),FileAllowed(['jpg','png','gif','jpeg']), 'images only please'])
    image_2 = FileField('Image 2', validators=[FileRequired(),FileAllowed(['jpg','png','gif','jpeg']), 'images only please'])
    image_3 = FileField('Image 3', validators=[FileRequired(),FileAllowed(['jpg','png','gif','jpeg']), 'images only please'])
