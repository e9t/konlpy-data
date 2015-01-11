#! /bin/bash

download_dir="$1"

cd "$download_dir/converters/eunjeon-mecab-python-0.996-ac44c1e23785"
python setup.py build
sudo python setup.py install
python3 setup.py build
sudo python3 setup.py install
