import sys  # arguments
import math # logarithm

ruDict = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

def sortDict(rawDict):
    sortedDict = {}
    for i in sorted(rawDict):
        sortedDict[i]=rawDict[i]
    return sortedDict

def flipSortDict(rawDict):
    sortedDict = {}
    invDict = {v: k for k, v in rawDict.items()}
    for i in sorted(invDict, reverse=True):
        sortedDict[i]=invDict[i]
    return {v: k for k, v in sortedDict.items()}

def H(ensemble):
    h = 0
    for z in ensemble:
        p = ensemble[z]
        h += p*math.log(p,2) # With the base 2.
    return -h


if len(sys.argv) < 2:
    print("Usage: entrophyCalculator.py <source file>")
    exit(0)

f = open(sys.argv[1])

freq = {}
for string in f:
    for i in string:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

f.seek(0)

biFreq = {}
for string in f:
    for i in range(0, len(string) - 1, 2): # ..., 2) to count bigrams with 2 char step.
        biGram = string[i:i+2]
        if biGram in biFreq:
            biFreq[biGram] += 1
        else:
            biFreq[biGram] = 1

totalChars = 0
for i in freq:
    totalChars += freq[i]
totalBiChars = 0                           # Same as totalChars - 1 (for step = 1).
for bi in biFreq:
    totalBiChars += biFreq[bi]

# Now we have the pairs "char - how many times it was in the text".
# Let's calculate the frequency.

for i in freq:
    freq[i] = freq[i]/totalChars
for bi in biFreq:
    biFreq[bi] = biFreq[bi]/totalBiChars

#print(str(flipSortDict(freq)), end="\n\n\n")
#print(str(sortDict(biFreq)), end="\n\n\n")
freq = flipSortDict(freq)
for key in freq:
    print(key,"\t",freq[key])

biFreq = sortDict(biFreq)
f = open('biFreq.csv', 'w')
for letter1 in ruDict:
    for letter2 in ruDict:
        bi = letter1+letter2
        if bi in biFreq:
            #f.write(bi)
            #f.write(',')
            f.write("{:,.6f}".format(biFreq[bi]))
            f.write(',')
        else:
            f.write(',')#,
    f.write('\n')
print('\nbiFreq matrix was written in the \"biFreq.csv\" file.\n')
print("H_1 = ", H(freq))
print("H_2 = ", 0.5*H(biFreq))

