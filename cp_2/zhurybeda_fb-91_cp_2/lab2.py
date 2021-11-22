import pandas as pd
import csv

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

key_list = ["мы", "вгм", "грвм", "после", "хнчрхический",
            "йфяцычувскмепи","фвпосэыарлжфывап","ывапролджйцугвыфья", "фывапролджйцукенгтчь"]

dict_alph = {}
for i in range(0, len(alph)):
    dict_alph[i] = alph[i]


def from_text_to_keys(text):
    text_list = []
    for letter in text:
        for let in dict_alph:
            if letter == dict_alph[let]:
                text_list.append(let)
    return text_list


def from_keys_to_text(keys_list):
    text = ""
    for i in keys_list:
        for let in dict_alph:
            if i == let:
                text += dict_alph[let]
    return text


def encode(text, key):
    text_keys_list = from_text_to_keys(text)
    keys_pos = from_text_to_keys(key)
    j = 0
    for i in range(len(text_keys_list)):
        text_keys_list[i] = (text_keys_list[i] + keys_pos[j]) % len(alph)
        j += 1
        if j == len(key):
            j = 0
    return from_keys_to_text(text_keys_list)


def decode(text, key):
    text_keys_list = from_text_to_keys(text)
    keys_pos = from_text_to_keys(key)
    j = 0
    for i in range(len(text_keys_list)):
        text_keys_list[i] = (text_keys_list[i] - keys_pos[j]) % len(alph)
        j += 1
        if j == len(key):
            j = 0
    return from_keys_to_text(text_keys_list)


df = pd.read_excel("character_frequency.xlsx", index_col=0)
df = df.where(pd.notnull(df), None)
freq_dict = df.to_dict()["freq"]


def calc_index(text):
    index = 0
    coef = 1 / ((len(text)) * (len(text) - 1))
    for letter in alph:
        letter_count = text.count(letter)
        index += letter_count * (letter_count - 1)
    return index * coef


def create_blocks(text, size):
    blocks = []

    for start in range(0, size):
        blocks.append(text[start::size])

    return blocks


def max_freq(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    res = max(freq, key=freq.get)
    return res


def find_key_len(text):
    indexes = {}
    for len_key in range(1, 31):
        coincidence_idx = 0

        blocks = create_blocks(text, len_key)

        for block in blocks:
            coincidence_idx += calc_index(block)
        coincidence_idx /= len_key
        indexes[len_key] = coincidence_idx

    return indexes


def find_key(text, r):
    keys = []
    blocks = create_blocks(text, r)
    letter = "о"
    for block in blocks:
        max = max_freq(block)
        key = (alph.index(max) - alph.index(letter)) % len(alph)
        keys.append(alph[key])
    key = ''.join(keys)
    return key

#task 1
file = open("clean_text.txt", 'r')
TEXT = file.read()
file.close()

indexes = {}
for key in key_list:
    encoded_text = encode(TEXT, key)
    I = calc_index (encoded_text)
    indexes[len(key)] = I

with open('task1.csv', 'w') as f:
    for key in indexes.keys():
        f.write("%s,%s\n"%(key,indexes[key]))

# task 3
CODED = open("coded_text.txt", 'r', encoding="utf-8").read()
key_len_data = find_key_len(CODED)
with open('task3.csv', 'w') as f:
    for key in key_len_data.keys():
        f.write("%s,%s\n"%(key,key_len_data[key]))
print(key_len_data)
key_len = max(key_len_data, key=key_len_data.get)
print(key_len)
key = find_key(CODED, key_len)
print(key)
print(decode(CODED, 'арудазовархимаг'))

decded = open("decoded.txt", "w")
decded.write(decode(CODED, 'арудазовархимаг'))
decded.close()
