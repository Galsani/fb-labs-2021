import sys

if len(sys.argv) < 3:
    print("Usage: entrophyCalculator.py <source file> <key>")
    exit(0)

f = open(sys.argv[1])
plainTextFile = open('plaintext.txt', 'w')
key = sys.argv[2]
keyLen = len(key)

for string in f:
    for i in range(0, len(string)):
        letter = string[i]
        plainTextFile.write(chr(ord('а') + (ord(letter) - ord(key[i%keyLen]))%32))


f.close()
plainTextFile.close()
