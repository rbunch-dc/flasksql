from flask import Flask, redirect, render_template
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
	print "Hello, World"
	return "Hello, World!"

# @app.route("/", methods=["POST"])
# def hello():
# 	print "Hello, World"
# 	return "Hello, World!"


@app.route("/algorithm")
def algorithm():
	print "DID I GET HERE?"
	return "Test1"

@app.route('/login')
def login():
	return render_template('login.html',
		name = "Rob",
		title = "American Ninja Warrior",
		a_list = [1,2,5,3,9],
		a_dict = {
			'boy1': "Mike TV",
			'boy2': "Agustus Gloop"
		},
		wannabetitle = "Willy Wonka")

@app.errorhandler(404)
def page_missing(e):
	print e
	return redirect("/", 404)

@app.route('/user/<user_name>')
def user_page(user_name):
	return "user %s" % user_name

if __name__ == "__main__":
	app.run(debug=True)