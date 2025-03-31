name: Run Python Script

on:  
  push:  
    branches:  
      - main  

jobs:  
  run-python:  
    runs-on: ubuntu-latest  

    steps:  
    - name: Checkout repository  
      uses: actions/checkout@v4  

    - name: Set up Python  
      uses: actions/setup-python@v5  
      with:  
        python-version: '3.10'  

    - name: Install dependencies  
      run: |  
        pip install -r requirements.txt || echo "No requirements"  

    - name: Run Python Script  
      run: python script.py
