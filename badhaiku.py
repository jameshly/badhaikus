import random
import syllables
from itertools import permutations
from PyDictionary import PyDictionary
fiveword_file = "5words.txt"
FIVEWORDS = open(fiveword_file).read().splitlines()
sevenword_file = "7words.txt"
SEVENWORDS = open(sevenword_file).read().splitlines()
#first line
fl= []
fls = 5
while fls > 0:
    cand = FIVEWORDS[random.randint(0,440529)]
    candsyll = syllables.estimate(cand)
    if candsyll < fls:
        print(cand)
        fl.append(cand)
        fls = fls - candsyll
sl = []
sls = 7
while fls > 0:
    cand = SEVENWORDS[random.randint(0,465357)]
    candsyll = syllables.estimate(cand)
    if candsyll < sls:
        print(cand)
        sl.append(cand)
        sls = sls - candsyll
tl = []
tls = 7
while fls > 0:
    cand = FIVEWORDS[random.randint(0,440529)]
    candsyll = syllables.estimate(cand)
    if candsyll < tls:
        print(cand)
        tl.append(cand)
        tls = tls - candsyll

print(fl)
print(sl)
print(tl)