#!/usr/bin/env python3

ignore = [ '/dev', '/home', '/proc', '/mnt' , '/sys', '/lost+found' ]

import os
import os.path

import sys

def key(x):
	return x.replace('/', '\1')

# Moves to the next values in the list of expected files
# Dynamically adds a parent directory if missing
def advance(l, multiple=False):
	discarded = l.pop(0)
	if multiple:
		while l and l[0].startswith(discarded):
			l.pop(0)
	if not l:
		return
	while not discarded.startswith(os.path.dirname(l[0])):
		l.insert(0, os.path.dirname(l[0]))

def advance_dir(l):
	advance(l, True)

def go_through_files(l, path='/'):
	kpath = key(path)
	while l and key(l[0]) < kpath:
		print("Not present: %s%s" % (str(l[0]), '/' if len(l)>1 and l[1].startswith(l[0]) else ''))
		advance_dir(l)
	if not l:
		return
	elif key(l[0]) > kpath:
		print("Not tracked: %s%s" % (path, '/' if os.path.isdir(path) else ''))
	elif key(l[0]) == kpath:
		#print("Matched %s" % path)
		advance(l)
		if os.path.isdir(path) and not os.path.islink(path) and not path in ignore:
			children = sorted(os.listdir(path))
			if path == '/':
				path = ''
			for child in children:
				#print('  Going into ' + path + '/' + child)
				go_through_files(l, path + '/' + child)

if len(sys.argv)!=2:
	print("Usage: find_files_not_owned.py [list of package tracked files]")
	sys.exit(1)

tracked_files = open(sys.argv[1]).read().splitlines()
tracked_files.sort(key=key)
go_through_files(tracked_files)

