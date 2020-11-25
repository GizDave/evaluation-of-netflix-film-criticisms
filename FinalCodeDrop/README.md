# EVALUATION OF NETFLIX FILM CRITICISMS (FALL 2020)
## Jolyne McHaffey, David Shaw, Raymond Shi

### Directory Overview:

**data ingestion**:

This directory is for putting source files into HDFS

/data_ingest

- download_data.py (script to download src files)
- ingestion.sh (script for ingestion data)


**ETL/cleaning code**:

This directory is for cleaning the datasets

/etl_code

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
  -  CleanMubiListMovieReducer.java
  -  CleanMubiMovie.java
  -  CleanMubiMovieMapper.java
  -  go.py
  -  README.md
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

**profiling code**: 

This directory is 1for counting the number of rows in the datasets

/profiling_code

- CountRecs.java
- CountRecsMapper.java
- CountRecsReducer.java
- go.py
- README.md

**analytic code**:

This directory is for analyzing the datasets

/ana_code

**screenshots**: 

This directory is for any relevant screenshots for ingestion, cleaning, profiling, and analyzing

/screenshots

- data
- movie-titles
- mubi-lists
- mubi-movie
- mubi-ratings
- netflix-titles

**test code**: 

This directory contains iscellaneous code

/test_code

**How to build code**:

follow the instructions below

**How to run code**:

**Where to find input data used:**

Once data ingestion and data cleaning is complete, and all the cleaned files are put into HDFS as well, the HDFS home directory should contain the following directory structure: 

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

**Where to find results of run**:

**INSTRUCTIONS**
The three sources of data we use for this project are found here:

1. https://www.kaggle.com/shivamb/netflix-shows
2. https://www.kaggle.com/bharath150/assignment-netflix
3. https://www.kaggle.com/clementmsika/mubi-sqlite-database-for-movie-lovers

**1. Data Ingestion:**

OPTION 1:
- download the files into a local directory: /dataset
- in /data_digest, run:
  > $ sh ingestion.sh

OPTION 2 (if option 1 fails):
1. Download the files directly from the links above
2. Transfer files to dumbo server (scp/ftp) (eg. scp ./yourfilename yourNetID@dumbo.es.its.nyu.edu:/home/yourNetID)
3. Create directories in HDFS ``./dataset`` with the following commands: 
  a. $ hdfs dfs -mkdir ./dataset
  b. $ hdfs dfs -mkdir ./dataset/netflix-shows
  c. $ hdfs dfs -mkdir ./dataset/assignment-matrix
  d. $ hdfs dfs -mkdir ./dataset/mubi
4. Put the datasets into their respective directories
  a. $ hdfs dfs -put netflix_titles.csv dataset/netflix-shows/
  b. $ hdfs dfs -put movie_titles.csv dataset/assignment-matrix/
  c. $ hdfs dfs -put data.csv dataset/assignment-matrix/
  d. $ hdfs dfs -put mubi_lists_data.csv dataset/mubi/
  e. $ hdfs dfs -put mubi_movie_data.csv dataset/mubi/
  f. $ hdfs dfs -put mubi_ratings_data.csv dataset/mubi/

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
