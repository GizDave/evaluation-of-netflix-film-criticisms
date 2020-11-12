java -version
yarn classpath

javac -classpath "$(yarn classpath)":. -d . Count.java
jar -cvf count.jar *.class

javac -classpath "$(yarn classpath)":. -d . Clean_data.java
jar -cvf data.jar *.class

javac -classpath "$(yarn classpath)":. -d . Clean_moviesTitles.java
jar -cvf moviesTitles.jar *.class

hdfs dfs -copyFromLocal data.jar
hdfs dfs -copyFromLocal moviesTitles.jar
hdfs dfs -copyFromLocal count.jar

hadoop jar data.jar Clean_data ./dataset/assignment_matrix/data.csv ./data
hadoop jar moviesTitles.jar Clean_moviesTitles dataset/assignment_matrix/movie_titles.csv ./moviesTitles

hadoop jar count.jar Count ./dataset/assignment_matrix/data.csv ./data/count
hadoop jar count.jar Count ./dataset/assignment_matrix/movie_titles.csv ./moviesTitles/count