#!/usr/bin/env bash
export JOTFORM_API_KEY=$(cat $HOME/.secrets/jotform_api_key)
time python src/main.py $*
