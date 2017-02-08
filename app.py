from flask import Flask, render_template, redirect, url_for, request, flash
from forms import User_Form
from models import User, db
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.secret_key = 'secret'
#Confifurar para el correo
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_USERNAME'] = 'sorpresa@gmail.com'
app.config['MAIL_PASSWORD'] = 'sorpresa'

@app.route("/")
def login():
    msg = Message("Hello",
                  sender="no-reply@idecrea.es",
                  recipients=["varanegadesign@gmail.com"])
    mail.send(msg)
    return render_template('items/login.html')

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = User_Form()
    #Comprobar el email esta en la base de datos
    if request.method == 'POST':
        if form.validate_on_submit():
            email= request.form['email']
            my_user= User.query.filter_by(email=email).first()
            if not my_user:
                # Comprobar si coinciden las password
                if request.form['password1'] == request.form['password2']:
                    my_user = User(request.form['username'], request.form['email'], request.form['password1'])
                    db.session.add(my_user)
                    try:
                        db.session.commit()
                        #Envio de email

                        #informamos al usuario
                        flash('Le acabamos de enviar un email con las instrucciones. Gracias.', 'success')
                    except:
                        db.session.rollback()
                        flash('Disculpe, ha ocurrido un error.', 'danger')
                    return redirect(url_for('login'))
                else:
                    flash('Las contraseñas no coinciden', 'danger')
            else:
                flash('El e-mail ya esta registrado', 'danger')
        else:
            #Mostramos errores
            errores = form.errors.items()
            for campo, mensajes in errores:
                for mensaje in mensajes:
                    flash(mensaje, 'danger')
    return render_template('items/signup.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()