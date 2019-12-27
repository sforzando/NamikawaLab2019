from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)


def get_images():
    dataset_path = Path('/home/shin/NamikawaLab2019/dataset/wabisabi')
    return [x.name for x in list(dataset_path.glob('**/*.jpg'))]


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


@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

