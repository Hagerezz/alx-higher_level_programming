#!/bin/bash
# Usage: ./1-body.sh <URL>
curl -s -o response.txt -w "%{http_code}" "$1" > /dev/null && grep -q "200" response.txt && tail -n +2 response.txt
