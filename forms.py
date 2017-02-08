from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, Length, Email

class User_Form(Form):
    username = StringField('Username', validators=[InputRequired('Debe introducir un nombre de usuario'),
                                              Length(1, 100, 'El nombre es demasiado largo')])
    email = StringField('E-mail', validators=[InputRequired('Debe introducir un e-mail'),
                                              Length(1, 80, 'El e-mail es demasiado largo'),
                                              Email('Tu e-mail no tiene una estructura correcta')])
    password1 = PasswordField('Contraseña', validators=[InputRequired('Necesitas indicar una contraseña')])
    password2 = PasswordField('Contraseña', validators=[InputRequired('Repita contraseña')])
    submit = SubmitField('Sign up')