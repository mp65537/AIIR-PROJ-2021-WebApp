import os

from flask import Flask, send_file, request
from forms import CompileForm

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/")
def main():
    return app.send_static_file('index.html')

@app.route('/compile', methods=['POST'])
def compile():
    form = CompileForm()
    zip = None

    if form.link.data != "":
        zip = "placeholder - zip from github"

    elif form.zip.data != None:
        zip = form.zip.data
    
    return "Placeholder - compiling"



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="0.0.0.0", debug=True, port=80)
