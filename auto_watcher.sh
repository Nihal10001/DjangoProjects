#!/bin/bash
echo "Starting file watcher for DjangoProjects..."
while true; do
    # Check for any changes in the last 10 seconds
    if git status --porcelain | grep -q .; then
        echo "Changes detected at $(date)"
        git add .
        git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"
        git push origin main
        echo "Changes committed and pushed!"
    fi
    sleep 10
done
