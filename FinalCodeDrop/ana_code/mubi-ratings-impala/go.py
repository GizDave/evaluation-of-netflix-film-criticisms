import os

# clear previous inputs
os.system('hdfs dfs -rm -r -f impalaInput/mubi-ratings')
#make impala input directory
os.system('hdfs dfs -mkdir impalaInput/mubi-ratings')

os.system('hdfs dfs -cp dataset/mubi/cleaned_mubi_ratings_data.csv impalaInput/mubi-ratings/cleaned_mubi_ratings_data.csv')
