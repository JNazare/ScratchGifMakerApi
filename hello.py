from flask import Flask, request
from werkzeug import secure_filename
import os

UPLOAD_FOLDER = '/Users/Juliana/Desktop'
ALLOWED_EXTENSIONS = set(['mov'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route('/', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
            return "DONE!"
    
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)