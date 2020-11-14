import os

##CLEAN
os.system("hdfs dfs -rm -r -f final/mubi/mubi-ratings-data/")

##SETUP 
os.system("hdfs dfs -mkdir final/mubi/mubi-ratings-data/")

##RUN
#remove class and jar files AND csv files output
os.system("rm *.class")
os.system("rm *.jar")
os.system("rm *.csv")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanMubiRatingsMapper.java")
os.system("javac -classpath `yarn classpath`:. -d . CleanMubiRatings.java")
#create jar file
os.system("jar -cvf CleanMubiRatings.jar *.class")
#run the program
os.system('hadoop jar CleanMubiRatings.jar CleanMubiRatings /user/"$USER"/dataset/mubi/mubi_ratings_data.csv /user/"$USER"/final/mubi/mubi-ratings-data/output')

##DUMP (dont dump for large csv files)
#os.system('hdfs dfs -cat final/netflix-shows/netflix-titles/ /user/"$USER"/final/netflix-shows/netflix-titles/output/part-r-00000')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/mubi/mubi-ratings-data/output/part-r-00000 cleaned_mubi_ratings_data.csv')

##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

print('##DONE##')
