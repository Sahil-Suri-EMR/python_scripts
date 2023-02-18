#!/usr/bin/python

import subprocess 

output=subprocess.check_output("ls -ltr",shell=True)
for line in output.split("\n"):
	if "py" in line:
		print line
