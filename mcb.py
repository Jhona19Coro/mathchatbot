###############################################################################
# File: mcb.py.
# Description: (Rudimentary) MathChatBot.
# Author: Adrian Manea.
# Disclaimer: There are a lot of elementary hacks here, I know.
#             But I had fun making it and that's what I care about.
###############################################################################
import time                      # for keeping progress
import sys                       # for writing the log in a variable file
import os                        # no transcript wanted, write it and trash it
import random
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
if len(sys.argv) != 2:
    if len(sys.argv) > 2:           # too many arguments
        print("The program must be run with one mandatory argument " +
              "(program name)")
        print("and one optional argument (filename for transcript).")
        print("Please rerun it. Exiting...")
        sys.exit()
    if len(sys.argv) == 1:          # no arguments
        print("You have not chosen a transcript file.")
        print("The interaction will be showed in the console only.")
        print("You can:")
        print("(1) Continue with no transcript;")
        print("(2) Add a transcript filename;")
        print("(3) Exit.")
        co = str(input())
        while ('1' not in co and '2' not in co and '3' not in co):
            print("Invalid choice. Please retry.")
            print("You can:")
            print("(1) Continue with no transcript;")
            print("(2) Add a transcript filename;")
            print("(3) Exit.")
            co = str(input())
        if '3' in co:
            print("Exiting...")
            sys.exit()
        if '2' in co:
            print("Please input a filename with extension " +
                  "(no spaces or special characters):")
            sys.argv.append(str(input()))
        if '1' in co:
            sys.argv.append("temp.txt")
mcb = open(str(sys.argv[1]), "w")

# write execution time
mcb.write("=== " + str(sys.argv[0]) + " ===\n")
mcb.write("=== " + str(time.strftime("%c")) + " ===\n")

# Math words
gr = 'group'
lim = 'limit'
su = 'sum'
pr = 'product'
intg = 'integral'
der = 'derivative'
dif = 'differential'
exp = 'exponential'
log = 'logarithm'
fr = 'fraction'
calc = 'calculus'
an = 'analysis'
mwords = [gr, lim, su, pr, intg, der, dif, exp, log, fr, calc, an]

# Predefined verbs
study = 'study'
learn = 'learn'
practice = 'practice'
read = 'read'
exercise = 'exercise'
define = 'define'
mverbs = [study, learn, practice, read, exercise, define]

