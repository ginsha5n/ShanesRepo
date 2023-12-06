# Intro
This project takes two text files and uses them to produce an outfile of words taken from both files and mixed together.

Different variations of output can be produced by passing in the number of words you want taken from one or both files.

* -p {integer number} specifies how many words to take from file one (positive words file)
* -n {integer number} specifies how many words to take from file two (negative words file)
* -h help

app.java  uses the value 2 as the default amount of words to take from the files if no arguments are provided.


# Testing

from java_app directory, run java test_folder/testing.java
This will run the testing file which runs the app multiple times.

# Usage
The scripts folder contains a number of shell scripts to run the application.

* buildScript compiles all neccessary files
* createRadamsaTestTiles runs the radamsa tool on a valid input and produces a series of test input
(The createRadamsaTestFiles.sh can be run with an argument inter of number of files to make, if not argument is given it defaults to 10)
* runRadmsa files runs the application on each testfile produced by radamsa and prints their output aswell as a passed/failed counter at the end detailing how many testcases passed and how many failed.
* runTests runs the application on some testcases  in the testing.java file. These tested the functionality of some of the applications framework tools


