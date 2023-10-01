conda create -n molvae python=3.9 -y
conda install -c conda-forge rdkit -y
conda install -c pytorch pytorch torchvision torchaudio cpuonly -y
conda install -c anaconda scikit-learn -y
conda install -c conda-forge tdqm -y
python -m pip install pyyaml