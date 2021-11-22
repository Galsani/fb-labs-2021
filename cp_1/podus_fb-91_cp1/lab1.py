import pandas
import numpy
import io
import re
import math
from pandas import ExcelWriter


alph_with_space = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                   'у','ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']


def char_frequency(str1):
    dict = {}
    for n in str1:
        if n in dict:
            dict[n] += 1
        else:
            dict[n] = 1
    res = sum(dict.values())
    for letter in dict:
        dict[letter] = float(dict[letter] / res)
    return dict


def bigram_frequency_step_two(str1):
    dict = {}
    count = 0
    bi_gram = ""
    i = 0
    while i < len(str1):
    #     if str1[i] == ' ' and count == 0:
    #         i += 1
    #         count = 2
    #     elif str1[i] == ' ' and count == 1:
    #         i += 1
    #         count = 2
    #     else:
        if count != 2:
            bi_gram += str1[i]
            count += 1
            i += 1
            if i == len(str1):
                if bi_gram in dict:
                    dict[bi_gram] += 1
                else:
                    dict[bi_gram] = 1
        if count == 2:
            count = 0
            if bi_gram != '':
                if bi_gram in dict:
                    dict[bi_gram] += 1
                else:
                    dict[bi_gram] = 1
            bi_gram = ""
    res = sum(dict.values())
    for bi_gram in dict:
        dict[bi_gram] = float(dict[bi_gram] / res)
    return dict


def bigram_frequency_step_one(str1):
    dict = {}
    count = 0
    bi_gram = ""
    i = 0
    while i < len(str1):
        # if str1[i] == ' ' and count == 0:
        #     i += 2
        #     count = 2
        # elif str1[i] == ' ' and count == 1:
        #     i += 2
        #     count = 2
        #     bi_gram = ""
        # else:
        if count != 2:
            bi_gram += str1[i]
            i += 1
            count += 1
        if count == 2:
            count = 0
            i -= 1
            if bi_gram != '':
                if bi_gram in dict:
                    dict[bi_gram] += 1
                else:
                    dict[bi_gram] = 1
            bi_gram = ""
    res = sum(dict.values())
    for bi_gram in dict:
        dict[bi_gram] = float(dict[bi_gram] / res)
    return dict


# def find_bigram_freq(text, intersect):
#     freq = {}
#     if intersect:
#         for i in range(0, len(text)):
#             if text[i:i+2] in freq:
#                 freq[text[i:i+2]] += 1
#             else:
#                 freq[text[i:i+2]] = 1
#         total = sum(freq.values())
#         for bigram in freq:
#             freq[bigram] = float(freq[bigram]/total)
#     else:
#         for i in range(0, len(text), 2):
#             if text[i:i+2] in freq:
#                 freq[text[i:i+2]] += 1
#             else:
#                 freq[text[i:i+2]] = 1
#         total = sum(freq.values())
#         for bigram in freq:
#             freq[bigram] = float(freq[bigram]/total)
#     return freq


def H(f):
    h = 0
    for let in f:
        h += f[let]*math.log(f[let], 2)
    return -h


def R(f):
    r = 1 - f/math.log(33, 2)
    return r


def sort_to_excel(text, file):
    df = pandas.DataFrame.from_dict(text, orient='index', columns=['amount'])
    df = df.sort_values(by='amount', ascending=0)
    writer = ExcelWriter(file, engine='xlsxwriter')
    df.to_excel(writer, "Sheet")
    writer.save()


def bigram_to_excel(dict, alphabet, file):
    df = pandas.DataFrame(index=alphabet, columns=alphabet)
    arr = []
    for i in alphabet:
        for j in alphabet:
            arr.append(i + j)
    f = 0
    for i in range(0, len(alphabet)):
        df[alphabet[i]] = arr[f:len(alphabet) + f]
        f = len(alphabet) + f
    df = df.T
    for i in list(dict):
        a, b = numpy.where(df == i)
        df.iloc[a, b] = dict[i]
    for i in arr:
        a, b  = numpy.where(df == i)
        df.iloc[a, b] = 0
    df.to_excel(file)


with io.open("text.txt", encoding='utf-8') as file:
    first_text = file.read()
    first_text = first_text.replace("\n", "")
    first_text = first_text.lower()

text = re.sub(r'[^\w\s]+|[\d]+', '', first_text)

data_char_with_space = char_frequency(text)
data_bigram_step_two_with_space = bigram_frequency_step_two(text)
data_bigram_step_one_with_space = bigram_frequency_step_one(text)
text = text.replace(" ", "")
data_char = char_frequency(text)
data_bigram_step_two = bigram_frequency_step_two(text)
data_bigram_step_one = bigram_frequency_step_one(text)



sort_to_excel(data_char_with_space, 'char_freq_with_space.xlsx')
bigram_to_excel(data_bigram_step_two_with_space, alph_with_space, 'bigram_step_two_with_space.xlsx')
bigram_to_excel(data_bigram_step_one_with_space, alph_with_space, 'bigram_step_one_with_space.xlsx')
sort_to_excel(data_char, 'char_freq.xlsx')
bigram_to_excel(data_bigram_step_two, alph, 'bigram_step_two.xlsx')
bigram_to_excel(data_bigram_step_one, alph, 'bigram_step_one.xlsx')


H_data_char_with_space = H(data_char_with_space)
H_data_bigram_step_two_with_space = 0.5 * H(data_bigram_step_two_with_space)
H_data_bigram_step_one_with_space = 0.5 * H(data_bigram_step_one_with_space)
H_data_char = H(data_char)
H_data_bigram_step_two = 0.5 * H(data_bigram_step_two)
H_data_bigram_step_one = 0.5 * H(data_bigram_step_one)


R_H_data_char_with_space = R(H_data_char_with_space)
R_data_bigram_step_two_with_space = R(H_data_bigram_step_two_with_space)
R_data_bigram_step_one_with_space = R(H_data_bigram_step_one_with_space)
R_data_char = R(H_data_char)
R_data_bigram_step_two = R(H_data_bigram_step_two)
R_data_bigram_step_one = R(H_data_bigram_step_one)


# print(H_data_char_with_space, R_H_data_char_with_space)
# print(H_data_bigram_step_two_with_space,R_data_bigram_step_two_with_space)
# print(H_data_bigram_step_one_with_space,R_data_bigram_step_one_with_space)
# print(H_data_char, R_data_char)
# print(H_data_bigram_step_two,R_data_bigram_step_two)
# print(H_data_bigram_step_one,R_data_bigram_step_one)



print(R(2.01))
print(R(2.75))
print(R(1.94))
print(R(2.76))
print(R(1.61))
print(R(2.37))


file.close()