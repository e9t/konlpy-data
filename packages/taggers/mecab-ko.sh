#! /bin/bash

download_dir="$1"

cd "$download_dir/taggers/mecab-0.996-ko-0.9.1"
./configure
make
make check
sudo make install
