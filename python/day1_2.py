#!/bin/python
f = open("input2", "r").read()

arrl:int = []
arrr:int = []

similar_dict = {}

i:int = 0
while i < len(f):
    arrl.append(int(f[i:i+5]))
    arrr.append(int(f[i+8:i+13]))
    i+=14;

i = 0
h = 0
while i < len(arrl):
    h = 0
    while h < len(arrr):
        if arrl[i] == arrr[h]:
            if not ((f"{arrl[i]}_" + str(i)) in similar_dict):
                similar_dict[f"{arrl[i]}_" + str(i)] = 1;
            else:
                similar_dict[f"{arrl[i]}_" + str(i)] += 1;
        else:
            if not ((f"{arrl[i]}_" + str(i)) in similar_dict):
                similar_dict[f"{arrl[i]}_" + str(i)] = 0;
        h+=1;
    i+=1;

total:int = 0
i = 0
while i < len(arrl):
    total += arrl[i]*similar_dict[f"{arrl[i]}_" + str(i)]
    i+=1
    
print(total)
