#!/bin/bash

ENV_NAME="dataforge"

PYTHON_VERSION="3.9"

PACKAGES=("numpy" "pandas" "matplotlib" "seaborn" "scikit-learn")

if ! command -v conda &> /dev/null; then
    echo "Error: Conda is not installed. Please install Conda first."
    exit 1
fi


if conda env list | grep -q "^$ENV_NAME\s"; then
    echo "Environment '$ENV_NAME' already exists. Use 'conda activate $ENV_NAME' to activate it."
    exit 0
fi


echo "Creating Conda environment '$ENV_NAME' with Python $PYTHON_VERSION..."
conda create -y -n "$ENV_NAME" python="$PYTHON_VERSION"


if [ $? -ne 0 ]; then
    echo "Error: Failed to create the Conda environment."
    exit 1
fi


echo "Activating the environment '$ENV_NAME'..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate "$ENV_NAME"


if [ ${#PACKAGES[@]} -gt 0 ]; then
    echo "Installing packages: ${PACKAGES[*]}..."
    conda install -y "${PACKAGES[@]}"
fi

echo "Conda environment '$ENV_NAME' created and activated successfully!"
echo "Use 'conda activate $ENV_NAME' to activate it in the future."
