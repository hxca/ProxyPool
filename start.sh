#!/bin/bash

python src/ProxyPool.py webserver &
python src/ProxyPool.py schedule
