import os

##CLEAN
os.system("hdfs dfs -rm -r -f final/mubi/mubi-movie-data/")

##SETUP 
os.system("hdfs dfs -mkdir final/mubi/mubi-movie-data/")

##RUN
#remove class and jar files AND csv files output
os.system("rm *.class")
os.system("rm *.jar")
os.system("rm *.csv")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanMubiMovieMapper.java")
os.system("javac -classpath `yarn classpath`:. -d . CleanMubiMovie.java")
#create jar file
os.system("jar -cvf CleanMubiMovie.jar *.class")
#run the program
os.system('hadoop jar CleanMubiMovie.jar CleanMubiMovie /user/"$USER"/dataset/mubi/mubi_movie_data.csv /user/"$USER"/final/mubi/mubi-movie-data/output')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/mubi/mubi-movie-data/output/part-'+'*'+'-00000'+' cleaned_mubi_movie_data.csv')

##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

os.system('hdfs dfs -rm dataset/mubi/cleaned_mubi_movie_data.csv')
os.system('hdfs dfs -put cleaned_mubi_movie_data.csv dataset/mubi/cleaned_mubi_movie_data.csv')

print('##DONE##')
