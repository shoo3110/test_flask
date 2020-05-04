from flask import Flask, request, url_for, render_template
import datetime
import os
app = Flask(__name__)


path = 'static/kenji.txt'
path2 = 'static/date.csv'


@app.route('/', methods=['GET','POST'])
def index():
        if request.method == 'POST':
                f = open(path, mode='w')
                message = request.form["memo"]
                f.write(message)
                print(type(message))
                f.close()

                d = open(path2, mode='w')
                date = datetime.datetime.now()
                update_date = date.strftime("%Y-%m-%d %H:%M")
                d.write(update_date)
                print(type(update_date))
                d.close()
                return render_template('index.html', message=message, update_date=update_date)
        else:
                f = open(path)
                message = f.read()
                print(type(message))
                f.close()
                d = open(path2)
                update_date = d.read()
                print(type(update_date))
                d.close()
                return render_template('index.html', message=message, update_date=update_date)



if __name__ == "__main__":
    app.run()