#! /usr/bin/env python3

import pymongo
from pymongo import MongoClient
import gridfs
from gridfs import GridFSBucket
from flask import Flask, render_template, request, url_for, Response, redirect, session
import json

app = Flask(__name__)
app.secret_key = b'_5-y4L"F4Q9z\n\x7ec]/'

@app.route('/', methods=['GET'])
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
def moar_tests() -> 'html':
    da_title = 'Moar Tests Title Page'
    first    = request.form['first_name']
    last     = request.form['last_name']
    return render_template('moar_tests.html', title=da_title,
                                                first=first,
                                                last=last)

@app.route('/playvideo', methods=['POST', 'GET'])
def play_video():
    if request.method == 'POST':
        session['video'] = request.form['movie_title'] 
        client    = MongoClient('mongodb://restheart:R3ste4rt!@35.242.180.246:27017')
        videos_db = client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')
    elif request.method == 'GET':
        client    = MongoClient('mongodb://restheart:R3ste4rt!@35.242.180.246:27017')
        videos_db = client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')
    else:
        return post 





if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)

