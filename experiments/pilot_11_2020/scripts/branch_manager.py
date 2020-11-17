import sys
import os
import csv

GIT_CMD = 'git -C'
PATH_V0 = '/home/benjamin/workspace/PythonV0'
PATH_V1 = '/home/benjamin/workspace/Python'
GIT_CHECKOUT_OPT = 'checkout'

COMMIT = 'commit'
V0 = 'v0'
V1 = 'v1'

if __name__ == '__main__':
    commit_id = sys.argv[1]
    os.system(' '.join([GIT_CMD, PATH_V0, GIT_CHECKOUT_OPT, '-'.join([COMMIT, commit_id, V0])]))
    os.system(' '.join([GIT_CMD, PATH_V1, GIT_CHECKOUT_OPT, '-'.join([COMMIT, commit_id, V1])]))
