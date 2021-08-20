# c = 1*p + 0*w + 6*g
# h = 0*p + 2*w + 12*g
# o = 2*p + 1+w + 6*g
c, h, o = map(int, input().split())
p = -0.25 * h + 0.5 * o
w = -1 * c + 0.25 * h + 0.5 * o
g = c / 6 + h / 24 - o / 12
p = round(p)
w = round(w)
g = round(g)
if p >= 0 and w >= 0 and g >= 0 and (c == 1 * p + 0 * w + 6 * g) and (h == 0 * p + 2 * w + 12 * g) and (o == 2 * p + 1 * w + 6 * g):
    print(w, p, g)
else:
    print('Error')
