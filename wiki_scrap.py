# load a text file
f = open('List_of_datasets_for_machine-learning_research.txt', 'r').read()
# find the text between two substrings
x=f.split('<tr>\n<td>')
# print(len(x))
g = open('custom_tags/ML_dataset.txt', 'w')
for i in range(len(x)):
		x[i]=x[i].split('<')[0]
		g.write(x[i])
		# print(x[i])
g.close()