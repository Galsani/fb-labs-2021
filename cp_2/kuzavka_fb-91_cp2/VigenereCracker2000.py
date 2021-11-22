import sys  # arguments

ANCHORLEN = 3
keyLen = 15

def flipSortDict(rawDict):
    sortedDict = {}
    invDict = {v: k for k, v in rawDict.items()}
    for i in sorted(invDict, reverse=True):
        sortedDict[i]=invDict[i]
    return {v: k for k, v in sortedDict.items()}

if len(sys.argv) < 2:
    print("Usage: VigenereCracker2000.py <source file>")
    exit(0)

f = open(sys.argv[1])

biFreq = {}
for string in f:
    for i in range(0, len(string) - 1, 1): # ..., 1) to count bigrams with 2 char step.
        biGram = string[i:i+ANCHORLEN]
        if biGram in biFreq:
            biFreq[biGram] += 1
        else:
            biFreq[biGram] = 1
biFreq = flipSortDict(biFreq)

# Make a target string for a frequency analysis.
crackableWithFreqAnal = ""

f.seek(0)
key = ''
print('Possible key: ', end= '')
for pos in range(0, keyLen):
    freq = {}
    crackableWithFreqAnal = ""
    
    for i in range(pos, len(string)-1, keyLen):  # Find every pos character and create crackable with frequency analysis string.
        crackableWithFreqAnal += string[i]
    for i in crackableWithFreqAnal:              # Calculate frequencies of each letter.
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    for dictKey in flipSortDict(freq):           # Get the key.
        print(chr(ord('а') + (ord(dictKey) - ord('о'))%32), end='')
        break;
print('\n')

print(biFreq)                                    # Guessing the length of the key.
print('Search for the common divisor for:')

for anchor in biFreq:
    anchorPos = []
    if biFreq[anchor] < 2:
        break
    print(anchor)
    f.seek(0)
    for string in f:
        for i in range(0, len(string) - 1, 1):
            word = string[i:i+ANCHORLEN]
            if word == anchor:
                anchorPos.append(i)

    anchorPos = [ele for ele in reversed(anchorPos)]
    for i in range(0, len(anchorPos)):
        if i+1 >= len(anchorPos):
            break
        else:
            print(anchorPos[i] - anchorPos[i+1])


f.close()
