# MathChatBot

This is a project that I chose as final homework for the NLP laboratory at the Security and Applied Logic Master's program at the University of Bucharest.

## Description
The project implements a (rudimentary) chatbot which (tries to) hold a conversation with you on mathematical topics. It will give you definitions of mathematical objects, ask you to study or to practice doing some exercises... y'know, nagging professor stuff.

## How does it work?
The program uses the `WordNet` database for all the words and definitions, as well as the `Stanford POS Tagger` for parsing phrases.

The bot greets you and asks you what do you want to learn (or talk) about.

- It has a database consisting of a list of synsets for mathematical (and related) terms. 
- It also has a database of specific verbs (e.g. *learn*, *study*, *know*, *practice*, *define*).
- It parses the line you enter, looking especially for *nouns* and *verbs* (rather, noun phrases and verbal phrases), as tagged by the Stanford POS Tagger.
- For each noun it found, it will make a list of similarity scores of it with respect to the nouns in the database, which will be sorted, to choose the one that is most relevant.
- For each verb it found, it will look it up in the database.
- Corresponding to the VP and NP, it will offer predefined answers.

## Example (planned) conversation
> -- Hi, I will be your MathChatBot for today. What subject are you interested in? <br />
> -- I want to *learn* about **derivatives**. <br />
> -- Would you like me to *define* the **derivatives** for you? 
> -- Yes. <br />
> -- [insert definition of derivative from WN here]. <br />
> Anything else?
> -- I would like to *practice* some **derivatives** **exercises**. <br />
> -- Well, then you should definitely check out some **exercises** in your course textbook.
> Anything else? <br />
> -- I would like to *read* about **exponentials**. <br />
> -- Do you mean (1) [one sense of the exponential] or (2) [second sense]? <br />
> -- 1. <br />
> -- You can check out some materials on Wikipedia or even better, in your course textbook.
> Anything else? <br />
> -- No, thanks. <br />
> -- OK, bye! <br />

## Further features (F) and ideas (I)
- (F) The bot will save the transcript in a text file.
- (I) The bot will provide clickable links by querying `ddg %q !w` for what you want to learn about.


## Tools used
- NLTK, Stanford POS Tagger, WordNet in Python 3;
- Emacs, Vim, st, GitLab.


## Other credits
Inspired by [ELIZA](https://en.wikipedia.org/wiki/ELIZA), see Common Lisp code [here](http://norvig.com/paip/eliza.lisp).
