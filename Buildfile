echo Stopping Services
docker stop pyvideo
docker rm pyvideo
rm -rf myflix

git clone https://github.com/adeli321/myflix.git
docker build -t pyvideo .
sleep 10

docker run -d -it -p 8080:8080 --name pyvideo pyvideo 
sleep 10
docker exec -it pyvideo python3 video.py