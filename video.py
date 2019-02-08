#! /usr/bin/env python3

import pymongo
from pymongo import MongoClient
import gridfs
from gridfs import GridFSBucket
from flask import Flask, render_template, request, url_for, Response

app = Flask(__name__)

@app.route('/')
def entry() -> 'html':
    return render_template('homepage.html', title='MyFlix Welcomes You')

@app.route('/invalid')
def invalid_request():
    return Response(status=400)

@app.route('/testme')
def test_me():
    text = 'Hello there I am a test!'
    return Response(text, mimetype='text/html')

@app.route('/moartests', methods=['POST'])
def moar_tests():
    da_title = 'Moar Tests Title Page'
    first    = request.form['first_name']
    last     = request.form['last_name']
    return render_template('moar_tests.html', title=da_title,
                                                first=first,
                                                last=last)

@app.route('/playvideo', methods=['POST', 'GET'])
def play_video():
    # def grab_title():
    #     video = request.form['movie_title']
    #     return video
    # client    = MongoClient(host='35.242.180.246:27017')
    # videoz     = request.form['movie_title']
    # if request.method == 'POST':
        # video = request.form['movie_title']
    client    = MongoClient('mongodb://restheart:R3ste4rt!@35.242.180.246:27017')
    # client2   = 0
    # if request.form['movie_title'] != '':
    # video = request.form.get("movie_title", True)
    # video     = request.form['movie_title']
    # video     = 'SampleVideo_1.mp4'
    video = request.form.get('movie_title')
    if video == None:
        return 'None no variable'
    else:
        client    = MongoClient('mongodb://restheart:R3ste4rt!@35.242.180.246:27017')
        videos_db = client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name('SampleVideo_1.mp4')
        contents  = grid_out.read()
        # return video
        return Response(contents, mimetype='video/mp4')
    # return Response(fake_contents, mimetype='video/mp4')
    # else:
    #     return 'hello'



if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)

