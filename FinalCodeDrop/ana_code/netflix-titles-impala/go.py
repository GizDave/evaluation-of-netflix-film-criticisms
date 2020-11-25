import os

#make directory if it doesnt exist
os.system('hdfs dfs -mkdir impalaInput')

# clear previous inputs
os.system('hdfs dfs -rm -r -f impalaInput/netflix-shows')
#make impala input directory
os.system('hdfs dfs -mkdir impalaInput/netflix-shows')

#navigate to 
os.system('hdfs dfs -cp dataset/netflix-shows/cleaned_netflix_titles.csv impalaInput/netflix-shows/cleaned_netflix_titles.csv')
