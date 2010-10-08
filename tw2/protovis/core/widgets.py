"""
TODO
"""

import tw2.core as twc
from tw2.core.resources import encoder
from tw2.protovis.core import resources as res

class PVPanel(twc.Widget):
    template = "genshi:tw2.protovis.core.templates.panel"
    resources = [res.pv_js]
   
    _initialized = twc.Variable('(bool)', default=False)
    _pv_prop_funcs = twc.Variable('(list) of JSSymbols', default=[])

    def init(self):
        self._pv_prop_funcs = []
        self._initialized = True
        return self

    def handlerFunctionClosure(self, name):
        def handlerFunction(*args, **kwargs):
            if not self._initialized:
                raise ValueError, "panel not initialized.  call .init() first"
            if kwargs:
                raise ValueError, "keyword arguments are disallowed"
            f = twc.JSSymbol(src=".%s(%s)" % (name, encoder.encode(args)[1:-1]))
            if f not in self._pv_prop_funcs:
                self._pv_prop_funcs.append(f)
            return self
        return handlerFunction

    def __getattr__(self, name):
        return self.handlerFunctionClosure(name)

# A convenience class to make writing visualizations easier
class PVObjects(object):
    Label = twc.JSSymbol(src='pv.Label')
    Bar = twc.JSSymbol(src='pv.Bar')
    Rule = twc.JSSymbol(src='pv.Rule')

pv = PVObjects()

