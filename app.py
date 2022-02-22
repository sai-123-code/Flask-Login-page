# Importing flask module in the project is mandatory An object of Flask class is our WSGI application.
from flask import Flask,redirect,url_for,render_template,request
# Flask constructor takes the name of current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, which tells the application which URL should call the associated function.
# ‘/’ URL is bound with hello_world() function.
@app.route('/')
def hello_world():
	return render_template('home.html')

@app.route('/passed/<uname>')
def passed(uname):
	return render_template('success.html',username=uname)

@app.route('/fail/<uname>')
def fail(uname):
	return 'Sorry your restricted for accessing webpage'

@app.route('/submit',methods=['POST','GET'])
def submit():
	if request.method=='POST':
		username=request.form['uname']
		password=request.form['pwd']
	result = ''
	if username =="varun" and password=="1234":
		result = 'passed'
	else:
		result = "fail"
	return redirect(url_for(result,uname=username))

# main driver function
if __name__ == '__main__':
	# run() method of Flask class runs the application
	# on the local development server.
	app.run(debug=True)
