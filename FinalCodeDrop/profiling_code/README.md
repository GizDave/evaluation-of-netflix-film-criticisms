the program counts the number of rows in a given csv file

this program assumes your csv file is in 

*./dataset/{dataset-name}/{csv-file-name}*

### TO RUN

> python go.py {dataset-name} {csv-file-name}

run options:

* netflix-shows
  - netflix_titles.csv
    > python go.py netflix-shows netflix_titles.csv
	
    > python go.py netflix-shows cleaned_netflix_titles.csv (generated)
	
* assignment-matrix
  - data.csv
    > python go.py assignment-matrix data.csv
	
	> python go.py assignment-matrix cleaned_data.csv (generated)
    
  - movie_titles.csv
    > python go.py assignment-matrix movie_titles.csv
	
	> python go.py assignment-matrix cleaned_movie_titles.csv (generated)
    
* mubi
  - mubi_lists_data.csv
    > python go.py mubi mubi_lists_data.csv
	
	> python go.py mubi cleaned_mubi_lists_data.csv (generated)
    
  - mubi_movie_data.csv
    > python go.py mubi mubi_movie_data.csv
	
	> python go.py mubi cleaned_mubi_movie_data.csv (generated)
    
  - mubi_ratings_data.csv
    > python go.py mubi mubi_ratings_data.csv
	
	> python go.py mubi cleaned_mubi_ratings_data.csv (generated)