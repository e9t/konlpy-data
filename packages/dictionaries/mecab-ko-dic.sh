#! /bin/bash

download_dir="$1"

cd "$download_dir/dictionaries/mecab-ko-dic-1.6.1-20140814"
./configure
sudo ldconfig
make
sudo sh -c 'echo "dicdir=/usr/local/lib/mecab/dic/mecab-ko-dic" > /usr/local/etc/mecabrc'
sudo make install
