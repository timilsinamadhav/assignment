#!/bin/bash

# Checking directory parameter
if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory>"
    exit 1
fi

directory="$1"

# Checking if the directory exists
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

# Find all files with .txt extention in the directory, convert to lowercase, 
# remove punctuation, split into words, sort, and get unique words
find "$directory" -type f -name "*.txt" -print0 | 
    xargs -0 cat | 
    tr '[:upper:]' '[:lower:]' | 
    tr -d '[:punct:]' | 
    tr ' ' '\n' | 
    sort | 
    uniq -i |
    grep -v '^$'
