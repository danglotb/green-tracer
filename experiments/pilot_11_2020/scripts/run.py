import sys
import os

PYTHON_CMD = 'python3'
FOLDER_GREEN_TRACER = 'green-tracer/'
SCRIPT_OPT = '--script'
PATH_TO_SCRIPT_OPT = '--path-to-script'
OUTPUT_OPT = '--output'

PREFIX_OUTPUT_PATH = 'experiments/pilot_11_2020/output/traces'

PATH_VERSIONS = ['/home/benjamin/workspace/PythonV0', '/home/benjamin/workspace/Python']

SCRIPTS = ['balanced_parentheses.py']
PATHS_TO_SCRIPT = ['data_structures/stacks/']

def run_cmd(cmd):
    print(cmd)
    os.system(cmd)

if __name__ == '__main__':
    # green-tracer-path index-script-path-to-script index-version suffix-output
    green_tracer_path = sys.argv[1]
    index_script_and_path_to_script = int(sys.argv[2])
    index_version = int(sys.argv[3])
    suffix_output = '_'.join([str(index_version), sys.argv[4]])
    run_cmd(' '.join([
        PYTHON_CMD,
        FOLDER_GREEN_TRACER + green_tracer_path,
        SCRIPT_OPT, SCRIPTS[index_script_and_path_to_script],
        PATH_TO_SCRIPT_OPT, '/'.join([
            PATH_VERSIONS[index_version],
            PATHS_TO_SCRIPT[index_script_and_path_to_script]
        ]),
        OUTPUT_OPT, '_'.join([PREFIX_OUTPUT_PATH,  suffix_output])
    ]))
