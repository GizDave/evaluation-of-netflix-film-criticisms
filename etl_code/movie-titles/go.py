import os

##CLEAN
os.system("hdfs dfs -rm -r -f final/assignment-matrix/movie-titles/")

##SETUP 
os.system("hdfs dfs -mkdir final/assignment-matrix/movie-titles/")

##RUN
#remove class and jar files AND csv files output
os.system("rm *.class")
os.system("rm *.jar")
os.system("rm *.csv")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanMovieTitlesMapper.java")
os.system("javac -classpath `yarn classpath`:. -d . CleanMovieTitles.java")
#create jar file
os.system("jar -cvf CleanMovieTitles.jar *.class")
#run the program
os.system('hadoop jar CleanMovieTitles.jar CleanMovieTitles /user/"$USER"/dataset/assignment-matrix/movie_titles.csv /user/"$USER"/final/assignment-matrix/movie-titles/output')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/assignment-matrix/movie-titles/output/part-'+'*'+'-00000'+' cleaned_movie_titles.csv')

##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

os.system('hdfs dfs -rm dataset/assignment-matrix/cleaned_movie_titles.csv')
os.system('hdfs dfs -put cleaned_movie_titles.csv dataset/assignment-matrix/cleaned_movie_titles.csv')

print('##DONE##')
