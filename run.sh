#!/bin/bash
# Load environment variables
if [ -f .env ]; then
    export $(cat .env | grep -v '^#' | xargs)
fi

# Run the script
uv run main.py
