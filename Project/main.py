from flask import Flask, render_template, Response, request, redirect, url_for
from camera import VideoCamera, VideoCamera2

app = Flask(__name__)

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/', methods = ["POST", "GET"])
def index():
    return render_template('index.html')

@app.route('/video_feed', methods = ["POST", "GET"])
def video_feed():
    return Response(gen(VideoCamera()), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug = False)
