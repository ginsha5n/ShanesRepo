#!/bin/bash

cd ..

directory="radamsaTesting/radamsaOutputFiles/"

# Counter for tests that passed/failed
tests_passed=0
tests_failed=0


for file in "$directory"*; do
    echo "Running script $file"
    java src.app -f $file
    exit_code=$?

    # if process exit code equals zero increase tests passed value else increse tests failed value
    if [ "$exit_code" -eq 0 ]; then
        echo "$file passed"
        ((tests_passed++))
    else
        echo "$file failed"
        ((tests_failed++))
    echo -e "-----------------------\n"
    fi
done

# Print amount of tests passed and failed.
echo "Passed: $tests_passed"
echo "Failed: $tests_failed"
