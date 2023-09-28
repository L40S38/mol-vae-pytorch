from rdkit import Chem
from rdkit.Chem import Draw
import glob

sdfs = glob.glob("./chembl_33/*.sdf")
output_file = open("output.txt","w",encoding="utf-8")

for sdf in sdfs:

    suppl = Chem.SDMolSupplier(sdf)
    mols = [x for x in suppl if x is not None] #./now.sdfに含まれる分子をmolオブジェクトにしたもののリスト

    print(len(mols))

    # get property name

    for prop in mols[0].GetPropNames():
        output_file.write('{}: {}\n'.format(prop, mols[0].GetProp(prop)))

output_file.close()