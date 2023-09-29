#!/bin/bash
# Usage: ./post_with_variables.sh <URL>
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
