# sudo pip install flask-mysql

from flask import Flask, render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
# create an instance of the mysql class
mysql = MySQL()
# Add to the app (Flask object) some config data for our connection
app.config['MYSQL_DATABASE_USER'] = 'x'
app.config['MYSQL_DATABASE_PASSWORD'] = 'x'
# The name of teh database we want to connect to at the DB server
app.config['MYSQL_DATABASE_DB'] = 'rest'
# Where teh MYSQL server is at
app.config['MYSQL_DATABASE_HOST'] = '127.0.0.1'
# use the mysql object's method "init_app" and pass it the flask object
mysql.init_app(app)

@app.route("/", methods=["GET"])
def index():
	
	# set up a cursor object whihc is what the sql object uses to connect and run queries
	cursor = mysql.connect().cursor()
	# execute a query with teh execute method
	cursor.execute("SELECT * FROM user WHERE 1")
	# Turn the mysql object into something we can use
	data = cursor.fetchall()
	print data
	if data is None:
		return "Your query returns no results"
	else:
		return render_template('rest.html',
			data = data)


if __name__ == "__main__":
	app.run(debug=True)