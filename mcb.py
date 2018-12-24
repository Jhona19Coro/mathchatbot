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

# Predefined verbs
study = 'study'
learn = 'learn'
practice = 'practice'
read = 'read'
exercise = 'exercise'
mverbs = [study, learn, practice, read, exercise]

# WordNet resources
# for mw in mwords:
#     ss = wn.synsets(mw)
#     count = 0
#     for s in ss:
#         mcb.write("WORD: " + str(s.lemmas()[0].name()))
#         mcb.write("\n")
#         mcb.write("Sense no. " + str(count) + ": " + str(s.definition()))
#         mcb.write("\n")
#         print("WORD: " + str(s.lemmas()[0].name()))
#         print("Sense no. " + str(count) + ": " + str(s.definition()))
#         count += 1
#     mcb.write("--------------------------------------------------\n")
#     print("-----------------------------------------------------------------")

# MANUALLY add the appropriate senses...
wndb = [
    wn.synsets(lim)[3],         # limit 1 (calculus)
    wn.synsets(lim)[4],         # limit 2 (boundary)
    wn.synsets(su)[1],          # sum (addition)
    wn.synsets(su)[5],          # sum (set theory)
    wn.synsets(pr)[2],          # product (multiplication)
    wn.synsets(pr)[5],          # product (set theory)
    wn.synsets(intg)[0],        # integral
    wn.synsets(der)[0],         # derived_function
    wn.synsets(exp)[0],         # exponential
    wn.synsets(log)[0],         # logarithm
    wn.synsets(fr)[2],          # fraction
    wn.synsets(calc)[2],        # calculus
    wn.synsets(an)[4]           # analysis
]

wndbNames = [s.lemmas()[0].name() for s in wndb]

# Predefined replies
hi = 'Hi there! '
anything = 'Anything else?'
more = 'Would you like to talk some more?'
els = 'Would you like to try something else instead? '
bye = 'OK then. Bye!'
would = 'Would you like to '
idk = "Sorry, I don't know anything about "
practice = 'Practice makes perfect, you know?'
subj = 'What subject are you interested in today?'

# Giving definitions
print(hi + subj)
reply = str(input())

while ('BYE' not in reply.upper() and 'NO' not in reply.upper()):
    if reply not in wndbNames:
        print(idk + reply + ". " + els)
    else:
        print("I can give you the definition of that. Here it is:")
        for ss in wndb:
            if ss.lemmas()[0].name() in reply:
                print("> Definition: " + ss.definition())
    print(more)
    reply = str(input())

mcb.close()
