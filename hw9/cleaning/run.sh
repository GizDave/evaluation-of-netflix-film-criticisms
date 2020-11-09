# Build the jar file and run

# Remove class and jar files
rm *.class
rm *.jar

# Compile
javac -classpath `yarn classpath` -d . CleanMapper.java
javac -classpath `yarn classpath` -d . CleanReducer.java
javac -classpath `yarn classpath`:. -d . Clean.java

# Create jar file
jar -cvf Clean.jar *.class

# Run the program
hadoop jar Clean.jar Clean /user/"$USER"/dataset/netflix_shows/netflix_titles.csv /user/"$USER"/final/output

