import sys  # arguments

def index(cipherTextLen, Y):                   # cipherTextLen a.k.a. "n"
    koef = 1/((cipherTextLen)*(cipherTextLen-1))
    I = 0
    for key in Y:
        N_t=freq[key]
        I += koef*(N_t*(N_t-1))
    return I

if len(sys.argv) < 2:
    print("Usage: indexCalculator.py <source file>")
    exit(0)

f = open(sys.argv[1])

cipherTextLen = 0
freq = {}
for string in f:
    for symbol in string:
        cipherTextLen += 1
        if symbol in freq:
            freq[symbol] += 1
        else:
            freq[symbol] = 1

print("Index =", index(cipherTextLen, freq))
f.close()
