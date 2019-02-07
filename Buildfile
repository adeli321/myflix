echo Stopping Services
docker stop pyvideo
docker rm pyvideo
rm -rf myflix

git clone https://github.com/adeli321/myflix.git
docker build -t buildme .
sleep 10

docker exec -it pyvideo bash -c 'pip install flask'
docker exec -it pyvideo bash -c 'pip install pymongo'
docker exec -it pyvideo python3 video.py