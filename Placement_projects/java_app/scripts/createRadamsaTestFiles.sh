#!/bin/bash

current_dir=$(basename "$(pwd)")
if [ "$current_dir" == "scripts" ]; then # String comparison
    cd ../radamsaTesting

else
    cd radamsaTesting/
fi


default_files_created=10

# This takes in the first argument in th cli as the amount of files to create, 
# if none is provided it defaults to the default_files_created value
files_created=${1:-$default_files_created}

# Delete old test files
rm radamsaOutputFiles/file*

# Create new files using radamsa
radamsa -n "$files_created" -o radamsaOutputFiles/file%n.txt ValidInput.txt
