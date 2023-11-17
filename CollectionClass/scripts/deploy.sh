#! usr/bin/bash

## Shell script to build docker image and deploy container

docker build -t flask-app -f ./deploy/Dockerfile .
#Run docker container in the background (-d)
sudo docker run -d -it -p --name flask 5000:5000 flask-app 
