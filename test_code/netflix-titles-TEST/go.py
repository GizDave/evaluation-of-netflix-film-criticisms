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
os.system("javac -classpath `yarn classpath` -d . CleanMapper.java")
os.system("javac -classpath `yarn classpath` -d . CleanReducer.java")
os.system("javac -classpath `yarn classpath`:. -d . Clean.java")
#create jar file
os.system("jar -cvf Clean.jar *.class")
#run the program
os.system('hadoop jar Clean.jar Clean /user/"$USER"/dataset/netflix-shows/netflix_titles.csv /user/"$USER"/final/netflix-shows/netflix-titles/output')

##DUMP (dont dump for large csv files)
#os.system('hdfs dfs -cat final/netflix-shows/netflix-titles/ /user/"$USER"/final/netflix-shows/netflix-titles/output/part-r-00000')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/netflix-shows/netflix-titles/output/part-'+'*'+'-00000'+' cleaned_netflix_titles.csv')

##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

print('##DONE##')
