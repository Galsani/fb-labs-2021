import math
import re

file = open('F:\\GitHub\\fb-labs-2021\\cp_1\\Bratunets_fb-91_cp1\\text.txt', encoding='utf-8')

alphabet_sm = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ы','ь','э','ю','я']

rawtext = file.read()
rawtext = rawtext.lower()
text = re.sub("[”|„|&|$|“|>|+|/|<| |,|.|!|?|-|-|‒|—|;|:|–|-|»|«|-|*|1|2|3|4|5|6|7|8|9|0|#|…|(|)|-|'|№|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z]", " ", rawtext)
# text = re.sub("^\s+|\n|\r|\s+$", '', text)
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[a-z]', ' ', text)
text = text.lower()
text = text.replace("ё", "е")
text = text.replace("ъ", "ь")
characters = len(text)

file2 = open('text2.txt', 'w')
file2.write(text)

textwoutspaces = text.replace(" ", "")
lentextwoutspaces = len(textwoutspaces)

file3 = open('text3.txt', 'w')
file3.write(textwoutspaces)

def count_frequency_with_spaces():
	i=0
	while i<31:
		print(text.count(alphabet_sm[i])/characters)
		i+=1
	print((text.count(" "))/characters)

def count_frequency_without_spaces():


	i=0
	while i<31:
		print(textwoutspaces.count(alphabet_sm[i])/lentextwoutspaces)
		i+=1

def amountofbigrmswithoutspaces():
	i=0
	j=0
	Sum=0
	while i<31:
		while j<31:
			amount = textwoutspaces.count(alphabet_sm[i]+alphabet_sm[j])
			Sum+=amount
			j+=1
			amount=0
		j=0
		i+=1
	return Sum

def amountofbigrmswithspace():
	i=0
	j=0
	Sum=0
	while i<31:
		while j<31:
			amount = text.count(alphabet_sm[i]+alphabet_sm[j])
			Sum+=amount
			j+=1
			amount=0
		j=0
		i+=1
	return Sum

amountofbigrmswithspace = amountofbigrmswithspace()
amountofbigrmswithoutspaces = amountofbigrmswithoutspaces()

def count_bigrams_with_spaces():
	
	i=0
	j=0
	amount = 0
	while i<31:
		while j<31:
			amount = text.count(alphabet_sm[i]+alphabet_sm[j])
			print(round((amount/amountofbigrmswithspace), 7))
			j+=1
			amount=0

		j=0
		i+=1

def count_bigrams_without_spaces():
	i=0
	j=0
	amount = 0
	while i<31:
		while j<31:
			amount = textwoutspaces.count(alphabet_sm[i]+alphabet_sm[j])
			print(round((amount/amountofbigrmswithoutspaces), 7))
			j+=1
			amount=0
		j=0
		i+=1

def H1_with_spacebars():

	Sum = 0
	i = 0
	while i<31:
		P = text.count(alphabet_sm[i])/characters
		Sum += P * math.log2(P)
		i += 1
	P = text.count(" ")/characters
	Sum += P * math.log2(P)
	print("H1 with spaces:%1f"%(-Sum))


def H1_without_spacebars():

	Sum = 0
	i = 0
	while i<31:
		P = textwoutspaces.count(alphabet_sm[i])/lentextwoutspaces
		Sum += P * math.log2(P)
		i += 1
	print("H1 without spaces:%1f"%(-Sum))

def H2_with_spacebars():

	Sum = 0
	i=0
	j=0
	P = 0
	amount = 0
	while i<31:
		while j<31:
			amount = text.count(alphabet_sm[i]+alphabet_sm[j])
			P = amount/amountofbigrmswithspace
			if P!=0:
				Sum += P * math.log2(P)
			j+=1
			amount=0

		j=0
		i+=1
	print("H2 with spaces:%1f"%(-Sum/2))

def H2_without_spacebars():
	Sum = 0
	i=0
	j=0
	P = 0
	amount = 0
	while i<31:
		while j<31:
			amount = textwoutspaces.count(alphabet_sm[i]+alphabet_sm[j])
			P = amount/amountofbigrmswithoutspaces
			if P!=0:
				Sum += P * math.log2(P)
			j+=1
			amount=0

		j=0
		i+=1
	print("H2 without spaces:%1f"%(-Sum/2))

def bigramSTEP2_frequency_with_spacebars():
	res = 0
	d = {}
	ind =0 
	j=0
	while ind<31:
	 	while j<31:
	 		d[alphabet_sm[ind]+alphabet_sm[j]]=0
	 		j+=1
	 	ind+=1
	 	j=0
	bigram = ""
	i = 0
	count = 0
	length = len(text)
	while i<length:
		if text[i]==" " or text[i+1]==" ":
			i+=2
		else:
			bigram = (text[i]+text[i+1])
			d[bigram] += 1
			i+=2
	res = sum(d.values())

	# print(d)
	# print(res)
	for bigram in d:
		d[bigram] = float(d[bigram]/res)
	list_keys = list(d.keys())
	list_keys.sort()
	# for i in list_keys:
	# 	print(i)
	# for i in list_keys:
	# 	print(d[i])
	Sum = 0
	for bigram in d:
		if d[bigram]!=0:
			Sum += (d[bigram])*math.log2(d[bigram])
	print("H2Step2 with spaces:%1f"%(-Sum/2))


def bigramSTEP2_frequency_without_spacebars():
	res = 0
	d = {}
	ind =0 
	j=0
	while ind<31:
	 	while j<31:
	 		d[alphabet_sm[ind]+alphabet_sm[j]]=0
	 		j+=1
	 	ind+=1
	 	j=0
	bigram = ""
	i = 0
	count = 0
	length = len(textwoutspaces)
	while i<length-1:
		bigram = (textwoutspaces[i]+textwoutspaces[i+1])
		d[bigram] += 1
		i+=2
	res = sum(d.values())

	# print(d)
	# print(res)
	for bigram in d:
		d[bigram] = float(d[bigram]/res)
	list_keys = list(d.keys())
	list_keys.sort()
	# for i in list_keys:
	# 	print(i)
	# for i in list_keys:
	# 	print(d[i])

	Sum = 0
	for bigram in d:
		if d[bigram]!=0:
			Sum += (d[bigram])*math.log2(d[bigram])
	print("H2Step2 without spaces:%1f"%(-Sum/2))


count_frequency_with_spaces()
count_frequency_without_spaces()

# count_bigrams_without_spaces()
# count_bigrams_with_spaces()

H1_with_spacebars()
H2_with_spacebars()

H1_without_spacebars()
H2_without_spacebars()

# print(characters)
# print(lentextwoutspaces)

# d = dict().fromkeys(set(text))
# for k in d.keys():
#     d[k] = text.count(k)
#     print(k, d[k])

bigramSTEP2_frequency_with_spacebars()
bigramSTEP2_frequency_without_spacebars()
