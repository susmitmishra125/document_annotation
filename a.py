# from unidecode import unidecode
# x="\ud835"
# try:
# 	if True:
# 		print(x)
# except UnicodeEncodeError:
# 	print("unicode error")
	
# print(unidecode(x))
# https://huggingface.co/allenai/scibert_scivocab_uncased/raw/main/config.json
# https://huggingface.co/allenai/scibert_scivocab_uncased/resolve/main/pytorch_model.bin
# https://huggingface.co/allenai/scibert_scivocab_uncased/raw/main/vocab.txt

from transformers import *
tokenizer = AutoTokenizer.from_pretrained('model_scibert')
model = AutoModel.from_pretrained('model_scibert')
# print(summary(model))
from keras.utils import plot_model
plot_model(model, to_file='bert.png')
print(tokenizer.encode("This is a sentence"))
