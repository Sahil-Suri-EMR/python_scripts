#!/usr/bin/python

def testfunc():
	f=open("server_list")
	o=open("my_list","a")
	for line in f.readlines():
		if "zzz" in line:
			print line.strip("\n")
			o.write(line)

testfunc()
