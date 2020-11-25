import os

##CLEAN
os.system("hdfs dfs -rm -r -f final/netflix-shows/netflix-titles/")

##SETUP 
os.system("hdfs dfs -mkdir final/netflix-shows/netflix-titles/")

##RUN
#remove class and jar files AND csv files output
os.system("rm *.class")
os.system("rm *.jar")
os.system("rm *.csv")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanNetflixTitlesMapper.java")
os.system("javac -classpath `yarn classpath`:. -d . CleanNetflixTitles.java")
#create jar file
os.system("jar -cvf CleanNetflixTitles.jar *.class")
#run the program
os.system('hadoop jar CleanNetflixTitles.jar CleanNetflixTitles /user/"$USER"/dataset/netflix-shows/netflix_titles.csv /user/"$USER"/final/netflix-shows/netflix-titles/output')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/netflix-shows/netflix-titles/output/part-'+'*'+'-00000'+' cleaned_netflix_titles.csv')

##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

os.system('hdfs dfs -rm dataset/netflix-shows/cleaned_netflix_titles.csv')
os.system('hdfs dfs -put cleaned_mubi_ratings_data.csv dataset/mubi/cleaned_mubi_ratings_data.csv')

print('##DONE##')
