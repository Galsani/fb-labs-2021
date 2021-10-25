#!/usr/bin/env python
# coding: utf-8

# In[5]:

import collections
import numpy
text = ''
with open("1.txt", 'r', encoding="utf-8") as file:
    text = file.read()
alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']
text = text.replace(' ', '').replace('ё', '').replace('.','').replace(',','').replace('-','').replace('\n','').lower()
#print(text,'\n')


def ind_vid(line):#OK
    alp = sorted(line)
    alpcount = alphabet
    alpcount = dict((k,0) for k in alpcount)

    temp = dict(collections.Counter(alp))
    for i in temp:
        alpcount[i] = temp[i]
    
    sum = 0
    for i in alphabet:
        sum += alpcount[i]*(alpcount[i]-1)
    I = (1/(len(line)*(len(line) -1)))*sum
    return I

def encode(line, key):#OK
    u=0
    sht = ''
    for i in line:
        sht += alphabet[(alphabet.index(i) + alphabet.index(key[u%len(key)]))%32]
        u+=1
    return(sht)   

def decode(sht, key):#OK
    u=0
    line = ''
    for i in sht:
        line += alphabet[(alphabet.index(i) + 32 - alphabet.index(key[u%len(key)]))%32]
        u+=1
    return(line)  

def to_bloks(line, key):#OK
    d = []
    i = 0
    while i < key:# проходимся по всем блокам шифротекста Y0 Y1
        temp = ''
        j = 0
        while i + j*key < len(line):# создаём блоки шифротекста Y0= y0+y(r)+y(2r)
            temp += line[i + j*key]
            j += 1
        d.append(temp)
        i += 1
    return(d)

def find_key_length(line):#OK
    #пройдёмся по всем ключам
    max_key = 32
    i = 2
    while i < max_key:
        j=0
        index = []
        d = []
        d = to_bloks(line, i)
        while j < len(d):# пройдёмся по всем блокам зашифрованного текста
            index.append(ind_vid(d[j]))
            j += 1
        print(numpy.mean(index))
        i += 1

def find_key(line, key):#OK
    frags = to_bloks(line, key)
    slovnuk = ''
    slovnuk1 = ''
    for i in frags:
        tmp = collections.Counter(i).most_common(1)[0]
        slovnuk += alphabet[(alphabet.index(tmp[0]) - alphabet.index('о'))%32]
        slovnuk1 += alphabet[(alphabet.index(tmp[0]) - alphabet.index('е'))%32]
    print('', slovnuk,'\n',slovnuk1)
    
def task1():#OK
    keys = ['да','нет','рыба','кисть','яношуноски','желтыйайфон','поточныйшифр','доставкаглово','макароныссыром','зашифровываться','трехзначноечисло','приставкашифратор','оперироватьцифрами','монограммахудожника','автометасоматический']
    task_text = ''
    with open("2.txt", 'r', encoding="utf-8") as file:
        task_text = file.read()
    
    task_text = task_text.replace(' ', '').replace('ё', '').replace('.','').replace(',','').replace('-','').replace('\n','').lower()
    print(task_text)
    print(ind_vid(task_text))
    for i in keys:
        print(ind_vid(encode(task_text, i)))  

#find_key_length(text)
#find_key(text, 14)
#task1()
#знаходження частот для блоків, де найчастіша буква не "о"
d = to_bloks(encode(text,'экомаятникфуко'), 14)


temp = collections.Counter(d[2]).most_common(1)[0]
temp1 = collections.Counter(d[6]).most_common(1)[0]
temp2 = collections.Counter(d[13]).most_common(1)[0]
print(temp, temp1, temp2)

# In[ ]:





# In[ ]:





# In[ ]:





