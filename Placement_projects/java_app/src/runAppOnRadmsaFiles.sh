#!/bin/bash

directory="radamsaTesting/radamsaOutputFiles/"

for file in "$directory"*; do 
    echo "Running script $file"
    java app_copy.java -i "$file"
    echo "-------------------"
done

