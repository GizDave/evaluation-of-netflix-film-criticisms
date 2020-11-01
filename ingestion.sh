module load python/gnu/2.7.11

pip install --user kaggle

python download_data.py

mkdir dataset

mv *.zip dataset

cd dataset

unzip "*.zip"
