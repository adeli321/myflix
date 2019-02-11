#! /usr/bin/env python3

import pymongo
from pymongo import MongoClient
import gridfs
from gridfs import GridFSBucket
from flask import Flask, render_template, request, url_for, Response, redirect, session

app = Flask(__name__)
app.secret_key = b'_5-y4L"F4Q9z\n\x7ec]/'














mongo_client = MongoClient('mongodb://restheart:R3ste4rt!@35.234.143.12:27017')

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

@app.route('/testimage')
def test_image() -> 'html':
    return render_template('image_test.html')

@app.route('/showvideo', methods=['POST', 'GET'])
def show_video() -> 'video':
    if request.method == 'POST':
        session['video_title'] = request.form['title']
        videos_db = mongo_client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video_title'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')
    elif request.method == 'GET':
        videos_db = mongo_client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video_title'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')


# @route('/img/gridfs/<filename>')
# def gridfs_img(filename):
#     dbname = 'my_gridfs'
#     db = connection[dbname]
#     fs = gridfs.GridFS(db)
#     thing = fs.get_last_version(filename=filename)
#     response.content_type = 'image/jpeg'
#     return thing


@app.route('/img/gridfs/<filename>')
def gridfs_img(filename):
    images_db = mongo_client.get_database('thumbnails')
    


    fs        = GridFSBucket(images_db)
    grid_out  = fs.open_download_stream_by_name(filename)
    contents  = grid_out.read()
    return Response(contents, mimetype='image/png')

    # fs        = gridfs.GridFS(images_db)
    # thing = fs.get_last_version(filename=filename)
    # response.content_type = 'image/jpeg'
    # return thing



@app.route('/playvideo', methods=['POST', 'GET'])
def play_video():
    if request.method == 'POST':
        session['video'] = request.form['movie_title'] 
        videos_db = mongo_client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')
    elif request.method == 'GET':
        videos_db = mongo_client.get_database('videos')
        fs        = GridFSBucket(videos_db)
        grid_out  = fs.open_download_stream_by_name(session['video'])
        contents  = grid_out.read()
        return Response(contents, mimetype='video/mp4')
    else:
        return post 





if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port=8080)

