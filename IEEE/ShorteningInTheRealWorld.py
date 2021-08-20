def base62(n):
    # split every number at n to list in base 62
    numbers = []
    while n:
        numbers.append(int(n % 62))
        n //= 62
    return numbers[::-1]


originURL = str(input())
numbersOfURL = int(input())
for i in range(numbersOfURL):
    baseURL = originURL
    targetURL = str(input())
    # step 1
    # change the url to hex base
    baseURL = [hex(ord(c)) for c in baseURL]
    targetURL = [hex(ord(c)) for c in targetURL]
    # make the urls size equal
    # targetUrl can be several time larger than baseURL
    urlLength = int(len(targetURL) // len(baseURL) + 1)
    for l in range(urlLength):
        baseURL += baseURL
    baseURL = baseURL[:len(targetURL)]
    # get the decimal value
    baseURL = [int(n, 16) for n in baseURL]
    targetURL = [int(n, 16) for n in targetURL]
    # XOR between the urls
    newURL = [hex(baseURL[i] ^ targetURL[i]) for i in range(len(baseURL))]
    # step 2
    # 0x?? -> ??
    numbersURL = [n[2:] for n in newURL[-8:]]
    # 0xc-> 0x0c
    for j in range(len(numbersURL)):
        if len(numbersURL[j]) != 2:
            numbersURL[j] = '0' + numbersURL[j]
    # change the hexadecimal to int
    numbersURL = int(''.join(numbersURL), 16)
    # step 3
    # https://en.wikipedia.org/wiki/ASCII
    # a-z -> 97-122  A-Z -> 65-90 sign-> 40-64
    resultURL = []
    for n in base62(numbersURL):
        if 10 <= n <= 35:
            resultURL.append(chr(n + 87))
        else:
            if n < 10:
                resultURL.append(str(n))
            else:
                resultURL.append(chr(n + 29))
    resultURL = originURL + '/' + ''.join(resultURL)
    print(resultURL)
