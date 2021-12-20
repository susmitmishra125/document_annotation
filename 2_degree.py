# thhis code does 2 things
# 1. read a cleaned text file and seperate sentences
# 2. does binary classification
#   naming convention
# the name of jsonfile shld be --> anno_ + <name of text file>
# for eg if the name text file is abc.txt then name of annotated file shld be anno_abc.json
# both the files shld be in separate folders

import nltk
import json
import os

path_text = r"mention_path_of_textfile_folder"  # r is necessary
path_json = r"mention_path_of_json_folder"  # follow the naming convention above

dir_list = os.listdir(path_text)  # gets the list of files in the foldeer

# looping through all the files ending with .txt
for xFile in dir_list:
    if x.endswith(".txt"):

        # open necessary files
        fTXT = open(path_text + "\\" + xFile, "r", encoding='utf8')
        fSENT = open("sent_" + xFile, "w", encoding='utf8')
        fjson = open(path_json + "\\" + "anno_" +
                     xFile[0:-3] + "json", encoding='utf8')
        fbin = open("bin_" + xFile, "w", encoding='utf8')

        # helper function to convert list to string

        def listToString(s):
            str1 = ""
            for ele in s:
                str1 += ele
                str1 += '\n'
            return str1

        data = fTXT.read()

        # sepearating lines and writing them in a text file
        sentences = nltk.sent_tokenize(data.replace("\n", " "))
        fSENT.write(listToString(sentences))

        # binary classification
        # make list of all the entities in json file
        anno_data = json.load(fjson)
        listw = anno_data["entities"]
        newlist = []

        for a in listw:
            newlist.append(a["offsets"][0]['text'])

        dict2 = {}
        for word in newlist:
            dict2[word] = -1

        count_list = []
        count = 0
        # splitting sentences into words
        for sent in sentences:
            word_list = sent.split()
            for word in word_list:
                try:
                    print(dict[word], end="")
                    count += 1
                except:
                    continue
            count_list.append(count)
            count = 0

        for c in count_list:
            fbin.write(str(c) + "\n")
