# Evaluation of Netflix Film Criticisms (FALL 2020)
## Jolyne McHaffey, David Shaw, Raymond Shi

### Directory Overview:

*the python/shell scripts written for this project are to facilitate the compilation process*

**/data_ingest**:

This directory is for data ingestion

- download_data.py (script to download source files)
- ingestion.sh (script for ingestion data)


**/etl_code**:

This directory is for ETL/cleaning code

- /data
  - CleanData.java
  - CleanDataMapper.java
  - CleanDataReducer.java
  - go.py 
  - README.md
- /movie-titles
  - CleanMovieTitles.java
  - CleanMovieTitlesMapper.java
  - CleanMovieTitlesReducer.java
  - go.py 
  - README.md
- /mubi-lists
  - CleanMubiLists.java
  - CleanMubiListsMapper.java
  - CleanMubiListsReducer.java
  - go.py
  - README.md
- /mubi-movie
  - CleanMubiListMovieReducer.java
  - CleanMubiMovie.java
  - CleanMubiMovieMapper.java
  - go.py
  - README.md
- /mubi-ratings
  - CleanMubiRatings.java
  - CleanMubiRatingsMapper.java
  - CleanMubiRatingsReducer.java
  - go.py
  - README.md
- /netflix-titles
  - CleanNetflixTitles.java
  - CleanNetflixTitlesMapper.java
  - CleanNetflixTitlesReducer.java
  - go.py
  - README.md

**/profiling_code**: 

This directory is for profiling code

- CountRecs.java
- CountRecsMapper.java
- CountRecsReducer.java
- go.py
- README.md

**/ana_code**:

This directory is for analytic code

**/screenshots**: 

This directory is for any relevant screenshots for the analytics

- data
- movie-titles
- mubi-lists
- mubi-movie
- mubi-ratings
- netflix-titles

**/test_code**: 

This directory contains miscellaneous code

***
## INSTRUCTIONS

The three sources of data we use for this project are found here:

1. https://www.kaggle.com/shivamb/netflix-shows
2. https://www.kaggle.com/bharath150/assignment-netflix
3. https://www.kaggle.com/clementmsika/mubi-sqlite-database-for-movie-lovers

**1. Data Ingestion:**

OPTION 1:

in /data_digest, run: ``$ sh ingestion.sh``

OPTION 2 (if option 1 fails):
1. Download the files directly from the links above
2. Transfer files to dumbo server (scp/ftp) (eg. scp ./yourfilename yourNetID@dumbo.es.its.nyu.edu:/home/yourNetID)
3. Create directories in HDFS ``./dataset`` with the following commands: 
    ```
    $ hdfs dfs -mkdir ./dataset
    $ hdfs dfs -mkdir ./dataset/netflix-shows
    $ hdfs dfs -mkdir ./dataset/assignment-matrix
    $ hdfs dfs -mkdir ./dataset/mubi
    ```
4. Put the datasets into their respective directories
    ```
    $ hdfs dfs -put netflix_titles.csv dataset/netflix-shows/
    $ hdfs dfs -put movie_titles.csv dataset/assignment-matrix/
    $ hdfs dfs -put data.csv dataset/assignment-matrix/
    $ hdfs dfs -put mubi_lists_data.csv dataset/mubi/
    $ hdfs dfs -put mubi_movie_data.csv dataset/mubi/
    $ hdfs dfs -put mubi_ratings_data.csv dataset/mubi/
    ```
After the files are put into HDSF, the directory should follow this structure:

> $ hdfs dfs -ls dataset/

```
.
└── dataset/
    ├── assignment-matrix/
    │   ├── data.csv
    │   ├── movie_titles.csv
    ├── mubi/
    │   ├── mubi_lists_data.csv
    │   ├── mubi_movie_data.csv
    │   └── mubi_ratings_data.csv
    └── netflix-shows/ 
        └── netflix_titles.csv

```
**2. Data Cleaning**

navigate to the /etl_code directory

OPTION 1:

run the python scripts to clean each dataset and upload the cleaned dataset to HDFS

- clean data.csv
    - run ``python go.py``
- clean movie_titles.csv 
    - run ``python go.py``
 - clean mubi_lists.csv
    - run ``python go.py``
 - clean mubi_movies.csv
    - run ``python go.py``
 - clean mubi_ratings.csv
    - run ``python go.py``
 - clean netflix_titles.csv
    - run ``python go.py``

OPTION 2 (if option 1 fails):

- for each dataset:
    - ``javac -classpath `yarn classpath` -d . {mapper-file-name}.java``
    - ``javac -classpath `yarn classpath`:. -d . {job-file-name}.java``
    - ``jar -cvf {job-file-name}.jar *.class``
    - ``hadoop jar {job-file-name}.jar {job-file-name} {dataset-path} {output-path}``
    - ``hdfs dfs -get {output-file} cleaned_{dataset-name}.csv``
	- ``hdfs dfs -put {output-file} {hdfs-directory-path}``
	
Once done, the hdfs dataset directory should follow this structure: 

> $ hdfs dfs -ls dataset/
```
.
└── dataset/
    ├── assignment-matrix/
    │   ├── data.csv
    │   ├── movie_titles.csv
    │   ├── cleaned_data.csv
    │   └── cleaned_movie_titles.csv
    ├── mubi/
    │   ├── mubi_lists_data.csv
    │   ├── mubi_movie_data.csv
    │   ├── mubi_ratings_data.csv
    │   ├── cleaned_mubi_lists_data.csv
    │   ├── cleaned_mubi_movie_data.csv
    │   └── cleaned_mubi_ratings_data.csv
    └── netflix-shows/ 
        ├── netflix_titles.csv
        └── cleaned_netflix_titles.csv

```
**3. Data Profiling**

navigate to the /profiling_code directory

for each dataset, run ``python go.py <directory-name> <csv-file-name>``
```
$ python go.py assignment-matrix data.csv
$ python go.py assignment-matrix cleaned_data.csv
$ python go.py assignment-matrix movie_titles.csv
$ python go.py assignment-matrix cleaned_movie_titles.csv
$ python go.py mubi mubi_lists_data.csv
$ python go.py mubi cleaned_mubi_lists_data.csv
$ python go.py mubi mubi_movie_data.csv
$ python go.py mubi cleaned_mubi_movie_data.csv
$ python go.py mubi mubi_ratings_data.csv
$ python go.py mubi cleaned_mubi_ratings_data.csv
$ python go.py netflix-shows netflix_titles.csv
$ python go.py netflix-shows cleaned_netflix_titles.csv
```
After profiling is complete, you should see 12 profiled .txt files for each dataset in the current directory.

**4. Data Analytics**

//todo


mubi_ratings_data.csv analytics with impala:
- in ana_code/mubi-ratings-impala
  - run ``python go.py`` to set impala input directory
  - check if directory is properly set:
    - ``hdfs dfs -ls impalaInput/mubi-ratings``
  - check usage.txt for instructions

netflix_titles.csv analytics:
- in ana_code/netflix-titles-impala
  - run ``python go.py`` to set impala input directory
  - check if directory is properly set:
    - ``hdfs dfs -ls impalaInput/netflix-titles``
  - check usage.txt for instructions
  













