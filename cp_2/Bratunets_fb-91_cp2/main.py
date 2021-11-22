import re
file = open('F:\\GitHub\\fb-labs-2021\\cp_2\\Bratunets_fb-91_cp2\\text.txt', encoding='utf-8')
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']

rawtext = file.read()
rawtext = rawtext.lower()
text = re.sub("[”|„|&|$|“|>|+|/|<| |,|.|!|?|-|-|‒|—|;|:|–|-|»|«|-|*|1|2|3|4|5|6|7|8|9|0|#|…|(|)|-|'|№|a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|" "]", "", rawtext)
#text1.find("ё")
text = re.sub(r'\s+', ' ', text)
text = re.sub(r'[a-z]', ' ', text)
text = text.replace("ё", "е")
#text = text1.replace("ё", "е")
text = text.lower()
print(text)

keys = {1: "да",2: "нет",3: "лето",4: "дождь",5: "авиалайнер",6: "раздвигание",7: "автопокрышка",8: "зеленыйслоник",9: "красиваямашина",10: "видеомагнитофон",11: "предусматривание",12: "оловянныйсолдатик",13: "безполезныйчеловек",14: "украинскийпарламент",15: "актуальнаяинформация"}

def EncodeNum(text):
	characters = len(text)
	i=0
	j=0
	list_encodenum = []
	while i<characters:
		while j<len(alphabet):
			if text[i] == alphabet[j]:
				list_encodenum.append(j)
			j+=1
		j=0
		i+=1
	return list_encodenum

def VizinerEncodeNum(value, key):
	i = 0
	j = 0
	lenv = len(value)
	lenk = len(key)
	list_VizEnc = []
	while i < lenv:
		index = (value[i]+key[(j%lenk)])%len(alphabet)
		list_VizEnc.append(index)
		j+=1
		i+=1
	return list_VizEnc

def VizinerEncode(listn):
	characters = len(listn)
	i=0
	j=0
	EncodedText = ""
	while i<characters:
		EncodedText+=alphabet[listn[i]]
		i+=1
	EncodedText+="\n"
	return EncodedText

def Viziner(text, key):
	return VizinerEncode(VizinerEncodeNum(EncodeNum(text), EncodeNum(key)))

file2 = open('encrypted.txt', 'w')
i=0
for i in keys:
	EncodedText = Viziner(text,keys[i])
	file2.write(EncodedText+'\n')

def IndexConform(text):
	characters = len(text)
	i=0
	amount=0
	Index=0
	Sum=0
	while i<len(alphabet):
		amount = text.count(alphabet[i])
		Sum+= amount*(amount-1)
		i+=1
	Index = Sum/(characters*(characters-1))
	return(Index)

print(IndexConform(text))
i=0
for i in keys:
	EncodedText = Viziner(text,keys[i])
	print(IndexConform(EncodedText))

