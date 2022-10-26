# -*- coding: utf-8 -*-
# @Time    : 2022/8/4 9:40
# @Author  : Nickel_Chieh
# @Software: PyCharm

import random
import matplotlib.pyplot as plt


def coin_flip(min, max):
    ratios = []
    x = range(min, max + 1)
    for number_flip in x:
        print(number_flip)
        numHeads = 0
        for n in range(number_flip):
            if random.random() < 0.5:
                numHeads += 1
        if number_flip == numHeads:
            ratios.append(-1)
        else:
            numTails = number_flip - numHeads
            ratios.append(numHeads / float(numTails))
    plt.title("Heads/Tails Ratios")
    plt.xlabel("Number of flip")
    plt.ylabel("Heads/Tails")
    plt.plot(x, ratios, 'o', alpha=0.3, color='g')
    plt.hlines(1, 0, x[-1], linestyles='dashed', colors='y')
    plt.show()


coin_flip(2, 1000)
