#!/bin/bash

# Runs Radamsa 10 times on "command_line_example.sh" and saves the output to files in
# output directory "output_files numbering the files 1 - 10 and adds .sh suffix "  
radamsa -n 10 -o radamsa_param_output/file%n.txt default_parameter.txt