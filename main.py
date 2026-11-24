#!/usr/bin/env python3
"""Two Lines to Your Past Self — make.fun entry.

Pass 1 (final): the loan-letter warning.
Line 1 names one concrete moment — Dad asking at Sunday dinner, the loan
letter still in the coat pocket. Line 2 traces the cause and effect: the
lie survives six months, Dad finds the letter, and the cost is the one
person who would have helped pay it off. Plain voice, addressed to one
specific person, no cleverness for its own sake.

Pass 2 (challenger, rejected): "Don't skip the last training run before the
marathon, the cold Tuesday one at 6 a.m. in the rain. / You hit the wall at
mile 22, and the finish line you miss is the only thing you think about
for a year." Rejected: the moment is concrete, but "hit the wall" is a
stock sports phrase and the consequence (thinking about it for a year) is
weaker cause-and-effect than losing the one person who would have helped.
The loan line wins on criteria 2 and 3.
"""

import os

ENTRY = (
    "Don't tell Dad the business is fine when he asks at Sunday dinner, "
    "with the loan letter still in your coat pocket.\n"
    "He finds it six months later, and the lie costs you the one person "
    "who would have paid it off with you."
)

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
