#!/bin/bash
# Usage: ./get_response_body.sh <URL>
response=$(curl -s -o /dev/null -w "%{http_code}" "$1") [ "$response" -eq 200 ] && curl -s "$1" || echo "Request failed with status code: $response"
