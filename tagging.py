import os
import sys
import json
import time
import numpy as np
import pandas as pd
from tqdm import tqdm
from nltk.tokenize import sent_tokenize, word_tokenize
from unidecode import unidecode
# read the document stored in txt files
annotation = 'annotation'
pdfjson = 'pdf2json'
dict = {
	'e_1':[],#METHOD
	'e_2':[],#SOFTWARE
	'e_3':[],#DATASET
	'e_4':[],#METRIC
	'e_5':[],#PARAMETER
	'e_6':[]#AUTHOR
	}
enc = {
	'e_1':'METHOD',
	'e_2':'SOFTWARE',
	'e_3':'DATASET',
	'e_4':'METRIC',
	'e_5':'PARAMETER',
	'e_6':'AUTHOR'
}
def dict_loader(dict):
	# loop through annotation folder
	f = open('negative_dict.txt','r')
	negative_array = f.read().split('\n')
	for filename in tqdm(os.listdir(annotation)):
		if filename.endswith('.json'):
			with open(os.path.join(annotation,filename),'r') as f:
				data = json.load(f)
			data = data['entities']
			try:
				for i in data:
					# print(i['offsets'][0]['text'],i['classId'])
					if i['offsets'][0]['text'] in negative_array or len(i['offsets'][0]['text'])>80:
						continue
					if(unidecode((i['offsets'][0]['text']).strip()) not in dict[i['classId']]):
						dict[i['classId']].append(unidecode(i['offsets'][0]['text'].strip()))
			except UnicodeEncodeError:
				print("UnicodeEncodeError")
	# store the dict in a json file
	for i in dict:
		dict[i] = sorted(dict[i])
	# make the dict to lower
	for i in dict:
		for j in range(len(dict[i])):
			dict[i][j] = dict[i][j].lower()
	with open('dict.json','w') as g:
		json.dump(dict,g)

def tagger(sent,dict):
	# make it to lower
	sent = sent.lower()
	words_list = word_tokenize(sent)
	temp = ' '.join(words_list)
	# labels = np.array(['O']*len(words_list))
	labels = ['O']*len(words_list)
	for i in dict:
		for j in dict[i]:
			j=word_tokenize(j)
			for k in range(len(words_list)):
				if words_list[k:k+len(j)] == j:
					labels[k] = 'B-'+enc[i]
					# labels[k+1:len(j+k)] = 'I-'+enc[i]
					for l in range(1,len(j)):
						labels[k+l] = 'I-'+enc[i]
	return words_list,labels
# loop through the .json files in pdfjson
def formatter(text,header,s):
		sents = sent_tokenize(text)
		for sent in sents:
			s+=header
			words,labels = tagger(sent,dict)
			for i in range(len(words)):
				s+=words[i]+' '+labels[i]+'\n'
			s+='\n'
		return s
# main function
if __name__ == '__main__':
	dict_loader(dict)
	s=''
	count = 0
	document_size = 40
	for filename in tqdm(os.listdir(pdfjson)):
		if count==document_size:
			break
		if filename.endswith(".json"):
			count+=1
			with open(pdfjson+'/'+filename) as f:
				data = json.load(f)
				data = data['metadata']
			
			s=formatter(data['title'],'section TITLE\nid '+pdfjson+'/'+filename+'\n',s)
			s=formatter(data['abstractText'],'section ABSTRACT\nid '+pdfjson+'/'+filename+'\n',s)
			data = data['sections']
			i=0
			for section in data:
				s=formatter(section['text'],'section '+str(i)+'\nid '+pdfjson+'/'+filename+'\n',s)
				i+=1
		# save s to a text file
		if count<=document_size*0.70:
			with open('train.txt','w') as f:
				f.write(s)
		elif count<=document_size*0.85:
			with open('dev.txt','w') as f:
				f.write(s)
		else:
			with open('test.txt','w') as f:
				f.write(s)