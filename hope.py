from flask import Flask,render_template,url_for

hope = Flask(__name__)

@hope.route('/')
def home(): 
    return render_template('index.html')
if __name__ == "_main_":
    hope.run(debug=True,port=3300)