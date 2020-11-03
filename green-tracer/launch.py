import sys
from computation.matrix import *
from green_tracer import GreenTracer

if __name__ == "__main__":
    sys.settrace(GreenTracer().traceit)
    main(int(sys.argv[1]), int(sys.argv[2]))
