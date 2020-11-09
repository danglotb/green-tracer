import sys
import random

from computation.matrix import *
from computation.htbv0_pyjouled import *
from computation.htbv1_pyjouled import *

if __name__ == "__main__":
    with open('example/input/input', 'r') as input:
        data = [int(x) for x in input.read().split('\n')]
    for i in range(0, 100):
        result_v0 = HeadTailBreakAlgoV0().htb(data)
        result_v1 = HeadTailBreakAlgoV1().htb(data)
