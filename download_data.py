from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
api.authenticate()

api.dataset_download_files('clementmsika/mubi-sqlite-database-for-movie-lovers')
api.dataset_download_files('bharath150/assignment-netflix')
api.dataset_download_files('shivamb/netflix-shows')