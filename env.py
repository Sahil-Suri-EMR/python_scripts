#!/usr/bin/python

import os

name=(os.getenv('NAM') or 'idk')

if name.startswith('sa'):
	print "%s is a good name" % name
else:
	print "%s could do better" % name
