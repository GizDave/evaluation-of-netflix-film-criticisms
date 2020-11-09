# Build the jar file and run

# Remove class and jar files
rm *.class
rm *.jar

# Compile
javac -classpath `yarn classpath` -d . ProfileMapper.java
javac -classpath `yarn classpath` -d . ProfileReducer.java
javac -classpath `yarn classpath`:. -d . Profile.java

# Create jar file
jar -cvf Profile.jar *.class

# Run the program
hadoop jar Profile.jar Clean /user/"$USER"/dataset/netflix_shows/netflix_titles.csv /user/"$USER"/final/output

