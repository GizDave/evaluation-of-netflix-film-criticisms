import os

# clear previous inputs
os.system('hdfs dfs -rm -r -f impalaInput')
#make impala input directory
os.system('hdfs dfs -mkdir impalaInput')

#navigate to 
os.system('hdfs dfs -cp dataset/mubi/cleaned_mubi_ratings_data.csv impalaInput/cleaned_mubi_ratings_data.csv')
