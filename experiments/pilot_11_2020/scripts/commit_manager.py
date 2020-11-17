import sys
import os
import csv

GIT_CMD = 'git -C'
PATH_V0 = '/home/benjamin/workspace/PythonV0'
PATH_V1 = '/home/benjamin/workspace/Python'
GIT_RESET_OPT = 'reset --hard'

PATH_COMMITS_FILE = 'experiments/pilot_11_2020/commits'

if __name__ == '__main__':
    with open(PATH_COMMITS_FILE) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for i in range(0, int(sys.argv[1])):
            next(csv_reader)
        row = next(csv_reader)
    commit_sha_v0 = row[1]
    commit_sha_v1 = row[2]
    os.system(' '.join([GIT_CMD, PATH_V0, GIT_RESET_OPT, commit_sha_v0]))
    os.system(' '.join([GIT_CMD, PATH_V1, GIT_RESET_OPT, commit_sha_v1]))
