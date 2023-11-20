# import the Flask library
from flask import Flask, render_template, request


# Create the Flask instance and pass the Flask 
# constructor the path of the correct module
app = Flask(__name__)

# The URL 'localhost:5000/square' is mapped to
# view function 'squarenumber'
# The GET request will display the user to enter 
# a number (coming from squarenum.html page)


@app.route('/', methods=['GET', 'POST'])
def index():
	return  "Welcome on my first containerized app stay tuned with developments"




# Start with flask web app with debug as
# True only if this is the starting page
if(__name__ == "__main__"):
	app.run(debug=True)