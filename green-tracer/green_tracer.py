import inspect
import sys
import linecache

class GreenTracer(object):

    def traceit(self, frame, event, arg):
        filename = frame.f_globals["__file__"]
        function_code = frame.f_code
        function_name = function_code.co_name
        lineno = frame.f_lineno
        print('%s %s#%s:%d' % (filename, list(frame.f_globals.keys())[-1], function_name, lineno))
        return self.traceit
