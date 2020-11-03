import inspect
import sys
import linecache

class GreenTracer(object):
    def __init__(self):
        self.lastframe = None

    def traceit(self, frame, event, arg):
        function_code = frame.f_code
        function_name = function_code.co_name
        lineno = frame.f_lineno
        vars = frame.f_locals

        source_lines, starting_line_no = inspect.getsourcelines(frame.f_code)
        loc = f"{function_name}:{lineno} {source_lines[lineno - starting_line_no].rstrip()}"
        vars = ", ".join(f"{name} = {vars[name]}" for name in vars)

        print(f"{loc:50}")

        return self.traceit
