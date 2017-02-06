from flask import Flask, render_template, redirect, url_for
from forms import User_Form

app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def index():
    return redirect(url_for('signup'))

@app.route("/signup")
def signup():
    form = User_Form()
    return render_template('items/signup.html', form=form)

if __name__ == '__main__':
    app.debug = True
    app.run()