#!/bin/bash
# Usage: ./http_methods.sh <URL>
curl -sI --request OPTIONS "$1" | grep -i allow | awk -F ": " '{print $2}'
