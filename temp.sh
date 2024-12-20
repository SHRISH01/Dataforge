#!/bin/bash

# Temporarily disable Conda auto-activation
export CONDA_AUTO_ACTIVATE_BASE=false

# Unset Conda environment variables if they exist
unset CONDA_DEFAULT_ENV
unset CONDA_PREFIX
unset CONDA_PROMPT_MODIFIER

# Check if the venv directory exists
if [ ! -d "./venv" ]; then
    echo "Virtual environment 'venv' not found. Creating one..."
    python3 -m venv venv
fi

# Activate the local venv environment
echo "Activating the virtual environment 'venv'..."
source venv/bin/activate

# Confirm the activation
if [ "$VIRTUAL_ENV" ]; then
    echo "Virtual environment 'venv' activated successfully."
else
    echo "Failed to activate the virtual environment 'venv'."
fi
