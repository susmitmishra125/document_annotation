import os
import sys
import json
annotation_path = "annotation"
map = {'e_1':"method",'e_2':"software",'e_3':"dataset",'e_4':"metric",'e_5':"parameters",'e_6':"authors",}
# import for intitialize dictionalize for storing the frequency
from collections import defaultdict
# loop through the annotation
dict = defaultdict(int)
doc = 0 
for filename in os.listdir(annotation_path):
	if filename.endswith(".json"):
		doc += 1
		# load the json
		annotation = json.load(open(os.path.join(annotation_path, filename), 'r'))
		# initialise dict to zeros
		for entity in annotation['entities']:
			dict[entity['classId']]+=1
		# sort the dict based on key
sorted_dict = sorted(dict.items(), key=lambda x: x[0])
# print(sorted_dict)
# print dict values devided by 6
for i in range(0,len(sorted_dict)):
	print(map[sorted_dict[i][0]],sorted_dict[i][1]/doc)