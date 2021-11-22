from Format_Text import text_format
import math
import pandas as pd
import numpy as np

alphabet_str_gap = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя '
alphabet_str = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


def read_from_file(file_name):
    with open(file_name) as file:
        text_str = file.read()
        file.close()
    return text_str

def write_to_file(my_str, Value):
    file_to_write = open('data_file.txt', 'a')
    file_to_write.write(my_str)
    file_to_write.write(str(Value))
    file_to_write.close()

def letter_frequency(str, alphabet):
    pair_letter_count = {}
    for letter in alphabet:
        pair_letter_count[letter] = 0
    for letter in str:
        pair_letter_count[letter] =  pair_letter_count[letter] + 1

    pair_letter_frequency = {}
    for letter in alphabet:
        pair_letter_frequency[letter] = round((pair_letter_count[letter])/len(str), 5)

    print(pair_letter_frequency)
    return pair_letter_frequency

def bigram_frequency(str, alphabet, cross = True):
    pair_bigram_count = {}
    pair_bigram_frequency = {}
    for letter1 in alphabet:
        for letter2 in alphabet:
            dict_key = letter1 + letter2
            pair_bigram_count[dict_key] = 0

    if (cross == True): #H1
        i = 0
        while i < len(str) - 1:
            key = str[i] + str[i+1]
            pair_bigram_count[key] = pair_bigram_count[key] + 1
            i = i + 1

        for key in pair_bigram_count.keys():
            pair_bigram_frequency[key] = round(pair_bigram_count[key]/(len(str)-1), 5)

    else: #H2
        if len(str) % 2 == 1:
            str += "ъ"
        i = 0
        while i < len(str) - 1:
            key = str[i] + str[i+1]
            pair_bigram_count[key] = pair_bigram_count[key] + 1
            i = i + 2

        for key in pair_bigram_count.keys():
            pair_bigram_frequency[key] = round(pair_bigram_count[key]/(len(str)/2), 5)

    print(pair_bigram_frequency)
    return pair_bigram_frequency

def entropy(Dict, n):
    entropy_list = []
    for key in Dict.keys():
        if Dict[key] != 0:
            entropy_list.append(float(Dict[key]) * math.log2(Dict[key])/n)
    entr = - sum(entropy_list)
    print(entr)
    return entr

def RU_redundancy(entropy, alphabet):
    return 1 - (entropy/math.log2(len(alphabet)))

