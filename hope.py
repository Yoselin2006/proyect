from flask import Flask,render_template,url_for

hope = Flask(__name__)

@hope.route('/')
def home(): 
    return render_template('home.html')
@hope.route('/signup')
def signup(): 
    return render_template('signup.html')
@hope.route('/signin')
def signin(): 
    return render_template('signin.html')


if __name__ == "_main_":
    hope.run(debug=True,port=3300) 
