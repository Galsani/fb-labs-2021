import math
def find_freq(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    total = sum(freq.values())
    for letter in freq:
        freq[letter] = float(freq[letter]/total)
    return freq


# print(find_freq("авпвапвапыфилшжщж"))


def find_bigram_freq(text, intersect):
    freq = {}
    if intersect:
        for i in range(0, len(text)):
            if text[i:i+2] in freq:
                freq[text[i:i+2]] += 1
            else:
                freq[text[i:i+2]] = 1
        total = sum(freq.values())
        for bigram in freq:
            freq[bigram] = float(freq[bigram]/total)
    else:
        for i in range(0, len(text), 2):
            if text[i:i+2] in freq:
                freq[text[i:i+2]] += 1
            else:
                freq[text[i:i+2]] = 1
        total = sum(freq.values())
        for bigram in freq:
            freq[bigram] = float(freq[bigram]/total)
    return freq


# print(find_bigram_freq("mo momemtmdghhр", True))
# print(find_bigram_freq("mo momemtmdghhр", False))


def find_entropy(text, n=1, intersect=True):

    if n == 1:
        freq = find_freq(text)
    elif n == 2:
        freq = find_bigram_freq(text, intersect)
    prob = freq.values()
    entropy = sum(list(map(lambda x: -x * math.log2(x), prob)))
    entropy *= 1 / n
    return entropy
def find_redundant(h, alph):
    return 1 - (h/math.log2(alph))

# print(find_entropy("sdfdshmaksjhkjvsvksjrbvbjkdf", 1))

file = open("non_spaces_text.txt", 'rt')
non_spaces_text = file.read()
file.close()
file = open("spaces_text.txt", 'rt')
spaces_text = file.read()
file.close()

h1_spaces_freq = find_freq(spaces_text)
h1_without_spaces_freq = find_freq(non_spaces_text)
h2_with_spaces_intersec_freq = find_bigram_freq(spaces_text, True)
h2_without_spaces_intersec_freq = find_bigram_freq(non_spaces_text, True)
h2_with_spaces_freq = find_bigram_freq(spaces_text, False)
h2_without_spaces_freq = find_bigram_freq(non_spaces_text, False)

h1_with_spaces = find_entropy(spaces_text)
h1_without_spaces = find_entropy(non_spaces_text)
h2_with_spaces_intersec = find_entropy(spaces_text, 2, True)
h2_without_spaces_intersec = find_entropy(non_spaces_text, 2, True)
h2_with_spaces = find_entropy(spaces_text, 2, False)
h2_without_spaces = find_entropy(non_spaces_text, 2, False)

h1_with_spaces_redundant = find_redundant(h1_with_spaces, 34)
h1_without_spaces_redundant = find_redundant(h1_without_spaces, 33)
h2_with_spaces_intersec_redundant = find_redundant(h1_with_spaces, 34)
h2_without_spaces_intersec_redundant = find_redundant(h1_with_spaces, 33)
h2_with_spaces_redundant = find_redundant(h1_with_spaces, 34)
h2_without_spaces_redundant = find_redundant(h1_with_spaces, 33)


# import csv
#
#
# def write_result(filename, dict):
#     with open(filename, 'w') as fp:
#         root = csv.writer(fp, delimiter='\t')
#         root.writerow(["Bigram", "freq"])
#         for i, j in dict.items():
#            root.writerow([i, j])


# write_result("h1_spaces_freq.csv", h1_spaces_freq)
# write_result("h1_without_spaces_freq.csv", h1_without_spaces_freq)
# write_result("h2_with_spaces_intersec_freq.csv", h2_with_spaces_intersec_freq)
# write_result("h2_without_spaces_intersec_freq.csv", h2_without_spaces_intersec_freq)
# write_result("h2_with_spaces_freq.csv", h2_with_spaces_freq)
# write_result("h2_without_spaces_freq.csv", h2_without_spaces_freq)

print("h1 with spaces: ", h1_with_spaces, "redurendacy: ", h1_with_spaces_redundant)
print("h1 without spaces: ", h1_without_spaces, "redurendacy: ", h1_without_spaces_redundant)
print("h2_with_spaces_intersec: ", h2_with_spaces_intersec, "redurendacy: ", h2_with_spaces_intersec_redundant)
print("h2_without_spaces_intersec: ", h2_without_spaces_intersec, "redurendacy: ", h2_without_spaces_intersec_redundant)
print("h2_with_spaces: ", h2_with_spaces, "redurendacy: ", h2_with_spaces_redundant)
print("h2_without_spaces: ", h2_without_spaces, "redurendacy: ", h2_without_spaces_redundant)