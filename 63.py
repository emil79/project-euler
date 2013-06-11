from itertools import count

S = set()
for i in range(1, 10):
    for j in count(1):
        if len(str(i ** j)) < j:
            break
        S.add(i ** j)
print len(S)