def main_function():
    text_format('text.txt', True)
    my_text = read_from_file('format_text.txt')

    MF = letter_frequency(my_text, alphabet_str_gap)
    write_to_file('Частота букв в тексті з пробілами: \n', MF)
    entropy_MF = entropy(MF, 1)
    write_to_file('\n\nЕнтропія\n', entropy_MF)
    write_to_file('\n\nНадлишковість: \n', RU_redundancy(entropy_MF, alphabet_str_gap))

    BF1 = bigram_frequency(my_text, alphabet_str_gap, True)
    write_to_file('\n\nЧастота біграм H1 в тексті з пробілами: \n', BF1)
    entropy_BF1 = entropy(BF1, 2)
    write_to_file('\n\nЕнтропія\n', entropy_BF1)
    write_to_file('\n\nНадлишковість: \n', RU_redundancy(entropy_BF1, alphabet_str_gap))

    BF2 = bigram_frequency(my_text, alphabet_str_gap, False)
    write_to_file('\n\nЧастота біграм H2 в тексті з пробілами: ', BF2)
    entropy_BF2 = entropy(BF2, 2)
    write_to_file('\n\nЕнтропія\n', entropy_BF2)
    write_to_file('\n\nНадлишковість: \n', RU_redundancy( entropy_BF2, alphabet_str_gap))

    text_format('text.txt', False)
    my_text_without_gaps = read_from_file('format_text.txt')

    MF_without_gaps = letter_frequency(my_text_without_gaps, alphabet_str)
    write_to_file('\n\nЧастота букв в тексті без пробілів: \n', MF_without_gaps)
    entropy_MF_without_gaps = entropy(MF_without_gaps, 1)
    write_to_file('\n\nЕнтропія\n', entropy_MF_without_gaps)
    write_to_file('\n\nНадлишковість: \n', RU_redundancy(entropy_MF_without_gaps, alphabet_str_gap))

    BF1_without_gaps = bigram_frequency(my_text_without_gaps, alphabet_str, True)
    write_to_file('\n\nЧастота біграм H1 в тексті без пробілів: \n', BF1_without_gaps)
    entropy_BF1_without_gaps = entropy(BF1_without_gaps, 2)
    write_to_file('\n\nЕнтропія\n', entropy_BF1_without_gaps)
    write_to_file('\n\nНадлишковість: \n',     RU_redundancy(entropy_BF1_without_gaps, alphabet_str_gap))

    BF2_without_gaps = bigram_frequency(my_text_without_gaps, alphabet_str, False)
    write_to_file('\n\nЧастота біграм H2 в тексті без пробілів: \n', BF2_without_gaps)
    entropy_BF2_without_gaps = entropy(BF2_without_gaps, 2)
    write_to_file('\n\nЕнтропія\n', entropy_BF2_without_gaps)
    write_to_file('\n\nНадлишковість: \n', RU_redundancy(entropy_BF2_without_gaps, alphabet_str_gap))
    
    data = pd.DataFrame.from_dict(MF,'index').stack().reset_index(level=0)
    data = data.sort_values(by=0, ascending=False)
    data = data.rename(columns = {'level_0': 'letter', 0: 'frequency'})

    data.to_excel('C:/Users/Lenovo/Desktop/letter_fr.xlsx')
    
    
    data = pd.DataFrame.from_dict(MF_without_gaps,'index').stack().reset_index(level=0)
    data = data.sort_values(by=0, ascending=False)
    data = data.rename(columns = {'level_0': 'letter', 0: 'frequency'})

    data.to_excel('C:/Users/Lenovo/Desktop/letter_fr_nogaps.xlsx')
    
    #----------------
    alphabet_sp = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я', ' ']
    alphabet_nosp = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']
    df = pd.DataFrame(index = alphabet_sp, columns=alphabet_sp)
    
    bg = []
    
    for i in alphabet_sp:
        for j in alphabet_sp:
            bg.append(i+j)
     
    n = 0
    for i in range(0,len(alphabet_sp)):
        df[alphabet_sp[i]] = bg[n:len(alphabet_sp)+n]
        n = len(alphabet_sp)+n
    df = df.T
    

    
    for b in list(BF1.keys()):
        a,c = np.where(df == b)
        df.iloc[a,c] = BF1[b]
        
    for b in bg:
        a,c = np.where(df == b)
        df.iloc[a,c] = 0
        
    print(df.head())
    df.to_excel('C:/Users/Lenovo/Desktop/bigr_h1.xlsx') 
        
     
    df = pd.DataFrame(index = alphabet_sp, columns=alphabet_sp)

    bg = []
    
    for i in alphabet_sp:
        for j in alphabet_sp:
            bg.append(i+j)
     
    n = 0
    for i in range(0,len(alphabet_sp)):
        df[alphabet_sp[i]] = bg[n:len(alphabet_sp)+n]
        n = len(alphabet_sp)+n
    df = df.T
    
    for b in list(BF2.keys()):
        a,c = np.where(df == b)
        df.iloc[a,c] = BF2[b]
        
    for b in bg:
        a,c = np.where(df == b)
        df.iloc[a,c] = 0
        
    print(df.head())
    df.to_excel('C:/Users/Lenovo/Desktop/bigr_h2.xlsx')
    
    
    df = pd.DataFrame(index = alphabet_nosp, columns=alphabet_nosp)

    bg = []
    
    for i in alphabet_nosp:
        for j in alphabet_nosp:
            bg.append(i+j)
     
    n = 0
    for i in range(0,len(alphabet_nosp)):
        df[alphabet_nosp[i]] = bg[n:len(alphabet_nosp)+n]
        n = len(alphabet_nosp)+n
    df = df.T
    
    for b in list(BF1_without_gaps.keys()):
        a,c = np.where(df == b)
        df.iloc[a,c] = BF1_without_gaps[b]
        
    for b in bg:
        a,c = np.where(df == b)
        df.iloc[a,c] = 0
        
    print(df.head())
    df.to_excel('C:/Users/Lenovo/Desktop/bigr_h1_nogaps.xlsx')
    df = pd.DataFrame(index = alphabet_nosp, columns=alphabet_nosp)

    bg = []
    
    for i in alphabet_nosp:
        for j in alphabet_nosp:
            bg.append(i+j)
     
    n = 0
    for i in range(0,len(alphabet_nosp)):
        df[alphabet_nosp[i]] = bg[n:len(alphabet_nosp)+n]
        n = len(alphabet_nosp)+n
    df = df.T
    
    for b in list(BF2_without_gaps.keys()):
        a,c = np.where(df == b)
        df.iloc[a,c] = BF2_without_gaps[b]
        
    for b in bg:
        a,c = np.where(df == b)
        df.iloc[a,c] = 0
        
    print(df.head())
    df.to_excel('C:/Users/Lenovo/Desktop/bigr_h2_nogaps.xlsx')
    

main_function()


