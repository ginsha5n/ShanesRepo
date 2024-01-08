#!/bin/bash

cd output_files

for script in *.sh; do
    echo "Running script $script"
    ./"$script"
    echo "-----------------------"
done