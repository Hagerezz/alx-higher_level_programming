#!/bin/bash
# Usage: ./delete_request.sh <URL>
curl -s -X DELETE "$1"
