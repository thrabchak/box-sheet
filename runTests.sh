#!/bin/bash

./env/bin/nosetests --with-coverage --cover-erase --cover-package=src --cover-html $@ 
