from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
import socket

app = Flask(__name__)
client = MongoClient('kate-mongo-service.default.svc.cluster.local', 27017)

db = client.flask_db
inputs = db.inputs

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        userInput = request.form['userInput']
        inputs.insert_one({'input': userInput})
        return redirect(url_for('index'))

    all_inputs = inputs.find()
    return render_template('index.html', inputs=all_inputs, hostname=socket.gethostname())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)