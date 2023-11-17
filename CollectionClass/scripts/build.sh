#! usr/bin/bash

## Shell script to build docker images

docker build -t flask-app -f ./deploy/Dockerfile .


