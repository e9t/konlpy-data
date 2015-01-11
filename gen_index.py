#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


from glob import glob
import hashlib
import json
import os


MAINDIR = './packages'

def get_id(jsonpath):
    return jsonpath.rsplit(os.path.sep, 1)[-1][:-5]

def get_meta(jsonpath):
    with open(jsonpath, 'r') as f:
        d = json.load(f)

    d['type'] = jsonpath.split(os.path.sep)[1]
    d['filepath'] = os.path.join(d['type'], d['id'])
    filepath = '%s/%s.%s' % (MAINDIR, d['filepath'], d['ext'])
    d['checksum'] = hashlib.md5(open(filepath, 'rb').read()).hexdigest()
    d['size'] = os.path.getsize(filepath)

    return d


if __name__=='__main__':
    package_names = glob('packages/*/*.json')
    packages_info = { get_id(p): get_meta(p) for p in package_names }

    with open('index.json', 'w') as f:
        json.dump(packages_info, f, indent=2)
