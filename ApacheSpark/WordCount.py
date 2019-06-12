# WordCount.py

import sys
from pyspark import SparkContext

if __name__=="__main__": 
	sc= SparkContext("local[2]","word count")
 
	sc.setLogLevel("ERROR")

	lines= sc.textFile("word_count.text")
 
	words= lines.flatMap(lambda line:line.split(" "))

	wordCounts= words.countByValue()
	for words, count in wordCounts.items():
		print(words, count)s