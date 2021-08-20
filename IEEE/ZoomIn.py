c = int(input())
r = int(input())
k = int(input())
zoom = dict()  # a example of a word
for s in range(k):
    ch = str(input())
    # create the example by a 2d array
    zoomIn = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        row = list(str(input()))
        #for j in range(c):
        zoomIn[i] = row
    zoom[ch] = zoomIn
amountOfZoom = int(input())
for size in range(amountOfZoom):
    sentence = str(input())
    for i in range(r):
        for k in sentence:
            for j in range(c):
                print(zoom[k][i][j], end='')
        print('')
