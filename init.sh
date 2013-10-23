#!/bin/bash

virtualenv venv -v
source venv/bin/activate
pip install -U -r requirements.txt
