echo Stopping Services
docker stop pyvideo
docker rm pyvideo
rm -rf myflix

docker build -t pyvideo .
sleep 5

docker run -d -it -p 8080:8080 --name pyvideo pyvideo 
sleep 5
docker exec -it pyvideo python3 video.py
