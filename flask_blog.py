from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = '989f5f34012c953dd427138de864094e'

posts = [
	{
		"author": "Pablo Tomasso",
		"title": "Intro to Flask",
		"content": "What is Flask?",
		"date_posted": "September 30, 2019"
	},
	{
		"author": "Ninja-Cat",
		"title": "Intro to mastering stealth",
		"content": "How to sneak up on any human pt.1",
		"date_posted": "October 31, 2019"
	}

]

@app.route("/")
@app.route("/home")
def home():
	return render_template("home.html", posts = posts)

@app.route("/about")
def about():
	return render_template("about.html", title = "About")

@app.route("/register", methods = ["GET", "POST"])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f"Account successfully created for { form.username.data }!", "success")
		return redirect(url_for("home"))
	return render_template("register.html", title = "Register Page", form = form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template("login.html", title = "Login Page", form = form)

if __name__ == "__main__":
	app.run(debug=True)

