from flask import Flask, request, render_template
app = Flask(__name__)

comments=[]

@app.route('/')
def index():
    message = 'sample_string'
    return render_template('index.html',message=message)

@app.route('/submit',methods=['Get','POST'])
def submit():
    return 'You entered:{}'.format(request['memo'])