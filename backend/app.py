from flask import Flask, request, send_file
from murf_api import generate_voice
from video_merge import merge_audio_video
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


app = Flask(__name__)
UPLOAD_FOLDER = "uploads/"
OUTPUT_FOLDER = "static/final_videos/"

@app.route('/upload', methods=['POST'])
def upload():
    video = request.files['video']
    script = request.form['script']
    voice_id = request.form['voice_id']

    video_path = os.path.join(UPLOAD_FOLDER, video.filename)
    video.save(video_path)

    audio_path = generate_voice(script, voice_id)
    output_path = merge_audio_video(video_path, audio_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
