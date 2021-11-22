rus_alph = 'абвгдежзийклмнопрстуфхцчшщьыэюя'
most_popular_bigrams = ["ст", "но", "то", "на", "ен"]
most_popular_letters = ["о", "е", "а"]


def alphabet_dict_1(alphabet):
    alph_dict = {}
    i = 0
    while (i < len(alphabet)):
        alph_dict[alphabet[i]] = i
        i = i+1
    return alph_dict


def alphabet_dict_2(alphabet):
    alph_dict = {}
    i = 0
    while (i < len(alphabet)):
        alph_dict[i] = alphabet[i]
        i = i+1
    return alph_dict


def gcd_recursion(n1, n2):
    if n1 == 0:
        return n2
    return gcd_recursion(n2 % n1, n1)


def extended_alg_euclid(n1, n2):
    if n1 == 0:
        return n2, 0, 1
    else:
        our_gcd, a, b = extended_alg_euclid(n2 % n1, n1)
    return our_gcd, b - (n2 // n1) * a, a


def reverse_element(n1, n2):
    if gcd_recursion(n1, n2) != 1:
        return False
    else:
        u = extended_alg_euclid(n1, n2)[1]
        return u % n2


def modular_equation(n1, n2, mod):
    gcd = gcd_recursion(n1, mod)
    if gcd == 1:
        a = (reverse_element(n1, mod) * n2) % mod
        return a
    else:
        if n2 % gcd != 0:
            return False
        else:
            res = []
            a = modular_equation(int(n1 / gcd), int(n2 / gcd), int(mod / gcd))
            res.append(a)
            for i in range(1, gcd):
                res.append(a + int(mod / gcd) * i)
        return res


def text_correction(file_name):
    with open(file_name, encoding="utf8") as file:
        text = file.read()
        text = text.replace("\n", "")
        file.close()
    return text


def make_bigrams_list(text):
    bigram_list = []
    i = 0
    while i < len(text):
        bigram = text[i] + text[i + 1]
        bigram_list.append(bigram)
        i = i + 2
    return bigram_list


def char_frequency(text, alph):
    dict = {}
    letter_frequency = {}
    for letter in alph:
        dict[letter] = 0
    for letter in text:
        dict[letter] = dict[letter] + 1
    for letter in alph:
        letter_frequency[letter] = (dict[letter]) / len(text)
    return letter_frequency


def bigram_frequency(text, alph):
    dict_bigram_count = {}
    dict_bigram_frequency = {}
    for let1 in alph:
        for let2 in alph:
            dict_key = let1 + let2
            dict_bigram_count[dict_key] = 0
    i = 0
    while i < len(text) - 1:
        key = text[i] + text[i + 1]
        dict_bigram_count[key] = dict_bigram_count[key] + 1
        i = i + 1
    for key in dict_bigram_count.keys():
        dict_bigram_frequency[key] = dict_bigram_count[key] / (len(text))
    return dict_bigram_frequency


def five_popular(frequency):
    sorted_values = sorted(frequency.values(), reverse=True)
    sorted_dict = {}
    for i in sorted_values:
        for j in frequency.keys():
            if frequency[j] == i:
                sorted_dict[j] = frequency[j]
    sorted_bigram_list = list(sorted_dict)
    i = 0
    five_popular_in_text = []
    while i < 5:
        five_popular_in_text.append(sorted_bigram_list[i])
        i = i+1
    return five_popular_in_text


def all_pairs(list):
    pairs = []
    for i in list:
        for j in list:
            if i != j:
                pairs.append([i, j])
    print("All pairs: ")
    print(pairs)
    return pairs


def pairs_bigrams_in_numbers(lst, alph):
    list_pairs_bigrams_in_numbers = []
    for pair in lst:
        n1 = alph[pair[0][0]] * len(rus_alph) + alph[pair[0][1]]
        n2 = alph[pair[1][0]] * len(rus_alph) + alph[pair[1][1]]
        list_pairs_bigrams_in_numbers.append((n1, n2))
    return list_pairs_bigrams_in_numbers


def bigram_in_numbers(lst, alph):
    list_bigram_in_numbers = []
    for i in lst:
        n = alph[i[0]] * len(rus_alph) + alph[i[1]]
        list_bigram_in_numbers.append(n)
    return list_bigram_in_numbers


def search_all_pottential_keys(pair_1, pair_2):
    sub_x = int(pair_1[0]) - int(pair_1[1])
    sub_y = int(pair_2[0]) - int(pair_2[1])
    res1 = modular_equation(sub_x, sub_y, len(rus_alph) ** 2)
    if not res1:
        return 0
    elif type(res1) == int :
        res2 = (int(pair_2[0]) - res1 * int(pair_1[0])) % len(rus_alph) ** 2
        return res1, res2
    else:
        res2 = (int(pair_2[0]) - res1[0] * int(pair_1[0])) % len(rus_alph) ** 2
        return res1[0], res2


def decrypt_text(text, keys):
    dict_decrypt_text = {}
    decrypt_str = ""
    for i in keys:
        if i != 0:
            for j in range(0, len(text) // 2):
                if str(reverse_element(i[0], len(rus_alph) ** 2)):
                    x = int(reverse_element(i[0], len(rus_alph) ** 2)) * (text[j] - i[1]) % len(rus_alph) ** 2
                    x1 = x // len(rus_alph)
                    x2 = x % len(rus_alph)
                    decrypt_str += alph_number_2[x1] + alph_number_2[x2]
                    j += 1
            dict_decrypt_text[i] = decrypt_str
            decrypt_str = ""
    return dict_decrypt_text


def search_right_key(dict_decrypt_text):
    potential_keys_by_letter = {}
    potential_keys_by_bigram = {}
    for key in dict_decrypt_text.keys():
        if dict_decrypt_text[key] != '':
            char_freq = char_frequency(dict_decrypt_text[key], rus_alph)
            popular_5_char = five_popular(char_freq)
            if popular_5_char[0] in most_popular_letters and popular_5_char[1] in most_popular_letters and popular_5_char[2] in most_popular_letters:
                potential_keys_by_letter[key] = popular_5_char
    for key in potential_keys_by_letter:
        bigram_freq = bigram_frequency(dict_decrypt_text[(key)], rus_alph)
        popular_5_bigram = five_popular(bigram_freq)
        if popular_5_bigram[0] in most_popular_bigrams and popular_5_bigram[1] in most_popular_bigrams and popular_5_bigram[2] in most_popular_bigrams:
            potential_keys_by_bigram[key] = popular_5_bigram
    return list(potential_keys_by_bigram.keys())[0]


def write_to_file_clear_text(text, key):
    clear_text = ""
    for j in range(0, len(text)):
        n = int(reverse_element(key[0], len(rus_alph) ** 2)) * (text[j] - key[1]) % len(rus_alph) ** 2
        n1 = n // len(rus_alph)
        n2 = n % len(rus_alph)
        clear_text += alph_number_2[n1] + alph_number_2[n2]
        j += 1
    print("Decrypted text:")
    print(clear_text)
    file_to_write = open('clear_text.txt', 'w')
    file_to_write.write(clear_text)
    file_to_write.close()


shifr_text = text_correction("16.txt")
dict_bigram_frequency = bigram_frequency(shifr_text, rus_alph)
popular_5 = five_popular(dict_bigram_frequency)
print("5 Most popular bigrams in text " + str(popular_5))
all_popular_5_pairs = all_pairs(most_popular_bigrams)
all_popular_5_pairs_in_text = all_pairs(popular_5)
alph_number_1 = alphabet_dict_1(rus_alph)
all_popular_5_pairs_in_num = pairs_bigrams_in_numbers(all_popular_5_pairs, alph_number_1)
all_popular_5_pairs_in_text_in_num = pairs_bigrams_in_numbers(all_popular_5_pairs_in_text, alph_number_1)
potentional_keys = []
for i in all_popular_5_pairs_in_num:
    for j in all_popular_5_pairs_in_text_in_num:
        potentional_key = search_all_pottential_keys(i, j)
        potentional_keys.append(potentional_key)
print("All potential keys in text: ")
print(potentional_keys)
list_text_bigrams = make_bigrams_list(shifr_text)
bigrams_in_numbers = bigram_in_numbers(list_text_bigrams, alph_number_1)
alph_number_2 = alphabet_dict_2(rus_alph)
dec_text = decrypt_text(bigrams_in_numbers, potentional_keys)
key = search_right_key(dec_text)
print(f"Our key is " + str(key))
write_to_file_clear_text(bigrams_in_numbers, key)