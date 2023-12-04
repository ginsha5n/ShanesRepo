#!/bin/bash

directory="radamsaTesting/radamsaOutputFiles/"

for file in "$directory"*; do
    echo "Running script $file"
    javac src/app_copy.java
    java src/app_copy.java -f $file
    echo "-----------------------"
done
