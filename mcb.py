###############################################################################
# File: mcb.py.
# Description: (Rudimentary) MathChatBot.
# Author: Adrian Manea.
###############################################################################
import time                      # for keeping progress
import nltk
from nltk.corpus import wordnet as wn
from nltk.tag.stanford import StanfordPOSTagger


# Setup POS Tagger
cale_model = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "models/english-bidirectional-distsim.tagger"
cale_jar_tagger = "/home/t3rtius/Documents/cs/sla-master/sem1/1-nlp-opt/" + \
    "stanford-pos-tagger/stanford-postagger-full-2018-10-16/" + \
    "stanford-postagger.jar"
tagger = StanfordPOSTagger(cale_model, cale_jar_tagger)

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
mverbsWN = [vbss for verb in mverbs for vbss in wn.synsets(verb)]

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
notu = "Sorry, I don't understand. Could you try something else, please?"
he = 'Hi, how can I help you today?'
leave = 'You can always end the conversation saying goodbye.'

# Giving definitions
# print(hi + subj)
# reply = str(input())

# while ('BYE' not in reply.upper() and 'NO' not in reply.upper()):
#     if reply not in wndbNames:
#         print(idk + reply + ". " + els)
#     else:
#         print("I can give you the definition of that. Here it is:")
#         for ss in wndb:
#             if ss.lemmas()[0].name() in reply:
#                 print("> Definition: " + ss.definition())
#     print(more)
#     reply = str(input())


# Conversation
print(he)
reply = str(input())

while ('BYE' not in reply.upper()):
    # Parse the reply, looking for nouns and verbs
    tokens = nltk.word_tokenize(reply)
    parts = dict(tagger.tag(tokens))
    verbs = [part for part in parts.keys() if "VB" in parts.get(part)]
    nouns = [part for part in parts.keys() if "NN" in parts.get(part)]
    if (not verbs and not nouns):
        print(notu)
        print(leave)
        reply = str(input())
    # Make list of all senses of the NOUNS in the reply
    nounSenses = [nn for noun in nouns for nn in wn.synsets(noun)]
    # Get the one which is most similar to what's in the DB
    # Make it a dictionary! {synset:similarity}
    nounSimsDict = {word.path_similarity(part): word for part in
                    nounSenses for word in wndb}
    # Store similarity scores separately, to get max
    nounSimsLs = [word.path_similarity(part) for part in nounSenses
                  for word in wndb]
    theNounSS = nounSimsDict[max(nounSimsLs)].lemmas()[0]
    theNounName = theNounSS.name()
    theNounDef = nounSimsDict[max(nounSimsLs)].definition()
    verbsUpper = [v.upper() for v in verbs]
    if ('LEARN' in verbsUpper or 'STUDY' in verbsUpper):
        print('So, you want to learn about ' + theNounName +
              ' or something like that.')
        print('There are great resources on the web you should try,')
        print(' like Wikipedia. But you better read the course manual.')
    if 'EXERCISE' in verbsUpper:
        print(practice)
        print('You should check out ProjectEuler.')
    if 'READ' in verbsUpper:
        print('There are great resources for reading about ' +
              theNounName + ' and related stuff.')
        print('You could try Wikipedia or the course manual.')
    if 'DEFIN' in verbsUpper:
        print('I can give you the definition of ' + theNounName + '.')
        print('Here it is: ')
        print('> Definition: ' + theNounDef)
    print(more)
    print(leave)
    reply = str(input())

mcb.close()
