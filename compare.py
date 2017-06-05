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

print("Comparing...")

try:
    hasher1 = hashlib.sha256()
    with open(file1, 'rb') as filea:
        buf1 = filea.read()
        hasher1.update(buf1)
        buf1 = None
        filea.close()
        file1hash = (hasher1.hexdigest())
except:
    print("An error occured with the first file.")
    exit()

try:
    hasher2 = hashlib.sha256()
    with open(file2, 'rb') as fileb:
        buf2 = fileb.read()
        hasher2.update(buf2)
        buf2 = None
        fileb.close()
        file2hash = (hasher2.hexdigest())
except:
    print("An error occured with the second file.")
    exit()

if (file1hash == file2hash):
    print("🗹 Files match.\n")
    print(file1 + ": " + file1hash)
    print(file2 + ": " + file2hash)
else:
    print("🗷 Files do not match.\n")
    print(file1 + ": " + file1hash)
    print(file2 + ": " + file2hash)
exit()
