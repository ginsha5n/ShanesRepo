#!/bin/bash

directory="radamsa_param_output/"

for file in "$directory"*; do
    echo "Running script $file"
    python3 app_copy.py -f "$file"
    echo "-----------------------"
done