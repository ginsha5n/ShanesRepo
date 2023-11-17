Title: 
Collection of Presidents Project


Description:
An application that creates a collection of people based on first and second name and allows the user
to access and modify the collection through an api.

The collection contains a dictionary/hash map with a first name as a key and its second name as its pair value. 
Also an array is involved that contains a list of first names in the order they are added in, the first name can 
be found by its index position and the first name at that position is used as a key to find its matching second
name in the dictionary before returning the first and second name as a whole.
Names can be added, retreived and deleted, through the programs api


Getting started:
pip install flask, requests
pip install pytest (for testing puroposes).


Executing:
Launch server address, localhost:5000:
Execute  <flask run --host 0.0.0.0 --port 5000> in the cli while in src directory. 

launch url in browser, http://localhost:5000/president
http://localhost:5000/president/upload allows the client to upload a file
if president.json file is uploaded the president data will be uploaded and sorted in order.

http://localhost:5000/president can be used to search the collection by name or index position if an argument is passed
http://localhost:5000/president?fname=<name>
http://localhost:5000/president?index=<number>
Postman is another way to preview how the collection functions with a good interface.

Alternatively:
From parent directory execute scripts/deploy.sh to build the docker image and deploy the container with the name flask.
This leaves the api running while the container is up and to stop the container with:
<docker container stop flask>


Author:
Shane Ginty, shane.ginty@siemens.com

Development Stages:
Received job outline
Created diagrams
Defined use cases
Implemented functionality (CollectionClass.py)
Created test cases using pytest framework (test driven development) (test.py)
Created api using flask rest end points (front end) (app.py)
Created api test cases using Postman and later pytest.(testRest.py)
Restructured application files (src,deploy,tests, Readme, requirments)
Restructured files and fixed bugs that came with it.
Deployed test server using a docker container.
Created shell scripts to build docker image and run container.
Created shell script to run testcases
Implemented multipart form-data to allow file upload from client side.
