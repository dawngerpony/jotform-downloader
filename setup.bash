#!/bin/bash
# Setup script for JotForm downloader

API_KEY_FILE=".env/api.key"

function go {
    if [ ! -d .env ]; then
        virtualenv .env
    fi
    . .env/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    if [ -f $API_KEY_FILE ]; then
        echo "Existing JotForm API key found."
    else
        echo "What is your JotForm API key? "
        read apikey
        echo "export JOTFORM_API_KEY=\"$apikey\"" > $API_KEY_FILE
    fi
}

go
