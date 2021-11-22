#!/usr/bin/env python
# coding: utf-8

# In[950]:


#text prepare

import regex 
import collections
import unicodedata
text = open("/home/sofi/1.txt").read()
text = text.lower()
text = text.replace("n","")
text = text.replace("ё","е")
text = text.replace("\n"," ")
text = ' '.join(text.split())

import re
#without space
newstring = ''.join(c for c in text if unicodedata.category(c).startswith('L'))

#with space
#newstring = regex.sub(r'[^\w\s]+|[\d]+', r'',text).strip()


print(newstring)
newstring = newstring[:2000]
print("OK")


# In[951]:


#Count
alp = []    
for i in range(0,len(newstring )):
    alp.append(newstring [i])
alpcount = dict(collections.Counter(alp))
print(alpcount)
print("\n")
freq = {k: alpcount[k] / len(word) for k in alpcount}
print(freq)


# In[952]:


alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']


# In[953]:



d = []
for id, item in enumerate(alp):
    d.append(id)

dd = dict(zip(alp,d))    
def encode(text,key,dd, alp):
    help = []
    for i in range(0, len(text)):
        help.append((dd[text[i]]+dd[key[i%len(key)]])%len(alp))
    code = alp[help[0]]
    for i in range(1, len(text)):
        code = code+alp[help[i]]
    return code
    


# In[932]:


def decode(code,key,dd, alp):
    help = []
    for i in range(0, len(code)):
        help.append((dd[code[i]]-dd[key[i%len(key)]])%len(alp))
        
    decod = alp[help[0]]
    for i in range(1, len(code)):
        decod = decod+alp[help[i]]
    return decod


# In[954]:


def gram(text, number):
    gr = []
    for i in range(0,len(text),number):
        gr.append(text[i:i+number])
    return gr

def countt(gram):
    alpcount = dict(collections.Counter(gram))
    return alpcount
   

def I(alpcount):
    i = []
    for key in list(alpcount.keys()):
        i.append(alpcount[key]*(alpcount[key]-1))
    IY = 1/(sum(alpcount.values())*(sum(alpcount.values())-1))*sum(i)
    return IY



# In[955]:


keys = ["а","сы","яма","весы","жарко","утопаютвпо","бесполезной","случайнониче","полезныештуки","пореверсунесох","мненадосделатьд","логикаразмещения","правдадумаешьчтоя","спроситькоечтооби","чтотоещепомнюспустя","автоматическивначале"]


# In[956]:




codes = []

for key in keys:
    codes.append(encode(newstring,key,dd,alp))
print(len(codes))    



r = []  
rlen = []
for i in range(0, len(codes)):
    rlen.append(len(keys[i]))
    alpcount = countt(gram(codes[i],1))
    r.append(I(alpcount))
print(r) 


# In[235]:


decodes = []
for i in range(0, len(codes)):
    decodes.append(decode(codes[i],keys[i],dd,alp))
print(len(decodes))


# In[957]:


import pandas as pd
df = pd.DataFrame()
df['r'] = rlen
df['I'] = r
df.to_excel("df.xlsx")


# In[958]:


import matplotlib as mpl
import matplotlib.pyplot as plt
plt.bar(df['r'],df['I'])
plt.show()


# In[959]:






def block(text, r):
    blocks = []
    for j in range(0, r):
        bl = ""
        for i in range(0, len(text)-j,r):
                bl = bl+text[i+j]
        if bl!="":       
            blocks.append(bl)
        else:
            continue
    return blocks    
    

blocks = []
for r in range(2,31):
    blocks.append(block(codes[3],r))
 
IY = []
for i in range(0, len(blocks)): 
    j = []
    for k in range(0, len(blocks[i])):
        
        alpcount = countt(blocks[i][k])
        j.append(I(alpcount))
    IY.append(sum(j)/len(j))  
        
II = dict(zip([r for r in range(2,31)],IY))    
print(II)


# In[948]:


cript = open("/home/sofi/gdalenv/lab2.txt").read()
cript = cript.replace('\n',"")


# In[949]:



blocks = []
for r in range(2,31):
    blocks.append(block(cript,r))
IY = []
for i in range(0, len(blocks)): 
    j = []
    for k in range(0, len(blocks[i])):
        alpcount = countt(blocks[i][k])
        j.append(I(alpcount))
        #print(j)       
    IY.append(sum(j)/len(j))         
II = dict(zip([r for r in range(2,31)],IY))    
print(II)         


# In[947]:


import pandas as pd
df = pd.DataFrame()
df['r'] = [r for r in range(2,31)]
df['I'] = IY
df.to_excel("df1.xlsx")


# In[817]:


IY = []
for i in range(0, len(blocks)): 
    j = []
    for k in range(0, len(blocks[i])):
        alpcount = countt(blocks[i][k])
        j.append(I(alpcount))
        #print(j)       
    IY.append(sum(j)/len(j))         
II = dict(zip([r for r in range(2,31)],IY))    
print(II)  


# In[943]:


def bl(r):
    blocks = block(cript,r)
    alpcount = [] 
    for i in range(0,len(blocks)):
        alpcount.append(countt(blocks[i]))
 

    freq = []
    for i in range(0,len(blocks)):
        temp = []
        temp = {k: alpcount[i][k] / len(blocks[i]) for k in alpcount[i]} 
        freq.append(temp)  
    top = []
    for i in range(0,len(freq)):
        temp = []
        temp = sorted(freq[i], key=lambda x : alpcount[i][x],reverse=1) 
        top.append(temp[0])

    help = ['о','а','е','и','н','т','л','с','р','в','к','у','м','п','д','г','я','з','ь','ы','ч','б','й','ж','ш','х','ю','щ','ц','э','ф','ъ']

    keys = []
    for j in range (0, len(help)):
        key = ""
        for i in range(0,len(top)):
            key = key+alp[(dd[top[i]] - dd[help[j]])%(len(alp))]
        keys.append(key) 
    print(keys)  

bl(13)


# In[926]:


cc = decode(cript,"громыковедьма",dd,alp)

        
cc  


# In[925]:


k = ""
kk = "громнкавьдумагромнкавьдумагромнкавьдумагромнкавьдумагромнкавьдума"
a = cript[46:59]
b = "теоретический"
for i in range(0,len(a)):
    k = k+alp[((dd[a[i]] - dd[b[i]])%(len(alp)))]
print(k)    
print(kk[46:59] )  

