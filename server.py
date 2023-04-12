from flask import Flask, render_template, request, url_for, flash, redirect
from forms import registrationForm, loginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = '832d1b72a3f6030c639fc41944ea3c3d'


@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html')

@app.route("/about")
def about():
   return render_template('about.html', title="about")

@app.route("/register", methods=['GET', 'POST'])
def register():
   form = registrationForm()
   if form.validate_on_submit():
       flash(f'Account create for {form.name.data}!', 'success')
       return redirect(url_for('home'))
   return render_template('register.html', title="register", form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
      return render_template('home.html')

if(__name__ == "__main__"):
   #app.run(host='137.21.145.253', debug=True)
   app.run(port=80, debug=True)
   #app.run(host="0.0.0.0", port=80)