# MANUALLY add the appropriate senses...
wndb = [
    wn.synsets(gr)[0],          # group (number of entities)
    wn.synsets(gr)[2],          # group (algebra)
    wn.synsets(lim)[3],         # limit 1 (calculus)
    wn.synsets(lim)[4],         # limit 2 (boundary)
    wn.synsets(su)[1],          # sum (addition)
    wn.synsets(su)[2],          # sum ('the final aggregate')
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

polyw = [wndb[j] for j in range(0, 7)]
wndbNames = [s.lemmas()[0].name() for s in wndb]

# Predefined replies
more = 'What else do you want to talk about?'
practice = 'Practice makes perfect, you know?'
notu = "Sorry, I don't understand. Could you try something else, please?"
he = 'Hi, how can I help you today?'
leave = 'You can always end the conversation saying goodbye.'
topics = "Here are the topics I know something about:"

# By verb
studyR1 = "I'm sure there are many resources you can check out. " + \
    "You can start by reading some Wikipedia."
studyR2 = "You should start by reading from the course textbook."
studyR3 = "Reading your course notes is always a good start."
studyR4 = "You can get together with some colleagues and try studying " + \
    "through discussions and debates if that works for you."
studyR5 = "Set aside at least 30 minutes each day and read through your notes."
studyReplies = [studyR1, studyR2, studyR3, studyR4, studyR5]
practiceR1 = "You can always start with the exercises in the textbook."
practiceR2 = "First, read the theory, then try solving some exercises " + \
    "in the textbook. See how that works for you."
practiceR3 = "You can find some good exercises on Project Euler."
practiceR4 = "Get a list of exercises from you professor and try " + \
    "solving those first."
practiceR5 = "It's always a good idea to start by reading the theory, though."
practiceReplies = [practiceR1, practiceR2, practiceR3, practiceR4, practiceR5]


# Conversation
print(he)
print(topics)
mcb.write(he + "\n")
mcb.write(topics + "\n")
for topic in mwords:
    print(topic)
    mcb.write(topic + "\n")
print("I can help you", end=" { ")
mcb.write("I can help you { ")
for vcount in range(0, len(mverbs) - 1):
    print(mverbs[vcount], end=", ")
    mcb.write(mverbs[vcount] + ", ")
print(mverbs[-1], end=" } ")
mcb.write(mverbs[-1] + " } ")
print("some of these.")
mcb.write("some of these.\n")
print(leave)
mcb.write(leave + "\n")
reply = str(input("--> "))
mcb.write("--> " + reply + "\n")

while ('BYE' not in reply.upper()):
    # Parse the reply, looking for nouns and verbs
    tokens = nltk.word_tokenize(reply)
    parts = dict(tagger.tag(tokens))
    verbs = [part for part in parts.keys() if "VB" in parts.get(part)
             or "VP" in parts.get(part)]
    verbsUpper = [v.upper() for v in verbs]
    nouns = [part for part in parts.keys() if "NN" in parts.get(part)
             or "NP" in parts.get(part)]
    nounsUpper = [n.upper() for n in nouns]
    while (not verbs and not nouns):
        print(notu)
        print(leave)
        reply = str(input("--> "))
        mcb.write("--> " + reply + "\n")
    # Make list of all senses of the NOUNS in the reply
    nounSenses = [nn for noun in nouns for nn in wn.synsets(noun)]
    # Get the one which is most similar to what's in the DB
    # Make it a dictionary! {synset:similarity}
    nounSimsDict = {word.path_similarity(part): word for part in
                    nounSenses for word in wndb}
    # Store (nonzero) similarity scores separately, to get max
    nounSimsLs = [k for k in nounSimsDict.keys() if k]
    theNounSS = nounSimsDict[max(nounSimsLs)]
    theNounSSLemma = nounSimsDict[max(nounSimsLs)].lemmas()[0]
    theNounName = theNounSSLemma.name()
    theNounDef = nounSimsDict[max(nounSimsLs)].definition()
    ans = False
    if ('LEARN' in verbsUpper or 'STUDY' in verbsUpper):
        print('So, you want to learn about ' + theNounName +
              ' or something related.')
        mcb.write('So, you want to learn about ' + theNounName +
                  ' or something related.' + "\n")
        print(random.choice(studyReplies))
        mcb.write(random.choice(studyReplies) + "\n")
        ans = True
    if ('EXERCISE' in verbsUpper or 'PRACTICE' in verbsUpper
       or 'EXERCISE' in nounsUpper or 'PRACTICE' in nounsUpper):
        mcb.write(practice + "\n")
        mcb.write(random.choice(practiceReplies) + "\n")
        print(practice)
        print(random.choice(practiceReplies))
        ans = True
    if 'READ' in verbsUpper:
        print('There are great resources for reading about ' +
              theNounName + ' and related stuff.')
        mcb.write('There are great resources for reading about ' +
                  theNounName + ' and related stuff.\n')
        print(random.choice(studyReplies))
        mcb.write(random.choice(studyReplies) + "\n")
        ans = True
    if ('DEFINE' in verbsUpper or 'DEFINITION' in nounsUpper):
        print('I can give you the definition of ' + theNounName + '.')
        mcb.write('I can give you the definition of ' + theNounName + '.\n')
        if theNounSS not in polyw:
            print("Here it is: ")
            mcb.write("Here it is: \n")
            print('> Definition: ' + theNounDef)
            mcb.write('> Definition: ' + theNounDef + "\n")
        else:
            # If polysemantic,
            # find which one of them it is
            senses = []
            for poly in polyw:
                if poly.lemmas()[0].name() == theNounSS.lemmas()[0].name():
                    senses.append(poly)
            print("I know " + str(len(senses)) + " definitions of " +
                  theNounName + ".")
            mcb.write("I know " + str(len(senses)) + " definitions of " +
                      theNounName + ".\n")
            count = 0
            mcb.write('Here is one of them:\n')
            print('Here is one of them: ')
            print('> Definition: ' + senses[count].definition())
            mcb.write('> Definition: ' + senses[count].definition() + "\n")
            count += 1
            print("Is this what you were after?")
            mcb.write("Is this what you were after?\n")
            yn = str(input("--> "))
            mcb.write("--> " + yn + "\n")
            while ("YES" not in yn.upper()
                   and "NO" not in yn.upper()):
                mcb.write("Please answer 'yes' or 'no'\n")
                print("Please answer 'yes' or 'no'")
                yn = str(input("--> "))
                mcb.write("--> " + yn + "\n")
            if ("YES" in yn.upper()):
                mcb.write("Great then!\n")
                print("Great then!")
            while ("NO" in yn.upper()):
                if count < len(senses):
                    print('Here is another one: ')
                    mcb.write("Here is another one:\n")
                    print('> Definition: ' + senses[count].definition())
                    mcb.write('> Definition: ' + senses[count].definition() +
                              "\n")
                    count += 1
                    print("Is this what you were after?")
                    mcb.write("Is this what you were after?\n")
                    yn = str(input("--> "))
                    mcb.write("--> " + yn + "\n")
                else:
                    print('I know no further, sorry.')
                    mcb.write('I know no further, sorry.\n')
                    break
        ans = True
    if not ans:
        print(notu)
        print(leave)
        mcb.write(notu + "\n")
        mcb.write(leave + "\n")
    print(more)
    print(leave)
    mcb.write(more + "\n")
    mcb.write(leave + "\n")
    reply = str(input("--> "))
    mcb.write("--> " + reply + "\n")

print("==================== PROGRAM TERMINATED ====================")
mcb.write("==================== PROGRAM TERMINATED ====================\n")

if (len(sys.argv) == 1 and '1' in co):
    os.remove("temp.txt")

mcb.close()
