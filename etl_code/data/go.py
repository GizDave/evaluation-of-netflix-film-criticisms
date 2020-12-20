import os

##CLEAN
os.system("hdfs dfs -rm -r -f final/assignment-matrix/data/")

##SETUP 
os.system("hdfs dfs -mkdir final/assignment-matrix/data/")

##RUN
#remove class and jar files AND csv files output
os.system("rm *.class")
os.system("rm *.jar")
os.system("rm *.csv")
#compile
os.system("javac -classpath `yarn classpath` -d . CleanDataMapper.java")
os.system("javac -classpath `yarn classpath`:. -d . CleanData.java")
#create jar file
os.system("jar -cvf CleanData.jar *.class")
#run the program
os.system('hadoop jar CleanData.jar CleanData /user/"$USER"/dataset/assignment-matrix/data.csv /user/"$USER"/final/assignment-matrix/data/output')

#GET FILE TO HADOOP SERVER
os.system('hdfs dfs -get /user/"$USER"/final/assignment-matrix/data/output/part-'+'*'+'-00000'+' cleaned_data.csv')
##delete class and jar files as they are not needed anymore
os.system("rm *.class")
os.system("rm *.jar")

os.system('hdfs dfs -rm dataset/assignment-matrix/cleaned_data.csv')
os.system('hdfs dfs -put cleaned_data.csv dataset/assignment-matrix/cleaned_data.csv')

print('##DONE##')
