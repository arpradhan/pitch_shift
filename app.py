from flask import (
    Flask,
    render_template,
    request)
from pitch_shift import PitchShift

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/shift', methods=['POST'])
def slow():
    audio = request.files['audio']
    octaves = float(request.form['octaves'])
    sound = PitchShift().from_file(audio, octaves)
    audio_html = sound._repr_html_()
    return render_template('shift.html', audio_html=audio_html)
