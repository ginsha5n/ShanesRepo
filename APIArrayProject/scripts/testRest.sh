#! usr/bin/bash

## Shell Script to run rest end point tests

# Deploys docker container
# Run tests for rest endpoints interaction 
# Bring down container
cd /mnt/c/Users/z004swjt/Documents/CodeBase/CollectionClass/src
sudo docker run -d -it --name flask -p 5000:5000 flask-app 
cd /mnt/c/Users/z004swjt/Documents/CodeBase/CollectionClass
sleep 1
pytest -v tests/testRest.py
docker stop flask
docker container rm flask  