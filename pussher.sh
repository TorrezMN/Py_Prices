#!/bin/bash


cd /home/torrezmn/Documentos/Py_Prices

# Get the current date and time
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M:%S)


# Set the commit message
COMMIT_MESSAGE="UPDATED - {$DATE} - {$TIME}"

# Stage all changes
git add *

# Commit the changes with the specified message
git commit -m "$COMMIT_MESSAGE"

# Push the changes to the remote repository
git push

