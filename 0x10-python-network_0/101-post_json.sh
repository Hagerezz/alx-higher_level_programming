#!/bin/bash
# Usage: ./post_json_request.sh <URL> <JSON_FILE>
curl -s -X POST -d "@$2" -H "Content-Type: application/json" "$1"
