import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder="build/static", template_folder="build")

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'build'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

print('Starting Flask!')

app.debug=True
app.run(host='127.0.0.1')
