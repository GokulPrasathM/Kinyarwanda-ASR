#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Install dependencies
pip install -r requirements.txt

# Run data collection script
python recipes/data_collect.py

# Run fine-tuning script
python recipes/finetune.py