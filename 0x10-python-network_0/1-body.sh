#!/bin/bash
# Usage: ./get_response_body.sh <URL>
curl -s -o /dev/null -w "%{http_code}" "$1" && curl -s "$1"
