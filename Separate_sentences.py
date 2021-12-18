import nltk


def listToString(s):

    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele
        str1 += '\n'

    # return string
    return str1


fp = open("2021.acl-long.1.txt", "r", encoding='utf8')
data = fp.read()

# first remove newline and replace it with a string
print(data.replace("\n", " "))

sentences = nltk.sent_tokenize(data.replace("\n", " "))

fp2 = open("sent.2021.acl-long.1.txt", "w", encoding='utf8')
fp2.write(listToString(sentences))
