#!/bin/python
f = open("testinput", "r").read()

arrl:int = []
arrr:int = []

i:int = 0
while i < len(f):
    arrl.append(int(f[i:i+5]))
    arrr.append(int(f[i+8:i+13]))
    i+=14;
