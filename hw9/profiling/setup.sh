## CURRENTLY UNUSED
# Setup the HDFS directory stucture and populate it. 

# Create new directory structure in HDFS
hdfs dfs -mkdir dataset
hdfs dfs -mkdir dataset/netflix_shows/

# Populate the input directory in HDFS with the input file
hdfs dfs -put filename.ext input_directory

# Verify what is in the input data directory
hdfs dfs -ls input_directory
