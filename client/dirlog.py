import os
import csv
import copy

olddirs = {}
dirs = {}

def getDirs():
	global olddirs
	global dirs
	flag = "Y"
	isModified = False
	if not os.path.isfile("dirlog.csv"):
		while flag == "Y":
			temp = raw_input("Path of the Directory you want to link?")
			dirs[temp] = os.walk(temp).next()[1]
			flag = raw_input("Do you want to link another directory?(Y/N)")
		w = csv.writer(open("dirlog.csv", "w"))
		for key, val in dirs.items():
			w.writerow([key, val])
		isModified = True
	else:
		if not olddirs:
			for key,val in csv.reader(open("dirlog.csv")):
				olddirs[key] = val
		for key, val in olddirs.items():
			dirs[key] = os.walk(key).next()[1]
		if dirs!=olddirs:
			w = csv.writer(open("dirlog.csv", "w"))
			for key, val in dirs.items():
				w.writerow([key, val])
			isModified = True
	olddirs = copy.deepcopy(dirs)
	dirs.clear()
	print isModified
	content = ""
	for key, val in olddirs.items():
		content = content+key+":"+"$".join(val)+","
	return content[:-1], isModified