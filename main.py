from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
	{
		'author': 'Eoghan Winters',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': '5th March 2020'
	},
	{
		'author': 'Ruairi Winters',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': '6th March 2020'
	}
]


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html', posts=posts)

@app.route("/about")
def about():
	return render_template('about.html', title='About')

if __name__ == "__main__":
	app.run(debug=True, host="0.0.0.0")
