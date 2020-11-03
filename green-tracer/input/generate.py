import random

bound = 1E3
with open('green-tracer/input/input', 'w') as file:
    file.write('\n'.join([str(random.randint(int(-bound), int(bound))) for x in range(0, int(bound))]))
