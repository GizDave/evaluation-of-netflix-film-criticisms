# Data Cleaning (ETL) and Profiling Code
## Jolyne McHaffey, David Shaw, Raymond Shi


The directories contains a mapreduce program for either cleaning or profiling the dataset

total: 7 mapreduce programs (6 cleaning, 1 profiling)

**The code assumes the hdfs directory structure is as follows:**
```
.
└── dataset/
    ├── assignment-matrix/
    │   ├── data.csv
    │   ├── movie_titles.csv
    │   └── cleaned_{data/movie_titles}.csv (generated)
    ├── mubi/
    │   ├── mubi_lists_data.csv
    │   ├── mubi_movie_data.csv
    │   ├── mubi_ratings_data.csv
    │   └── cleaned_mubi_{lists/movie/ratings}_data.csv (generated)
    └── netflix-shows/ 
        ├── netflix_titles.csv
        └── cleaned_netflix_titles.csv (generated)

```

### netflix-titles

* netflix_titles.csv
	> /netflix-titles

### assignment-matrix

* movie_titles.csv 
	> /movie-titles

* data.csv 
	> /data

### mubi

* mubi_lists_data.csv
	> /mubi-lists

* mubi_movie_data.csv 
	> /mubi-data

* mubi_ratings_data.csv 
	> /mubi-ratings

### generic dataset profiling

> /profiling