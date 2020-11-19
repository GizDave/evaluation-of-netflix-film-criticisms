import sys
from pyspark import SparkContext
from pyspark.sql import SQlContext
from csv import reader

if (len(sys.argv)!=2):
  print('Usage:')
  sys.exit(1)

sc = SparkContext()
lines = sc.textFile(sys.argv[1],1)

#todo