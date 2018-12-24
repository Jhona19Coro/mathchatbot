###############################################################################
# File: mcb.py.
# Description: (Rudimentary) MathChatBot.
# Author: Adrian Manea.
###############################################################################
import time                      # for keeping progress
from nltk.corpus import wordnet as wn

# log file
mcb = open("mcb.txt", "a+")      # append for progress keeping

# write execution time
mcb.write("=== " + str(time.strftime("%c")) + " ===\n")

# Math words
lim = 'limit'
su = 'sum'
pr = 'product'
intg = 'integral'
der = 'derivative'
dif = 'diferential'
exp = 'exponential'
log = 'logarithm'
fr = 'fraction'
calc = 'calculus'
an = 'analysis'
mwords = [lim, su, pr, intg, der, dif, exp, log, fr, calc, an]

# WordNet resources
for mw in mwords:
    ss = wn.synsets(mw)
    count = 0
    for s in ss:
        mcb.write("WORD: " + str(s.lemmas()[0].name()))
        mcb.write("\n")
        mcb.write("Sense no. " + str(count) + ": " + str(s.definition()))
        mcb.write("\n")
        print("WORD: " + str(s.lemmas()[0].name()))
        print("Sense no. " + str(count) + ": " + str(s.definition()))
        count += 1
    mcb.write("--------------------------------------------------\n")
    print("-----------------------------------------------------------------")

# to keep:
# limit -> sense 3, 4
# sum -> sense 1, 5
# product -> sense 2, 5
# integral -> sense 0
# derivative -> sense 0
# exponential -> sense 0
# logarithm -> sense 0 (THE ONLY ONE)
# fraction -> sense 2
# calculus -> sense 2
# analysis -> sense 4


mcb.close()
