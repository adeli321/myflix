echo Stopping Services
sudo docker stop pyvideo
sudo docker rm pyvideo
rm -rf myflix

sudo docker build -t pyvideo .
sleep 5

sudo docker run -d -it -p 8080:8080 --name pyvideo pyvideo 
sleep 5
sudo docker exec -it pyvideo python3 video.py
