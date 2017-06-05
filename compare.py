#!/usr/bin/python3

import sys
import hashlib

try:
    file1 = sys.argv[1]
    file2 = sys.argv[2]
except:
    print("I need two files you idiot!")
    exit()

try:
    open(file1, 'r')
except FileNotFoundError:
    print("Cannot open " + file1)
    exit()

try:
    open(file2, 'r')
except FileNotFoundError:
    print("Cannot open " + file2)
    exit()

try:
    hasher1 = hashlib.md5()
    with open(file1, 'rb') as file1:
        buf1 = file1.read()
        hasher1.update(buf1)
    file1hash = (hasher1.hexdigest())
except:
    print("An error occured with the first file.")
    exit()

try:
    hasher2 = hashlib.md5()
    with open(file2, 'rb') as file2:
        buf2 = file2.read()
        hasher2.update(buf2)
    file2hash = (hasher2.hexdigest())
except:
    print("An error occured with the second file.")
    exit()

if (file1hash == file2hash):
    print("🗹 Files match.")
else:
    print("🗷 Files do not match.")

exit()
