
import csv
import numpy as np
import os 
import shutil
import glob

# read data from file

name = []
obj_id = []
meta_id = []


with open('../can.csv', 'rb') as f:
    reader = csv.reader(f) #csv read object file
    next(reader) # skip the headers
    i=0
    for row in reader:
		META_ID = row[1]
		if META_ID[0] == '0':
			META_ID = row[1][1:8]
		else:
			META_ID = row[1][0:8]
		ID = row[0]
		NAME = row[5]
		
		meta_id.append('0'+ META_ID)
		name.append(NAME)
		obj_id.append(ID[4:])

directory = '~/Downloads/ShapeNetCore.v2/'
dest = os.path.join("~/Downloads/shapenet_models")
meta_id = list(set(meta_id))
for item in meta_id:
	if os.path.isdir(item):
		# find folder 
		os.chdir(item)
		# for each obj in class go in and rename according to its name
		for obj_class in obj_id: 
			if os.path.isdir(obj_class):
				obj_name = name[obj_id.index(obj_class)]
				print obj_name
				print os.getcwd()
				os.chdir(obj_class+"/models")
				for fileName in os.listdir("."):
					os.rename(fileName, fileName.replace("model_normalized", obj_name))
				os.chdir(directory+item)
		# for each obj_class in item go in and rename according to its name
		for obj_class in obj_id:
			if os.path.isdir(obj_class): 
				os.chdir(obj_class+"/models")
				for file in [glob.glob('*.obj'), glob.glob('*.mtl')]:
					shutil.copy2(file[0], dest)
				os.chdir(directory+item)
		os.chdir(directory)
    	



