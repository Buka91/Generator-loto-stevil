# -*- coding: utf-8 -*-

import random

def lottoCombination():

    combination = list()

    print "Program: Welcome to the Lottery numbers generator."
    print "Program: Please enter how many random numbers 1 - 50 would you like to have:"
    number = raw_input("User: ")
    err = False
    try:
        number = int(number)
    except:
        err = True

    while number < 1 or number > 50 or err:
        print "Program: Please enter how many random numbers 1 - 50 would you like to have:"
        number = raw_input("User: ")
        try:
            number = int(number)
            err = False
        except:
            err = True

    lottoNumbers = range(1, 51)
    for i in range(number):
        picked_number = random.choice(lottoNumbers)
        combination.append(picked_number)
        lottoNumbers.remove(picked_number)

    print "Program: " + str(combination)
    print "Program: END"

if __name__ == "__main__":
    lottoCombination()