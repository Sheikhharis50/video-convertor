#!/bin/bash
set -e

echo 'fetching updates.'
sudo apt update

echo 'installing python.'
sudo apt install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3
python --version

echo 'installing ffmpeg package.'
sudo apt install ffmpeg
ffmpeg -version

echo 'creating and activating python virtual environment.'
python -m venv venv
source venv/bin/activate

