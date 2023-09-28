import os
import time

start = time.time()

os.makedirs("./chembl_33",exist_ok=True)

f = open("./chembl_33.sdf","r",encoding="utf-8")
mol = []
mol_count = 0
max_count = 10000

while mol_count < max_count:
    line = f.readline()
    if not line:
        break
    mol.append(line)
    if line[:4]=="$$$$":
        title = mol[0][:-1]
        fo = open(f"./chembl_33/{title}.sdf","w",encoding="utf-8")
        for m in mol:
            fo.write(m)
        fo.close()
        mol = []
        mol_count += 1
    
        if mol_count%1000==0:
            now = time.time()
            print(f"{mol_count} file finished, time={now-start}")

