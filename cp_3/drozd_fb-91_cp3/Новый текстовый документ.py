#!/usr/bin/env python
# coding: utf-8

# In[144]:


def euclid(a, b):
    if b == 0:  
        return a, 1, 0
    else:
        d, x, y = euclid(b, a % b)
        return d, y, x - y * (a // b)
    
def obr(a,mod):
    return euclid(a,mod)[1]%mod
ob(7,9)


# In[185]:


def gcd(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


# In[422]:


def rivn(a,b,mod):
    if (a == 0 and b == 0):
        return "infinity"
    if (a == 0 and b != 0):
        return "error"
    if (a != 0):
        d = gcd(a,mod)
        if d==1:
            return obr(a,mod)*b
        elif d>1:
            if b%d == 0:
                a1 = a/d
                b1 = a/d
                mod1 = mod/d
                rez = []
                for i in range(0,d):
                    rez.append((obr(a1,mod1)*b1+i*mod1)%mod)
                return rez
            else:
                return "error"
                        
                
    
rivn(5,5,15)    


# In[127]:


def bigram(text):
    bigram = []
    for j in range(0, len(text),2):
        bigram.append(text[j]+text[j+1])
    return bigram


# In[60]:


def freq(bigram):
    bigramtwo = []
    for j in range(0, len(text)-2,2):
        bigramtwo.append(text[j]+text[j+1])
    from collections import Counter

    bigramtwocount = dict(Counter(bigramtwo))
    freqbigramtwo = {k: bigramtwocount[k] / len(bigramtwo) for k in bigramtwocount}
    return freqbigramtwo 


# In[ ]:


text = open("/home/sofi/gdalenv/3.txt").read()
text = text.replace("\n","")
bigr = bigram(text)
freqbigram = freq(bigr)


# In[257]:


import pandas as pd
data = pd.DataFrame.from_dict(freqbigram,'index').stack().reset_index(level=0)  
print(data.columns)
data = data.sort_values(by=0, ascending=False)
data = data.rename(columns = {'level_0': 'bigram', 0: 'freq'})
data = data.reset_index(inplace=False).drop(columns= ['index'])
most = list(data['bigram'].head())
most


# In[325]:


alp = ['а', 'б', 'в', 'г', 'д', 'е', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ','ы', 'ь', 'э', 'ю', 'я']


# In[326]:


d = dict(zip(alp,list(r for r in range(0,len(alp)))))


# In[327]:


def value(bigram,mod,d):
    value = d[bigram[0]]*mod+d[bigram[1]]
    return value


# In[ ]:


values = []
for b in bigr:
    values.append(value(b,len(alp),d))
valuebigr = dict(zip(bigr,values))      
 


# In[447]:


def aval(X1,Y1,X2,Y2,mod):
    b = (Y1-Y2)%mod**2
    a = (X1-X2)%mod**2
    av = rivn(a,b,mod)
    if av!= 'error':
        return av%mod**2
    else:
        return None

def bval(y,x,a,mod):
    if a!= None:
        b = (y - a*x)%(mod**2)
        return b 
    else:
        return None


# In[252]:


def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
        
def decode(bigr,a,b,mod,d):
    x = []
    real = []
    for y in bigr:    
        x.append(((value(y,mod,d)-b)*obr(a,mod**2))%(mod**2))
    for i in range(0,len(x)):
        real.append(get_key(d,x[i]//mod))
        real.append(get_key(d,x[i]-(x[i]//mod)*mod))
    return real
        


# In[213]:


ukr = [ 'а', 'б', 'в', 'г', 'ґ', 'д', 'е', 'є', 'ж', 'з', 'и', 'і', 'ї', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ю', 'я']


# In[365]:


most


# In[347]:


mostrus =  ['ст', 'но', 'то', 'на', 'ен']


# In[449]:


a = []
b = []
for i in range(0,4):
    big_val_x1 = value(mostrus[i%4],len(alp),d)
    big_val_x2 = value(mostrus[(i+1)],len(alp),d)
    for j in range(0,4):
        big_val_y1 = value(most[j%4],len(alp),d)
        big_val_y2 = value(most[(j+1)%4],len(alp),d)
        a.append(aval(big_val_x1,big_val_y1,big_val_x2,big_val_y2,len(alp)))
        b.append(bval(big_val_y1,big_val_x1, a[len(a)-1],len(alp)))
        b.append(bval(big_val_y2,big_val_x2, a[len(a)-1],len(alp)))
        


# In[463]:


print(a,b)


# In[ ]:





# In[464]:


real = []
for i in range(0, len(a)):
    if a[i]!= None: 
        real.append(''.join(decode(bigr,a[i],b[2*i],len(alp),d)))
        real.append(''.join(decode(bigr,a[i],b[2*i+1],len(alp),d)))
real[1]


# In[353]:


a = []
b = []
for i in range(0,4):
    a.append(aval(value(most[i],len(alp),d),value(mostrus[i],len(alp),d),value(most[i+1],len(alp),d),value(mostrus[i+1],len(alp),d),len(alp)))
    b.append(bval(value(mostrus[i],len(alp),d),value(most[i],len(alp),d),a[i],len(alp)))
 


# In[465]:


for i in range(0, len(real)):
    print(real[i][:100])
    print('\n')


# In[425]:


y1 = value(most[2],len(alp),d)
y2 = value(most[3],len(alp),d)
x1 = value(mostrus[2],len(alp),d)
x2 = value(mostrus[3],len(alp),d)


# In[435]:


ab = []
i = 0
a = aval(x1,y1,x2,y2,len(alp))
b = bval(y2,x2,a,len(alp))


# In[440]:


real = ''.join(decode(bigram('до'),a,b,len(alp),d))


# In[441]:


real


# In[341]:


x1 = value(most[i],len(alp),d)
x2 = value(most[i+1],len(alp),d)


# In[342]:


y1 = value(mostrus[i],len(alp),d)
y2 = value(mostrus[i+1],len(alp),d)


# In[343]:


print(x1,y1,x2,y2)


# In[344]:


aval(x1,y1,x2,y2,len(alp))


# In[280]:


bva


# In[443]:


real = []
real.append(''.join(decode(bigr,a,b,len(alp),d)))
real


# In[338]:


a[3] 


# In[339]:


b[3]


# In[337]:


real[3]



