print max({sum(int(x) for x in str(a ** b))
           for a in range(100) for b in range(100)})
