#!/usr/bin/python

import os

f=open("/etc/fstab")
for line in f.readlines():
	if "nfs" in line:
		dir_list=line.split(" ")
		dir=dir_list[1]
		print dir
		if not os.path.exists(dir):
			os.makedirs(dir)
			print "Created directory: %s" % dir
