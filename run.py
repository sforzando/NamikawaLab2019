from flask import Flask, request, render_template, send_from_directory, jsonify
from pathlib import Path

import logging
import logging.handlers
import random
import shutil

DATASET_PATH = '/mnt/dataset/wabisabi/'
MOVED_PATH = '/mnt/dataset/moved/'
MOSAIC_PATH = '/mnt/dataset/mosaic/'

app = Flask(__name__)

# Add RotatingFileHandler to Flask Logger
handler = logging.handlers.RotatingFileHandler(
    "NamikawaLab2019.log", "a+", maxBytes=3000, backupCount=5)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'))
app.logger.addHandler(handler)


def get_images():
    images = [x.name for x in list(Path(DATASET_PATH).glob('**/*.jpg'))]
    random.shuffle(images)
    return images


def move_images(images):
    for image in images:
        app.logger.info('Moving: ' + image)
        shutil.move(DATASET_PATH + image, MOVED_PATH + image)


def get_moved_images():
    images = [x.name for x in list(Path(MOVED_PATH).glob('**/*.jpg'))]
    return images


@app.route('/dataset/<path:filename>')
def get_dataset(filename):
    return send_from_directory(DATASET_PATH, filename)


@app.route('/mosaic/<path:filename>')
def get_mosaic(filename):
    return send_from_directory(MOSAIC_PATH, filename)


@app.route('/')
def index():
    return render_template('index.html', images=get_images())


@app.route('/first')
def first():
    return render_template('first.html', images=get_images())


@app.route('/second')
def second():
    return render_template('second.html', images=get_images())


@app.route('/third')
def third():
    return render_template('third.html', images=get_images())


@app.route('/move', methods=['POST'])
def move():
    rgd = request.get_data(as_text=True)
    app.logger.info('request.get_data(): ' + rgd)
    images = rgd.replace('images%5B%5D=', '').split('&')
    move_images(images)
    return jsonify(rgd)


@app.route('/moved')
def moved():
    return render_template('index.html', images=get_moved_images())


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
