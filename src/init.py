import os
import whisper

from flask import Flask, request
from flask import jsonify
from flasgger import Swagger
from flask_cors import CORS
from werkzeug.utils import secure_filename

app = Flask(__name__)
swagger = Swagger(app)
CORS(app)

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    """
    Transcribe an audio file
    ---
    parameters:
      - name: audio
        in: formData
        type: file
        required: true
    responses:
      200:
        description: Text transcribed from the audio file
    """
    if 'audio' not in request.files:
        return jsonify(error='No audio file in request'), 400

    file = request.files['audio']
    filename = secure_filename(file.filename)
    filepath = os.path.join('audios', filename)
    file.save(filepath)

    model = whisper.load_model("medium")
    result = model.transcribe(filepath)

    return jsonify(text=result["text"])

if __name__ == '__main__':
    app.run(debug=True, port=5000)