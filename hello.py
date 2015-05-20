from flask import Flask, request, send_file
from werkzeug import secure_filename
import os
from moviepy.editor import *
from PIL import Image

UPLOAD_FOLDER = '/Users/Juliana/Desktop'
GIF_FILE_PATH = '/Users/Juliana/Desktop/test.gif'
ALLOWED_EXTENSIONS = set(['MOV'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def make_gif(filename):
    clip = (VideoFileClip(filename).rotate(-90).resize(0.5))
    clip.write_gif(GIF_FILE_PATH, fps=1)
    with open(GIF_FILE_PATH, "rb") as f:
        gif = f.read()
        encoded_gif = gif.encode("base64")
    return encoded_gif
    # gif = Image.open(GIF_FILE_PATH)
    # return gif#send_file(GIF_FILE_PATH, mimetype="image/gif", as_attachment=True)

@app.route('/', methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files["file"]
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path_on_comp = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(path_on_comp)
            gif = make_gif(path_on_comp)
            return gif
    
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)