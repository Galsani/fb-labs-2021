import io
import pandas


alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
        'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
keys = ["ты", "кто", "рыба", "рыбак", "асортимент", "лесоводство", "единоборство", " автотранспорт",
        "накопительство", "малочисленность", "парадоксальность", "хлебозаготовитель", "невразумительность",
        "дираопромышленность", "воздухопроницаемость"]

dict_alph = {}
for i in range(0, len(alph)):
    dict_alph[i] = alph[i]

with io.open("text.txt") as file:
    text = file.read()
    text = text.replace(' ', '')


def encode_text_by_alph(txt):
    text_list = []
    for letter in txt:
        for let in dict_alph:
            if letter == dict_alph[let]:
                text_list.append(let)
    return text_list


def decode_text_by_alph(text_list):
    txt = ""
    for i in text_list:
        for let in dict_alph:
            if i == let:
                txt += dict_alph[let]
    return txt


def compare_text_key(txt, key):
    dict = {}
    j = 0
    count = 0
    for i in txt:
        dict[count] = [i, key[j]]
        count += 1
        j += 1
        if j >= len(key):
            j = 0
    return dict


def full_encode(txt, key):
    enc_text_by_alph = encode_text_by_alph(txt)
    enc_key_alph = encode_text_by_alph(key)
    dict = compare_text_key(enc_text_by_alph, enc_key_alph)
    enc_txt_list = []
    for i in dict:
        new_letter = (dict[i][0] + dict[i][1]) % len(dict_alph)
        enc_txt_list.append(new_letter)
    enc_txt = decode_text_by_alph(enc_txt_list)
    return enc_txt


def full_decode(enc_txt, key):
    enc_text_by_alph = encode_text_by_alph(enc_txt)
    enc_key_by_alph = encode_text_by_alph(key)
    dict = compare_text_key(enc_text_by_alph, enc_key_by_alph)
    dec_txt_list = []
    for i in dict:
        go = (dict[i][0] - dict[i][1] + len(dict_alph)) % len(dict_alph)
        dec_txt_list.append(go)
    dec_txt = decode_text_by_alph(dec_txt_list)
    return dec_txt


def I(enc_txt):
    dict_freq = {}
    for let in enc_txt:
        if let in dict_freq:
            dict_freq[let] += 1
        else:
            dict_freq[let] = 1
    kof = 1 / ((len(enc_txt)) * (len(enc_txt) - 1))
    I = 0
    for key in dict_freq:
        I += kof * (dict_freq[key] * (dict_freq[key] - 1))
    return I


def finding_key_for_var_16():
    dict_enc = {}
    for i in range(2, 22):
        count_table = 0
        j = 0
        dict_table = {}
        while j < len(shifr_text):
            piece_text = shifr_text[j:j+i]
            if len(piece_text) == i:
                for table in range(0, i):
                    if count_table < i:
                        dict_table[table] = {}
                    if piece_text[table] in dict_table[table]:
                        dict_table[table][piece_text[table]] += 1
                    else:
                        dict_table[table][piece_text[table]] = 1
                    count_table += 1
            j += i
        I = 0
        for table in range(0, i):
            I = 0
            len_column = 0
            for key in dict_table[table]:
                len_column += dict_table[table][key]
            kof = 1 / (len_column * (len_column - 1))
            for key in dict_table[table]:
                I += kof * (dict_table[table][key] * (dict_table[table][key] - 1))
        dict_enc[i] = I
        print("r: " + str(i) + " " + str(I))
    df_enc = pandas.DataFrame.from_dict(dict_enc, orient="index")
    with pandas.ExcelWriter('I_enc.xlsx') as writer_enc:
        df_enc.to_excel(writer_enc)
    all_key = ""
    for table in range(0, 21):
        list_arr = []
        i = 0
        new_str = ""
        while i+table < len(shifr_text):
            list_arr.append(shifr_text[i+table])
            i = i + 21
        for let in list_arr:
            new_str += let
        counted_chars = {}
        for char in new_str:
            if char in counted_chars:
                counted_chars[char] += 1
            else:
                counted_chars[char] = 1
        sorted_values = sorted(counted_chars.values())
        sorted_dict = {}
        for i in sorted_values:
            for k in counted_chars.keys():
                if counted_chars[k] == i:
                    sorted_dict[k] = counted_chars[k]
                    break
        key = (alph.index(max(sorted_dict, key = sorted_dict.get)) - alph.index('о')) % len(alph)
        all_key += alph[key]
        new_text = []
        for letter in new_str:
            new_letter = alph.index(letter) - key
            new_text.append(alph[new_letter % len(alph)])
        text_str = ""
        for l in new_text:
            text_str += l
    return all_key


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


dict_I = {}
for key in keys:
    print("Ключ: " + key)
    print("Початковий текст: " + text)
    encode_text = full_encode(text, key)
    print("Закодованый текст: " + encode_text)
    print(I(encode_text))
    dict_I[key] = [len(key), I(encode_text)]
    decode_text = full_decode(encode_text, key)
    print("Розкодований текст: " + decode_text)
df_I = pandas.DataFrame.from_dict(dict_I, orient="index")
with pandas.ExcelWriter('I.xlsx') as writer:
    df_I.to_excel(writer)
with io.open("shifr_text.txt", encoding='utf-8') as shifr_file:
    shifr_text = shifr_file.read()
    shifr_text = shifr_text.replace("\n", "")
print("Розмір ключа 21")
print("Можливий Ключ: "  + str(finding_key_for_var_16()))
print("Ключ після аналізу текста: башняяростичерныемаки")
dec_text = full_decode(shifr_text, "башняяростичерныемаки")
print("Розкодований текст: " + dec_text)
dict_enc_text = char_frequency(dec_text)
df = pandas.DataFrame.from_dict(dict_enc_text, orient='index', columns=['freq'])
df = df.sort_values(by='freq', ascending=0)
df = df.to_string()
with open("freq.txt", "w") as freq_text:
    freq_text.write(df)
freq_text.close()
shifr_file.close()
file.close()



