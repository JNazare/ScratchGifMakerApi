from flask import Flask, request
from werkzeug import secure_filename
import os
from moviepy.editor import *

UPLOAD_FOLDER = '/Users/Juliana/Desktop'
ALLOWED_EXTENSIONS = set(['MOV'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def make_gif(filename):
    clip = (VideoFileClip(filename).rotate(-90).resize(0.3))
    clip.write_gif("/Users/Juliana/Desktop/test.gif", fps=1)

@app.route('/', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path_on_comp = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path_on_comp)
            make_gif(path_on_comp)
            return "DONE!"
    
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)