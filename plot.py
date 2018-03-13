#!/usr/bin/env python3
import matplotlib.pyplot as p
from collections import Counter
import json


def removenoise(array, noiselvl=5):
    """Asume all values which appears just a few times are noise. Remove them."""
    amount, amountbevore = 0, 0
    previos, moreprevios = 0, 0
    for i in range(len(array)):  # Fucks up Beginning. Works fine after first row of at least 5 same values
        if array[i] == previos:
            amount += 1
        elif amount > noiselvl:
            moreprevios = previos
            amountbevore = amount
            previos = array[i]
            amount = 1
        else:
            for j in range(1, amount + 1, 1):
                if array[i - j] == 1:
                    array[i - j] = 0
                elif array[i - j] == 0:
                    array[i - j] = 1
                else:
                    print('Unknown symbol in Data')
            previos = moreprevios
            amount += amountbevore + 1
    return array


if __name__ == '__main__':

    with open('datar2.csv') as f:
        data = f.read()
    count, morecount = 0, 0
    prev, moreprev = 0, 0
    pri = 0
    largen = []
    oneplot = []
    plotdata = []
    data = removenoise([int(x) for x in data])
    for x in data:
        if x == prev:
            count += 1
        else:
            if prev == 0 and 50 < count and not pri:
                pri = 39000
                largen.append(round(count/100))
                count = 0
                prev = x
                continue
            if pri:
                oneplot.extend([int(prev) for _ in range(int(count/10))])
                if pri > count:
                    pri -= count
                else:
                    pri = 0
            elif not pri and oneplot:
                diffzero = [x for x in oneplot if x != 0]
                if diffzero and oneplot:
                    plotdata.append(oneplot)
                oneplot = []
            prev = x
            count = 0

    print(json.dumps(Counter(largen), sort_keys=True))
    
    p.figure(figsize=(220, 5))
    datase = 0
    for dataset in plotdata:
        p.plot(plotdata[:3200000])
        p.tight_layout()
        p.xlim(xmin=0)
        p.savefig('data{0}.png'.format(datase))
        p.clf()
        datase += 1
