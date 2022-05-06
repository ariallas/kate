# import http.server
# import socketserver
# import socket

# PORT = 30001

# Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     print(socket.gethostbyname(socket.gethostname()))
#     httpd.serve_forever()

from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost', 27017)

db = client.flask_db
inputs = db.inputs

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method=='POST':
        userInput = request.form['userInput']
        inputs.insert_one({'input': userInput})
        return redirect(url_for('index'))

    all_inputs = inputs.find()
    return render_template('index.html', inputs=all_inputs)