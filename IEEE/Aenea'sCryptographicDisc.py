import math
r = int(input())
# add the letters and degrees to dictionary
degrees = dict()
for i in range(26):
    letter, degree = map(str, input().split())
    degrees[letter] = degree
# change the phrase to uppercase and create a new string without signs
phrase = str(input()).upper()
result = r
onlyLetters = []
for i in phrase:
    if i.isalpha():
        onlyLetters.append(i)
letters = ''.join(letter for letter in onlyLetters)
# cals the length of the thread with the formula of calc chord
# https://en.wikipedia.org/wiki/Chord_(geometry)
for i in range(1, len(letters)):
    result += (2 * (r *
                    abs(math.sin(math.radians(abs(float(degrees[letters[i]]) - float(degrees[letters[i - 1]])) / 2)))))

print(math.ceil(result))
