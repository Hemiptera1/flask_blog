from flask import Flask, render_template, url_for
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

if __name__ == "__main__":
	app.run(debug=True)

