import random

number = 1E4
bound = 1E6
with open('green-tracer/input/input', 'w') as file:
    file.write('\n'.join([str(random.randint(int(-bound), int(bound))) for x in range(0, int(number))]))
