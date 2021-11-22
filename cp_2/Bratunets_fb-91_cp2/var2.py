import sys

file = open('F:\\GitHub\\fb-labs-2021\\cp_2\\Bratunets_fb-91_cp2\\var2.txt', encoding='utf-8')
alphabet = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
popular = ["о", "е", "ф", "и"]


text = file.read()
def Index(text):
	characters = len(text)
	temp = ""
	r=2
	j=0
	counter=0
	alphcount=0
	Sum=0
	Index=0
	SumBig=0
	keylett = 0
	while r<=32:
		while j<r:
			while counter<characters//r:
				temp += text[counter*r+j]
				counter+=1
				#print(temp)
				if counter == characters//r:
					# if r==30:
					# 		print(temp)
					#print(temp)
					while alphcount<len(alphabet):
						amount = temp.count(alphabet[alphcount])
						Sum += amount*(amount-1)
						alphcount+=1
			Index += Sum/(len(temp)*(len(temp)-1))
			Sum=0
			temp=""
			counter=0
			alphcount=0
			
			j+=1
		# SumBig+= Index/(len(text)*(len(text)-1))
		# if abs(Index/r-0.0553) < 0.005:
		#print(r)
		print(Index/r)
		Index = 0
		SumBig=0
		r+=1
		j=0

def FindKey(text, r):
	characters = len(text)
	temp = ""
	counter=0
	alphcount=0
	mostcommonlettamount = 0
	templettamount = 0
	j=0
	mostcommonlett = ""
	while j<r:
		while counter<characters//r:
			temp += text[counter*r+j]
			counter+=1
			if counter == characters//r:
				for letter in alphabet:
					templettamount = temp.count(letter)
					if templettamount > mostcommonlettamount:
						mostcommonlettamount = templettamount
						mostcommonlett = letter
				for i in popular:
					keylett = (alphabet.index(mostcommonlett) - alphabet.index(i))%len(alphabet)
					print(alphabet[keylett], end=' ')
				print("__")
		temp=""
		counter=0
		mostcommonlettamount = 0
		templettamount = 0
		mostcommonlett = ""
		j+=1


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

def VizinerDecodeNum(value, key):
	i = 0
	j = 0
	lenv = len(value)
	lenk = len(key)
	list_VizEnc = []
	while i < lenv:
		index = (value[i]-key[(j%lenk)])%len(alphabet)
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
	return VizinerEncode(VizinerDecodeNum(EncodeNum(text), EncodeNum(key)))


Index(text)
FindKey(text, 14)
print("____________________________")
FindKey(text, 28)

print(Viziner(text, "последнийдозор"))