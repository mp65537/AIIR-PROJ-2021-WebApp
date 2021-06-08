import os, git, tempfile, time, requests, msgpack

from flask import flash, Flask, send_file, request
from forms import CompileForm
from werkzeug.utils import redirect, secure_filename

app = Flask(__name__, static_url_path='')
app.config['SECRET_KEY'] = 'you-will-never-guess'

@app.route("/")
def main():
    return app.send_static_file('index.html')

@app.route('/compile', methods=['POST'])
def downlaod():
    form = CompileForm()

    codefile = tempfile.NamedTemporaryFile(suffix='.zip').name
    codefilepath = os.path.join(codefile)
    
    # link z githuba
    if 'file' not in request.files:
        codedir = tempfile.mkdtemp()
        codedirpath = os.path.join(codedir)

        repo = git.Repo.clone_from(form.link.data, to_path=codedirpath)

        with open(codefilepath, 'wb') as zipfile: 
            repo.archive(zipfile, format='zip')
    
    else:
        file = request.files['file']

        # ani plik ani link
        if file.filename == '':
            return 'No file/link has been provided.'

        # plik
        else:
            file.save(codefilepath)

    # compile
    with open(codefilepath, 'rb') as to_compile:
        data = msgpack.packb({'zip': to_compile.read()})
        response = requests.post(
            'http://py:8080/api', 
            data=data,
            headers={'Content-Type': 'application/octet-stream'}
        )
        response_data = msgpack.unpackb(response.content)

        # placeholder - sobie czy cokolwiek wgle doszlo
        return str(response_data)

if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(levelname)-8s %(message)s'
    )

    app.run(host="0.0.0.0", debug=True, port=80)
    
