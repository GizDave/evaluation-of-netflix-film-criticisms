import os
import sys

##----START TODO------
dataset = str(sys.args[0]) #dataset 1=netflix-shows,2=assignment-netflix,3=mubi 
table = str(sys.args[1]) #table 

if(dataset=="1"): #netflix_titles.csv
    directory = "netflixshows/"
    if(table=="1"):
        inputSrc = "netflix_titles.csv"
elif(dataset=="2"):
    pass
    #TODO
elif(dataset=="3"):
    pass
    #TODO
##----END TODO--------

#clean
os.system("hdfs dfs -rm -r -f final/"+directory+inputSrc)
#remove class and jar files
os.system("rm *.class")
os.system("rm *.jar")
#compile
os.system("javac -classpath `yarn classpath` -d . ProfileMapper.java")
os.system("javac -classpath `yarn classpath` -d . ProfileReducer.java")
os.system("javac -classpath `yarn classpath`:. -d . Profile.java")
#create jar file
os.system("jar -cvf Profile.jar *.class")
#run the program
##TODO
os.system('hadoop jar Profile.jar Clean /user/"$USER"/dataset/'+directory+inputSrc+' /user/"$USER"/final/'+directory+inputSrc+'/output')
os.system('hdfs dfs -cat final/'+directory+inputSrc+'/output/part-r-00000')

print('##DONE##')