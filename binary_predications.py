import os
import sys
import time
# import numpy as np
import pandas as pd
from simpletransformers.classification import ClassificationModel

data_folder = 'pdf2txt'
label_folder = 'count'

sentences = []
counts = []

# loop through the data folder
for filename in os.listdir(data_folder):
		if filename.endswith(".txt"):
				# get the lines in a list from the file
				with open(os.path.join(data_folder, filename), 'r') as f:
					lines = f.readlines()
				# get the label
				with open(os.path.join(label_folder, 'count_'+filename), 'r') as f:
					labels = f.readlines()
				# add the label to the list
				counts=counts+labels
				# add the lines to the list
				sentences=sentences+lines
labels = [int(int(x[0:-1])>0) for x in counts]

df = pd.DataFrame({'text': sentences, 'label': labels})

# split train test
train_df, test_df = df.iloc[:int(len(df)*0.8)], df.iloc[int(len(df)*0.8):]

model = ClassificationModel('bert','bert-base-uncased',args={'fp16':False, 'learning_rate': 3e-5})

model.train_model(train_df)
result, model_outputs, wrong_predictions = model.eval_model(test_df)
# print result
print(result)
print(model_outputs)
print(wrong_predictions)
