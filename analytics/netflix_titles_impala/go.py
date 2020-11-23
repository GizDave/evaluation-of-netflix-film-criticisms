import os

# clear previous inputs
os.system('hdfs dfs -rm -r -f impalaInput')
#make impala input directory
os.system('hdfs dfs -mkdir impalaInput')

#navigate to 
os.system('hdfs dfs -cp dataset/netflix-shows/cleaned_netflix_titles.csv impalaInput/cleaned_netflix_titles.csv')
