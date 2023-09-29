conda create -n molvae python=3.9 -y
conda activate molvae
conda install -c conda-forge rdkit -y
conda install -c pytorch pytorch torchvision torchaudio cpuonly -y
#pip install torch torchvision torchaudio #GPU環境を利用する場合はこちらを推奨
conda install -c anaconda scikit-learn -y
conda install -c anaconda seaborn -y
conda install -c conda-forge tqdm -y
python -m pip install pyyaml