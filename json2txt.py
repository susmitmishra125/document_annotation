import json
import os
json_folder = "pdf2json"
text_folder = "pdf2json"
# iterate recursively through the json folder
for root, dirs, files in os.walk(json_folder):
		for filename in files:
				# check if file is a json file
				if filename[-5:]!=".json":
						continue
				# open the json file
				with open(os.path.join(root,filename), 'r') as json_file:
						# load the json file
						json_data = json.load(json_file)
						# print the keys of the json file
						# print(json_data['metadata'].keys())

						
						# get the text from the json file
						# text = json_data['text']
						# write the text to a file
						# textfilename = filename[:-5]+".txt"
						# with open(os.path.join(text_folder,textfilename), 'w', encoding='utf8') as outputFile:
						# 		outputFile.write(text)