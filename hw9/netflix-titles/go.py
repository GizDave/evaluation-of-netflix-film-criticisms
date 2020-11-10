import os
import sys

#clean
os.system("hdfs dfs -rm -r -f final/netflixshows/netflix_titles/")
#remove class and jar files
os.system("rm *.class")
os.system("rm *.jar")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanNetflixTitlesMapper.java")
#os.system("javac -classpath `yarn classpath` -d . CleanNetflixTitlesReducer.java") #reducer not necessary
os.system("javac -classpath `yarn classpath`:. -d . CleanNetflixTitles.java")
#create jar file
os.system("jar -cvf CleanNetflixTitles.jar *.class")
#run the program
##TODO
os.system('hadoop jar CleanNetflixTitles.jar CleanNetflixTitles /user/"$USER"/dataset/netflixshows/netflix_titles /user/"$USER"/final/netflixshows/netflix_titles/output')
os.system('hdfs dfs -cat final/netflixshows/netflix_titles/ /output/part-r-00000')

print('##DONE##')
