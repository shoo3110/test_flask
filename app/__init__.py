from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    path = 'static/kenji.txt'
    with open(path) as f:
        message = f.read()
        print(type(message))
    return render_template('index.html',message=message)


@app.route('/submit',methods=["POST"])
def submit():
    message = request.form["memo"]
    return render_template('send_post.html',message=message)

