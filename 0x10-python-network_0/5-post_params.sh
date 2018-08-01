#!/bin/bash
# sends a POST request with variables
curl -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -s "$1"
