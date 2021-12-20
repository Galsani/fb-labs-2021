import random

A_secret = {}
A_open = {}
B_secret = {}
B_open = {}
simple = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]

def func(a, b):
    if (b == 0):
        d = [a, 1, 0]
        return d
    else:
        d = func(b, a % b)
        y = d[1]
        x = d[2]
    #    print(a,b)
        return (d[0], x, y - (a // b) * x)

def revers(a, b):
    if (gcd(a, b)!= 1):
        return None
    else:
        return func(a, b)[1]


def gornera(x, a, n):
    a_bin = bin(a)[2:][::-1]
    tmp = [x]
    for i in range(1,len(a_bin)):
        tmp.append((tmp[i-1]**2)%n)
    all = 1
    for i in range(len(a_bin)):
        if a_bin[i] == '1':
            all = (all *tmp[i])%n
    return all

def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)

def is_simple(number):
    for i in simple:
        if number % i == 0:
            return False
    return True

def random_number():
    simpliness = False
    while simpliness == False:
        simpliness = True
        #Шаг0
        p = int(random.getrandbits(256))#псевдослучайное число в диапазоне
        print("Posibble: ", p)
        if is_simple(p) == False:
            simpliness = False
            continue
        #находим расклад
        i = 0
        temp = p - 1
        while temp % 2 == 0:
            temp = temp//2
            i += 1
        s = i
        d = int(temp)

       # d = int(d) if d == int(d) else print("Error")
        #print(p, s, d)#нашли расклад
        #Шаг 1
        for k in range(0, 8):
            x = random.randint(2, p-1)
            if gcd(x, p) > 1:
                simpliness = False
                break
            #Шаг 2
            temp = gornera(x, d, p)
            if temp == 1 or temp == -1 or temp == p-1:
                continue
            else:
                for i in range(1, s):
                    x = gornera(x, 2, p)
                    if x == -1 or x == p-1:
                        simpliness = True
                        break
                    elif x == 1:
                        simpliness = False
                        break
                else:
                    simpliness = False
    return p


keys = []
def get_keys():
    for i in range(0, 4):
        keys.append(random_number())
    if keys[0]*keys[1] < keys[2]*keys[3]:
        return True
    else:
        keys.clear()
        get_keys()


def take_e_d(pp, qq):
    y = (pp - 1) * (qq - 1)
    while 1:
        e = random.randint(2, y-1)
        if gcd(e, y) == 1:
            break
    d = revers(e, y) % y
    return e, d

def build_rsa():
    get_keys()
    A_secret['p'] = keys[0]
    A_secret['q'] = keys[1]
    A_open['e'], A_secret['d'] = take_e_d(A_secret['p'], A_secret['q'])
    A_open['n'] = A_secret['p']*A_secret['q']
    B_secret['p'] = keys[2]
    B_secret['q'] = keys[3]
    B_open['e'], B_secret['d'] = take_e_d(B_secret['p'], B_secret['q'])
    B_open['n'] = B_secret['p'] * B_secret['q']

def encrypt_rsa(m, e, n):
    k = gornera(m, e, n)
    return k

def decrypt_rsa(c, d, n):
    return gornera(c, d, n)%n

def auth_encrypt(k, d, e1, n1, n):
    S = gornera(k, d, n)
    S1 = gornera(S, e1, n1)
    k1 = encrypt_rsa(k, e1, n1)
    return k1, S1

def auth_decrypt(k1, S1, d, n, e1, n1):
    S = decrypt_rsa(S1, d, n)
    k = decrypt_rsa(k1, d, n)
    auth = gornera(S, e1, n1)
    if k == auth:
        print("its cool")
    else:
        print("meh")
    return k

for i in keys:
    print(i)

build_rsa()
kk = random.randint(0, A_open['n'] -1)
kk1, SS1 = auth_encrypt(kk, A_secret['d'], B_open['e'], B_open['n'],  A_open['n'])
r = auth_decrypt(kk1, SS1, B_secret['d'], B_open['n'], A_open['e'], A_open['n'])
print("Secret A: ", A_secret['d'], "\nOpen A: ", A_open, "\nSecret B: ", B_secret['d'], "\nOpen B: ", B_open)
print("Plaintext: ", kk, "\nCiphertext: ", kk1)
if kk == r:
    print(len(simple))