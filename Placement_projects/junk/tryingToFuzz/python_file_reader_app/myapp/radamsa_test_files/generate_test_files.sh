#!/bin/bash

# Runs Radamsa 10 times on "command_line_example.sh" and saves the output to files in
# output directory "output_files numbering the files 1 - 10 and adds .sh suffix "  
radamsa -n 10 -o output_files/%n.sh command_line_example.sh