from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def post():
    name = request.form.get('memo')