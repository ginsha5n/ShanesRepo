#!/bin/bash

directory="radamsaTesting/radamsaOutputFiles/"

for file in "$directory"*; do
    echo "Running script $file"
    javac src/app.java
    java src/app.java -f $file
    echo "-----------------------"
done
