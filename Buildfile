echo Stopping Services
docker stop pyvideo
docker rm pyvideo

docker run -d --name pyvideo python
docker exec -it pyvideo bash
git clone https://github.com/adeli321/myflix.git
pip install pymongo
pip install flask
python3 video.py