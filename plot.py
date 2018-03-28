#!/usr/bin/env python3
import matplotlib.pyplot as p


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
    output = []
    for x in data:
        if x == prev:
            count += 1
        else:
            if 50 < count:
                output.append((prev, count))
                count = 0
                prev = x
    parsedout = []
    lzero, lone = False, False
    for i in range(len(output)):
        if 82 < output[i][1] < 95:
            if output[i][0] == 0:
                parsedout.append(1)
                lone, lzero = True, False
        elif 114 < output[i][1] < 125:
            if output[i][0] == 1 and not lone:
                parsedout.append(1)
                lone, lzero = False, False
        elif 60 < output[i][1] < 77:
            if output[i][0] == 0:
                parsedout.append(0)
                lone, lzero = False, True
        elif 95 < output[i][1] < 105:
            if output[i][0] == 1 and not lzero:
                parsedout.append(0)
                lone, lzero = False, False

    print(str(output))
    print(str(parsedout))

    if False:
        p.figure(figsize=(220, 5))
        datase = 0
        # for dataset in plotdata:
        p.plot(data)
        p.tight_layout()
        p.xlim(xmin=0)
        p.savefig('data{0}.png'.format(datase))
        p.clf()
        datase += 1
