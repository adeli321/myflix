echo Stopping Services
docker stop pyvideo
docker rm pyvideo
rm -rf myflix

docker run -d --name pyvideo python
sleep 10
docker exec -it pyvideo bash
git clone https://github.com/adeli321/myflix.git
pip install pymongo
pip install flask
python3 video.py