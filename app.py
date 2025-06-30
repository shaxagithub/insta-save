from flask import Flask, request, send_file, render_template
import os
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    try:
        ydl_opts = {
            'outtmpl': 'downloaded_video.%(ext)s',
            'format': 'mp4',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return send_file('downloaded_video.mp4', as_attachment=True)
    except Exception as e:
        return f"Xatolik yuz berdi: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
