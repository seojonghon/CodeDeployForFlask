#!/bin/bash

cd  /home/ubuntu/hello-flask

echo ">>> run app ------------------------------------"
python3 -u app.py > /dev/null 2> /home/ubuntu/flask.log < /dev/null &
