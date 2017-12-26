"""Advent of Code
day25.py
Code by Dylan Sheehy
http://adventofcode.com/2017/day/25
"""

from turing import Turing

STATES = {
    'A': [
        {'write': 1, 'move': 1, 'next': 'B'}, # current value is 0
        {'write': 0, 'move': -1, 'next': 'C'} # current value is 1
    ],
    'B': [
        {'write': 1, 'move': -1, 'next': 'A'}, # current value is 0
        {'write': 1, 'move': 1, 'next': 'D'} # current value is 1
    ],
    'C': [
        {'write': 1, 'move': 1, 'next': 'A'}, # current value is 0
        {'write': 0, 'move': -1, 'next': 'E'} # current value is 1
    ],
    'D': [
        {'write': 1, 'move': 1, 'next': 'A'}, # current value is 0
        {'write': 0, 'move': 1, 'next': 'B'} # current value is 1
    ],
    'E': [
        {'write': 1, 'move': -1, 'next': 'F'}, # current value is 0
        {'write': 1, 'move': -1, 'next': 'C'} # current value is 1
    ],
    'F': [
        {'write': 1, 'move': 1, 'next': 'D'}, # current value is 0
        {'write': 1, 'move': 1, 'next': 'A'} # current value is 1
    ]
}

TM = Turing('A', STATES)
STEPS = 12919244
for i in range(STEPS):
    if i % 1000000 == 0:
        print(i)
    TM.run()

print(TM.checksum())
