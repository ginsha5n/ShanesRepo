#!/bin/bash

current_dir=$(basename "$(pwd)")
if [ "$current_dir" == "scripts" ]; then # String comparison
    cd ..
fi


# Remove any old logfile
path_to_log_file="TestOutputFile.log"

# Check file exists before deleting (good practise)

if [ -e "$path_to_log_file" ]; then
    rm "$path_to_log_file"
    echo "Deleted old log file"
fi

javac test_folder/testing.java  # Compile
java test_folder.testing    # Run
