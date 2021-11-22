def gcd(a, b):
    if not b:
        return 1, 0, a
    y, x, d = gcd(b, a % b)
    return x, y - (a // b) * x, d
#a^-1, x, y
# print(gcd(30, 50))
# print(gcd(154, 803))

def re(a,b):
    x, _, _ = gcd(a, b)
    return x


def linear_comp(a, b, n):
    a_re, _, d = gcd(a, n)
    if d == 1:
        x = (a_re * b) % n
        return [x]
    else:
        solutions = []
        if b % d == 0:
            a1 = a / d
            b1 = b / d
            n1 = n / d
            x = linear_comp(a1, b1, n1)
            solutions_loc = linear_comp(a1, b1, n1)
            solutions.append(x[0])
            for i in range(1, d):
                solutions.append((x[0] + int(n / d) * i) % n)
            return solutions
        else:
            return None


# print(linear_comp(154, 22, 803))