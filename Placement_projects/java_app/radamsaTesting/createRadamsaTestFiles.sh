#!/bin/bash

# Delete old test files
rm radamsaOutputFiles/file*

# Create new files using radamsa
radamsa -n 10 -o radamsaOutputFiles/file%n.txt ValidInput.txt
