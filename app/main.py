import os
from flask import Flask, render_template
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/")
def main():
    # get base from env vars instead
    base = os.environ['API']
    api = base + '/api'
    artifact = base + '/artifact'
    return render_template('index.html', api=api, artifact=artifact)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)-8s %(message)s'
    )

    app.run(host="0.0.0.0", debug=True, port=80)
    
