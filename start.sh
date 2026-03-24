#!/bin/bash

echo "Starting stream server..."
python stream.py &

sleep 2

echo "Starting Highrise bot..."

python -m highrise bot:StarlightSnugglesBot $ROOM_ID $API_TOKEN || echo "BOT CRASHED"
