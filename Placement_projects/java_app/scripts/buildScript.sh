#!/bin/bash

# Compile javav files within the application

# figure out current directory. Command will work in either the base project dir or the scripts folder.
current_dir=$(basename "$(pwd)")
if [ "$current_dir" == "scripts" ]; then # String comparison
    cd ..
fi

# Compile App
javac src/app.java

# Compile Testing app.
javac test_folder/testing.java 

echo "Java files compiled successfully"
