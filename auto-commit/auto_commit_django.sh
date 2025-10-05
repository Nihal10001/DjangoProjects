#!/bin/bash

cd /home/nihal/Documents/Coding/DjangoProjects/DjangoProjects  # CHANGE THIS PATH

echo "Watching DjangoProjects for changes..."
echo "Press Ctrl+C to stop"

inotifywait -m -r -e modify,create,delete --exclude '\.git' --format '%w%f' . | while read FILE
do
    # Ignore some common files that change frequently but shouldn't be committed
    if [[ $FILE == *"__pycache__"* ]] || [[ $FILE == *".pyc"* ]]; then
        continue
    fi
    
    echo "Change detected: $FILE"
    sleep 3  # Wait for multiple rapid changes
    
    cd /home/nihal/Documents/Coding/DjangoProjects/DjangoProjects  # CHANGE THIS PATH
    git add .
    if ! git diff --cached --quiet; then
        git commit -m "Auto-commit: $(date +'%Y-%m-%d %H:%M:%S')" --no-verify
        git push origin main
        echo "Changes committed and pushed!"
    fi
done
