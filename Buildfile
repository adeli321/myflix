echo Stopping Services
sudo docker stop pyvideo
sudo docker rm pyvideo

sudo docker build -t pyvideo .
sudo docker run -d -it -p 8080:8080 --name pyvideo pyvideo 
sudo docker exec -d pyvideo python3 video.py
