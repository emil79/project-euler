def number_word(n):
    if n == 1000:
        s = "one thousand"
    elif n >= 100:
        q, r = divmod(n, 100)
        s = number_word(q) + " hundred"
        if r:
            s += " and " + number_word(r)
    elif n >= 20:
        q, r = divmod(n, 10)
        s = ("twenty", "thirty", "forty", "fifty",
             "sixty", "seventy", "eighty", "ninety")[q - 2]
        if r:
            s += " " + number_word(r)
    else:
        s = ("one", "two", "three", "four", "five", "six",
             "seven", "eight", "nine", "ten", "eleven", "twelve",
             "thirteen", "fourteen", "fifteen", "sixteen",
             "seventeen", "eighteen", "nineteen")[n - 1]
    return s

print len(''.join([number_word(i + 1) for i in range(1000)]).replace(' ', ''))
