import os
import sys

##----START TODO------
#dataset = str(sys.args[0]) #dataset netflix-shows,assignment-netflix,mubi 
#table = str(sys.args[1]) #table 

if (len(sys.argv)==3):
    dataset = str(sys.argv[1])
    table = str(sys.argv[2])
    tableDir = '-'.join(table.split('_'))[0:-4] #make underscores into hyphens 
    
    print("dataset:",dataset)
    print("table:",table)
    
    #CLEAN
#    os.system("hdfs dfs -rm -r -f final/"+dataset+"/"+table)
    print("hdfs dfs -rm -r -f final/"+dataset+"/"+tableDir)
    
    #SETUP
#    os.system("")
    print("hdfs dfs -mkdir final/"+dataset+"/"+tableDir)
    
    #RUN
    #remove class and jar files
#    os.system("rm *.class")
#    os.system("rm *.jar")
    print("rm *.class")
    print("rm *.jar")
    
    #compile
    #os.system("javac -classpath `yarn classpath` -d . ProfileMapper.java")
    #os.system("javac -classpath `yarn classpath` -d . ProfileReducer.java")
    #os.system("javac -classpath `yarn classpath`:. -d . Profile.java")
    print("javac -classpath `yarn classpath` -d . ProfileMapper.java")
    print("javac -classpath `yarn classpath` -d . ProfileReducer.java")
    print("javac -classpath `yarn classpath`:. -d . Profile.java")
    
    #create jar file
#    os.system("jar -cvf Profile.jar *.class")
    print("jar -cvf Profile.jar *.class")
    
    #run program
    #os.system('hadoop jar Profile.jar Profile /user/"$USER"/dataset/'+dataset+"/"+table+' /user/"$USER"/final/'+dataset+"/"+tableDir+'/output')
    print('hadoop jar Profile.jar Profile /user/"$USER"/dataset/'+dataset+"/"+table+' /user/"$USER"/final/'+dataset+"/"+tableDir+'/output')
    
    #DUMP
    #os.system('hdfs dfs -cat /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000')
    print('hdfs dfs -cat /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000')
    
    #GET
    #os.system('hdfs dfs -get /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000 profiled_'+table[0:-4]+'.txt')
    print('hdfs dfs -get /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000 profiled_'+table[0:-4]+'.txt')
    print('##DONE##')
    
##CLEAN
#os.system("hdfs dfs -rm -r -f final/"+directory+inputSrc);
#
###SETUP 
#os.system("hdfs dfs -mkdir final/netflix-shows/netflix-titles/")
#
###RUN
##remove class and jar files
#os.system("rm *.class")
#os.system("rm *.jar")
#
##compile
#os.system("javac -classpath `yarn classpath` -d . ProfileMapper.java")
#os.system("javac -classpath `yarn classpath` -d . ProfileReducer.java")
#os.system("javac -classpath `yarn classpath`:. -d . Profile.java")
##create jar file
#os.system("jar -cvf Profile.jar *.class")
##run the program
#os.system('hadoop jar Profile.jar Profile /user/"$USER"/dataset/netflix-shows/netflix_titles.csv /user/"$USER"/final/netflix-shows/netflix-titles/output')
#
###DUMP (dont dump for large csv files)
#os.system('hdfs dfs -cat final/netflix-shows/netflix-titles/ /user/"$USER"/final/netflix-shows/netflix-titles/output/part-r-00000')
#
##GET FILE TO HADOOP SERVER
#os.system('hdfs dfs -get /user/"$USER"/final/netflix-shows/netflix-titles/output/part-r-00000 cleaned_netflix_titles.csv')
#print('##DONE##')

else:
    print("Usage: <directory-name> <csv-file-name>")
    
##----END TODO------