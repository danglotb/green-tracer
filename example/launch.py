import sys
import random

from computation.matrix import *
from computation.htbv0 import *
from computation.htbv1 import *
from green_tracer import GreenTracer

if __name__ == "__main__":
    with open('example/input/input', 'r') as input:
        data = [int(x) for x in input.read().split('\n')]
    sys.settrace(GreenTracer().traceit)
    result_v0 = HeadTailBreakAlgoV0().htb(data)
    result_v1 = HeadTailBreakAlgoV1().htb(data)
    if not result_v0 == result_v1:
        print('Someting went wrong')
    sys.settrace(None)
