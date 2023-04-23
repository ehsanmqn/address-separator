#!/bin/bash

# Remove any existing distribution files
rm -rf dist/

# Install latest versions of setuptools and pip
pip install --upgrade setuptools pip

# Build the wheel file
python setup.py sdist bdist_wheel
echo "address-separator packaged successfully"

# Install the wheel file
pip install dist/*.whl
echo "address-separator installed successfully"