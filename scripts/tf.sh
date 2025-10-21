#!/bin/bash
# Terraform wrapper script that loads environment variables from .env file

set -e  # Exit on error

# Check if .env file exists
if [ ! -f .env ]; then
    echo "Error: .env file not found in project root"
    exit 1
fi

# Load environment variables from .env
set -a
source .env
set +a

# Run terraform with all arguments passed to this script
terraform -chdir=terraform "$@"
