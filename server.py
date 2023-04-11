from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
   return render_template('home.html')

@app.route("/about")
def about():
   return render_template('about.html', title="about")

@app.route("/register", methods=('GET', 'POST'))
def register():
   # Textfield names: name, email, password, confirmPassword
   if request.method == "POST":
      if request.form['password'] != request.form['confirmPassword']:
         return render_template('register.html', title="register", error="is-invalid", errorMsg="Password must match", inputName=request.form['name'], inputEmail=request.form['email'])
      # redirect when inputs are valid
      return redirect('/', code=302)
      #print(request.form['name'])
   return render_template('register.html', title="register")

if(__name__ == "__main__"):
   app.run(port=8000, debug=True)
   #app.run(host="0.0.0.0", port=80)


