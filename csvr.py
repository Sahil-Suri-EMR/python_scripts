#!/usr/bin/python

import csv

with open("pass.csv") as myf:
	readcsv=csv.reader(myf,delimiter=',')
	for row in readcsv:
		print row[0]
