## not functional yet
import sys
from pyspark import SparkContext, SparkConf
from csv import reader

def get_year(line):
  pass
  year = line[6]
  return year

def get_desc(line):
  pass
  return line[10]

if __name__ == "__main__":
  
  sc = SparkContext()
  line = sc.textFile('dataset/netflix-shows/cleaned_netflix_titles.csv')
  
  line = line.map(lambda line : line.lower())
#  line = line.mapPartitions(lambda x: reader(x))
  tokens = line.flatMap(lambda l: l.split(',(?=([^\"]*\"[^\"]*\")*[^\"]*$)'))
  
  yearDesc = tokens.map(lambda token:())
  
  
  # spark action
  line.saveAsTextFile('netflix_titles_test.out')
  
  sc.stop()
  