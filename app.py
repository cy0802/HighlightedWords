import os
import imgToStr
import crawler
from flask import Flask, request, render_template, send_file
import readJson
import requests
import io

UPLOAD_FOLDER = '/static/upload'
ALLOWED_EXTENSIONS = set(['jpg', 'png', 'jpeg'])

app = Flask(__name__, static_folder="static/")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_SIZE'] = 7 * 1024 * 1024  # 7MB


@app.route('/history')
def history():
    word = readJson.select('data.json')
    return render_template('memorizeWord.html', words=word)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/intro")
def intro():
    return render_template('introduce.html')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/audio/<src>")
def test3(src):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    re = requests.get('https://dictionary.cambridge.org' +
                      src.replace('=', '/', 8), headers=user_agent)
    return send_file(io.BytesIO(re.content), mimetype="audio/mp3")


@app.route("/upload", methods=['POST', 'GET'])
def upload_picture():
    if request.method == "POST":
        picture = request.files['picture']
        if request.form['history'] == 'history':
            history = True
        else:
            history = False
        if picture.filename == '':
            return render_template('index.html', warning_msg="You didn't upload picture.")
        if allowed_file(picture.filename) == False:
            return render_template('index.html', warning_msg="Allowed filetype : jpg, png, jpeg")
        if picture and allowed_file(picture.filename):
            path = os.path.join('static', 'upload', picture.filename)
            picture.save(path)
            words = imgToStr.ImgToStr(path)
            translate = crawler.Translate(words)
            words = []
            for i in translate:
                words.append(i[0])
            print(words)
            if history == True:
                readJson.insertData(words, 'data.json')
            imgToStr.resize(path)
            return render_template('index.html', translation=translate, picture_path=picture.filename)

def main():
    app.run()
