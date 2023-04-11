from flask import Flask, render_template

app = Flask(__name__)


posts = [
   {
   'author': 'Dustin Meyer',
   'title': 'Blog post 1',
   'content': "First post",
   'date_posted': 'April 20, 2018'
   },
      {
   'author': 'Bob Joe',
   'title': 'Blog post 2',
   'content': "Second post",
   'date_posted': 'April 21, 2018'
   },
]

@app.route("/")
@app.route("/home")
def home():
   return render_template('index.html', posts=posts)


@app.route("/about")
def about():
   return render_template('about.html', title="about")


app.run(host="0.0.0.0", port=80)


