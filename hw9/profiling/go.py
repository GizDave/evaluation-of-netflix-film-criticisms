import os
import sys

if (len(sys.argv)==3):
    dataset = str(sys.argv[1]) #dataset netflix-shows,assignment-netflix,mubi 
    table = str(sys.argv[2])
    tableDir = '-'.join(table.split('_'))[0:-4] #make underscores into hyphens 

    #CLEAN
    os.system("hdfs dfs -rm -r -f final/"+dataset+"/"+tableDir)
    
    #SETUP
    os.system("hdfs dfs -mkdir final/"+dataset+"/"+tableDir)
    
    #RUN
    #remove class and jar files AND the previous output of same csv
    os.system("rm *.class")
    os.system("rm *.jar")
    os.system("rm profiled_"+table[0:-4]+'.txt')
    
    #compile
    os.system("javac -classpath `yarn classpath` -d . CountRecsMapper.java")
    os.system("javac -classpath `yarn classpath` -d . CountRecsReducer.java")
    os.system("javac -classpath `yarn classpath`:. -d . CountRecs.java")
    
    #create jar file
    os.system("jar -cvf CountRecs.jar *.class")
    
    #run program
    os.system('hadoop jar CountRecs.jar CountRecs /user/"$USER"/dataset/'+dataset+"/"+table+' /user/"$USER"/final/'+dataset+"/"+tableDir+'/output')
    
    #DUMP
    os.system('hdfs dfs -cat /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000')
    
    #GET
    os.system('hdfs dfs -get /user/"$USER"/final/'+dataset+'/'+tableDir+'/output/part-r-00000 profiled_'+table[0:-4]+'.txt')
    print('##DONE##')
else:
    print("Usage: <directory-name> <csv-file-name>")