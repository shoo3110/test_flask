from flask import Flask, request, render_template
import datetime
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
    date = datetime.datetime.now()
    update_date = date.strftime("%Y-%m-%d %H:%M")
    return render_template('send_post.html',message=message, update_date=update_date)

