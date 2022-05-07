"""
Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0-100,
100-200, and so on. While the second dimension represents the prime numbers in
that range
"""

def prime_list(num1, num2):
    list_ = []
    for i in range(num1, num2):
        count = 0
        for j in range(1, i):
            if i % j == 0:
                count += 1
        if count >= 2:
            continue
        if count < 2:
            list_.append(i)
    return list_


if __name__ == "__main__":
    array = []
    a = 1
    b = 100
    while b < 1000:
        out_list = prime_list(a, b)
        array.append(out_list)
        a += 100
        b += 100

    print(array)