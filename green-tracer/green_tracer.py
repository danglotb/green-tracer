import inspect
import sys
import linecache
import os

class GreenTracer(object):

    def traceit(self, frame, event, arg):
        function_code = frame.f_code
        filename = function_code.co_filename
        function_name = function_code.co_name
        lineno = frame.f_lineno
        if 'python_script_path' in frame.f_globals:
            filename = frame.f_globals['python_script_path']
        print('%s %s:%d' % (filename, function_name, lineno))
        return self.traceit

if __name__ == '__main__':
    sys.settrace(GreenTracer().traceit)
    python_script_path = sys.argv[1]
    sys.argv = sys.argv[1:]
    exec(open(python_script_path).read())
    sys.settrace(None)
