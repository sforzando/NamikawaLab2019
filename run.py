import logging.handlers
import random
import shutil
import string
from pathlib import Path

from flask import Flask, request, render_template, send_from_directory, jsonify

DATASET_PATH = '/mnt/dataset/wabisabi/'
MOVED_PATH = '/mnt/dataset/moved/'
MOSAIC_PATH = '/mnt/dataset/mosaic/'

app = Flask(__name__)

# Add RotatingFileHandler to Flask Logger
handler = logging.handlers.TimedRotatingFileHandler('NamikawaLab2019.log', when='D')
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(handler)


def get_random_string(digit=8):
    """ for Cache Control Hash """
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(digit)])


def get_images():
    images = [x.name for x in list(Path(DATASET_PATH).glob('**/*.jpg'))]
    random.shuffle(images)
    return images


def move_images(images):
    for image in images:
        try:
            shutil.move(DATASET_PATH + image, MOVED_PATH + image)
        except Exception as e:
            app.logger.error(e)
        else:
            app.logger.info('Moved: ' + image)


def undo_images(images):
    for image in images:
        try:
            shutil.move(MOVED_PATH + image, DATASET_PATH + image)
        except Exception as e:
            app.logger.error(e)
        else:
            app.logger.info('Undoed:' + image)


def get_moved_images():
    images = [x.name for x in list(Path(MOVED_PATH).glob('**/*.jpg'))]
    return images


@app.route('/dataset/<path:filename>')
def get_dataset(filename):
    return send_from_directory(DATASET_PATH, filename)


@app.route('/moved/<path:filename>')
def get_moved(filename):
    return send_from_directory(MOVED_PATH, filename)


@app.route('/mosaic/<path:filename>')
def get_mosaic(filename):
    return send_from_directory(MOSAIC_PATH, filename)


@app.route('/')
def index():
    return render_template('index.html', images=get_images(), cch=get_random_string(8))


@app.route('/first')
def first():
    return render_template('first.html', images=get_images(), cch=get_random_string(8))


@app.route('/second')
def second():
    return render_template('second.html', images=get_images(), cch=get_random_string(8))


@app.route('/third')
def third():
    return render_template('third.html', images=get_images(), cch=get_random_string(8))


@app.route('/moved')
def moved():
    return render_template('moved.html', images=get_moved_images(), cch=get_random_string(8))


@app.route('/move', methods=['POST'])
def move():
    rgd = request.get_data(as_text=True)
    app.logger.info('/move: ' + rgd)
    images = rgd.replace('images%5B%5D=', '').split('&')
    move_images(images)
    return jsonify(rgd)


@app.route('/undo', methods=['POST'])
def undo():
    rgd = request.get_data(as_text=True)
    app.logger.info('/undo: ' + rgd)
    images = rgd.replace('images%5B%5D=', '').split('&')
    undo_images(images)
    return jsonify(rgd)


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
