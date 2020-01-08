#!/bin/bash

python ProxyPool.py webserver &
python ProxyPool.py schedule
