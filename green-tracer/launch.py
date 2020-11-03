import sys
import random

from computation.matrix import *
from computation.htb import *
from green_tracer import GreenTracer

if __name__ == "__main__":
    with open('green-tracer/input/input', 'r') as input:
        data = [int(x) for x in input.read().split('\n')]
    sys.settrace(GreenTracer().traceit)
    HeadTailBreakAlgo().htb(data)
    sys.settrace(None)
