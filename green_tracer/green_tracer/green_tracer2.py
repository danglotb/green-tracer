import inspect
import sys
import linecache
import os
import argparse
import importlib.util

class GreenTracer2(object):

    def __init__(self, output_path):
        self.output_path = output_path
        self.output_file = open(self.output_path, 'w')

    def is_std(self, filename):
        return filename.startswith('/usr/lib/python3.8') or \
            filename.startswith('<frozen ')

    def get_locals_and_values(self, locals):
        vars = []
        for var in locals:
            try:
                if not locals[var] == None and not var.startswith('__'):
                    try:
                        vars.append('='.join([var, locals[var].str()]))
                    except AttributeError:
                        try:
                            vars.append('='.join([var, str(locals[var])]))
                        except AttributeError:
                            vars.append(var)
            except AttributeError:
                return vars
        return vars

    def get_source_line(self, code):
        try:
            return inspect.getsourcelines(code)
        except OSError:
            return '', -1

    def traceit(self, frame, event, arg):
        function_code = frame.f_code
        filename = function_code.co_filename
        function_name = function_code.co_name
        lineno = frame.f_lineno
        name = frame.f_globals["__name__"]
        if 'python_script_path' in frame.f_globals:
            filename = frame.f_globals['python_script_path']
        vars = self.get_locals_and_values(frame.f_locals)
        line = linecache.getline(filename, lineno)
        self.output_file.write('%s:%s:%s:%d {%s} (%s)\n' % (filename, name, function_name, lineno, line.rstrip(), ','.join(vars)))
        return self.traceit

    def close(self):
        self.output_file.close()

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path-to-script', help='')
    parser.add_argument('--script', help='')
    parser.add_argument('--arguments', default='', help='')
    parser.add_argument('--output-path', help='', default='out.trace')
    args = parser.parse_args()
    tracer = GreenTracer(args.output_path)
    script_name = args.script
    path_to_script = args.path_to_script
    if not args.arguments == None:
        arguments = args.arguments.split(',')
    sys.path.append(path_to_script)
    sys.argv = [path_to_script + script_name] + arguments
    sys.settrace(tracer.traceit)
    exec(open(path_to_script + script_name).read())
    sys.settrace(None)
    tracer.close()
