from cprint import cprint
import turbofunc, copy

def tspc(*args, **kwargs):
    return turbofunc.string_plus_clear(*args, **kwargs, backspace=True)

oc = copy.deepcopy(cprint)
class cprint(oc):
    def info(string, *args, **kwargs):
        if not kwargs.get("no", False):
            string = tspc(string)
        try:del kwargs['no']
        except:pass
        oc.info(string, *args, **kwargs)
    def ok(string, *args, **kwargs):
        if not kwargs.get("no", False):
            string = tspc(string)
        try:del kwargs['no']
        except:pass
        oc.ok(string, *args, **kwargs)
    def warn(string, *args, **kwargs):
        if not kwargs.get("no", False):
            string = tspc(string)
        try:del kwargs['no']
        except:pass
        oc.warn(string, *args, **kwargs)
    def err(string, *args, **kwargs):
        if not kwargs.get("no", False):
            string = tspc(string)
        fatal = kwargs.get("fatal", False)
        try: del kwargs['fatal']
        except: pass
        try:del kwargs['no']
        except:pass
        oc.err(string, fatal, *args, **kwargs)
    def fatal(string, *args, **kwargs):
        if not kwargs.get("no", False):
            string = tspc(string)
        fatal = kwargs.get("fatal", False)
        try: del kwargs['fatal']
        except: pass
        try:del kwargs['no']
        except:pass
        oc.fatal(string, fatal, *args, **kwargs)
