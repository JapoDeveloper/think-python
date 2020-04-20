def histogram(s):
    d = dict()
    for l in s:
        d[l] = d.get(l, 0) + 1
    return d


h = histogram('Hello everybody')
print(h)
