import os
import json

json_folder = "annotation"
text_folder = "pdf2txt"
bin_folder = "count"
# check if folder exists if not create it
if not os.path.exists(bin_folder):
    os.makedirs(bin_folder)

# load json as a dictionary
# and then make a list of all the entities

ent_list = []  # list to store the entities
ent_dict = {}  # dict to store unique entities
for filename in os.listdir(json_folder):
    if filename[-5:] != ".json":  # only process json files
        continue
    json_file_path = os.path.join(json_folder, filename)
    f = open(json_file_path, encoding='UTF8')
    JsonF = json.load(f)
    list_1 = JsonF["entities"]
    for a in list_1:
      if len(a["offsets"][0]['text'].lower())>3:
        ent_list.append(a["offsets"][0]['text'].lower())
    for word in ent_list:
        ent_dict[word] = -1
    f.close()
# reading from the text file and counting the frequency
for filename in os.listdir(text_folder):
    if filename[-4:] != ".txt":  # only process txt files
        continue
    file_path = os.path.join(text_folder, filename)
    txt_file = open(file_path, 'r', encoding='UTF8')
    text_corp = txt_file.read()
    # splitting into sentences
    count_list = []  # to store frequency
    sentences = text_corp.split("\n")
    for sent in sentences:
        count = 0
        for word in ent_list:
            if word in sent:
                count += 1
        count_list.append(count)
    # writing the count_list in a doc
    bin_file = "count_" + filename
    with open(os.path.join(bin_folder, bin_file), 'w', encoding='utf8') as outputFile:
        for num in count_list:
            outputFile.write(str(num))
            outputFile.write("\n")
