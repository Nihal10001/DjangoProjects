#!/bin/bash
cd ~/DjangoProjects
while true; do
    if git status --porcelain | grep -q .; then
        echo "Changes detected: $(date)"
        git add .
        git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')"
        git push origin main
        echo "Pushed successfully at $(date)"
    fi
    sleep 30
done
