module load python/gnu/2.7.11

pip install --user kaggle

python download_data.py

mkdir dataset

mv *.zip dataset

cd dataset

unzip "*.zip"

cd ..

hdfs dfs -mkdir ./dataset/
hdfs dfs -mkdir ./dataset/netflix_shows/
hdfs dfs -mkdir ./dataset/assignment_matrix/
hdfs dfs -mkdir ./dataset/mubi/

hdfs dfs -copyFromLocal dataset/netflix_titles.csv 
hdfs dfs -copyFromLocal dataset/combined_data_1.txt
hdfs dfs -copyFromLocal dataset/combined_data_2.txt
hdfs dfs -copyFromLocal dataset/combined_data_3.txt
hdfs dfs -copyFromLocal dataset/combined_data_4.txt
hdfs dfs -copyFromLocal dataset/movie_titles.csv
hdfs dfs -copyFromLocal dataset/data.csv
hdfs dfs -copyFromLocal dataset/mubi_lists_data.csv
hdfs dfs -copyFromLocal dataset/mubi_movie_data.csv
hdfs dfs -copyFromLocal dataset/mubi_ratings_data.csv

hdfs dfs -mv netflix_titles.csv ./dataset/netflix_shows/
hdfs dfs -mv combined_data_1.txt combined_data_2.txt combined_data_3.txt combined_data_4.txt movie_titles.csv data.csv ./dataset/assignment_matrix/
hdfs dfs -mv mubi_lists_data.csv mubi_movie_data.csv mubi_ratings_data.csv ./dataset/mubi/

hdfs dfs -setfacl -m user:...:rw- ./dataset
hdfs dfs -setfacl -m user:...:rw- ./dataset

rm -r dataset
