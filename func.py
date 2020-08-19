#!/usr/bin/python

def prnum(num):
	while num <= 30:
		print num
		num+=1

while True:

	num=int(raw_input("enter a number less than 30: "))

	if num <30:
		prnum(num)
		break
	else:
		print "Incorrect number"
