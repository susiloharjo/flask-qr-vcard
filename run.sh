#!/bin/bash

# Exit script if any command fails
set -e

# Check if docker-compose is installed
if ! command -v docker-compose &> /dev/null
then
    echo "docker-compose could not be found"
    exit 1
fi

echo "Running docker-compose build..."
docker-compose build

echo "Build completed successfully."
