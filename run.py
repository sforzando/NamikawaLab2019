from flask import Flask, request, render_template, send_from_directory, jsonify
from pathlib import Path

import random
import shutil

app = Flask(__name__)

DATASET_PATH = '/mnt/dataset/wabisabi/'
MOVED_PATH = '/mnt/dataset/moved/'
MOSAIC_PATH = '/mnt/dataset/mosaic/'


def get_images():
    # dataset_path = Path(__file__).parent / 'dataset/wabisabi'
    dataset_path = Path(DATASET_PATH)
    images = [x.name for x in list(dataset_path.glob('**/*.jpg'))]
    random.shuffle(images)
    return images


def move_images(images):
    for image in images:
        print('Moving: ' + image)
        shutil.move(DATASET_PATH + image, MOVED_PATH + image)


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
    print('request.get_data(): ' + rgd)
    images = rgd.replace('images%5B%5D=', '').split('&')
    move_images(images)
    return jsonify(rgd)


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
