from lab_math import *

file = open("07.txt", 'rt')
TEXT = file.read()
file.close()


def find_bigram_freq(text):
    freq = {}
    for i in range(0, len(text), 2):
        if text[i:i + 2] in freq:
            freq[text[i:i + 2]] += 1
        else:
            freq[text[i:i + 2]] = 1
    total = sum(freq.values())
    for bigram in freq:
        freq[bigram] = float(freq[bigram] / total)
    return freq


freq = find_bigram_freq(TEXT)
sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
top_cypher_bi = list(sorted_freq)[:5]
print(top_cypher_bi)
top_bi = ["ст", "но", "то", "на", "ен"]

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ь', 'ы', 'э', 'ю', 'я']
m = len(alph)


def bi_to_number(bigram):
    return (alph.index(bigram[0]) * m + alph.index(bigram[1])) % m ** 2


# print(bi_to_number('вб'))
def decrypt(text, keys):
    a = int(keys[0])
    b = int(keys[1])
    decrypt_text = []
    for i in range(0, len(text), 2):
        x = (re(a, m ** 2) * (bi_to_number(text[i:i + 2]) - b)) % (m ** 2)
        decrypt_text.append(alph[x // m] + alph[x % m])
    return ''.join(i for i in decrypt_text)


def pair(text):
    couple = []
    pairs = []
    for i in top_bi:
        for j in top_cypher_bi:
            couple.append((i, j))
    for i in couple:
        for j in couple:
            if i != j or (j, i) not in pairs:
                pairs.append((i, j))
    return pairs


def find_key(pair):
    x1 = bi_to_number(pair[0][0])
    x2 = bi_to_number(pair[0][1])
    y1 = bi_to_number(pair[1][0])
    y2 = bi_to_number(pair[1][1])
    keys = []
    a = linear_comp(x1 - x2, y1 - y2, m ** 2)
    if a:
        for i in a:
            b = (gcd(y1 - i * x1, m ** 2)[1]) % m ** 2
            keys.append((i, b))
    return keys


def all_keys(pairs):
    keys = []
    for pair in pairs:
        key = find_key(pair)
        if len(key) != 0:
            for i in range(len(key)):
                keys.append(key[i])
    return keys


pairs = pair(TEXT)

keys = all_keys(pairs)

texts = []

for key in keys:
    texts.append(decrypt(TEXT, key))

def check(texts):
    clean_text = []
    for text in texts:
        if not any(text.find("аь"), text.find("оо"), text.find("оь")):
            clean_text.append(text)
    return clean_text
