"""
TODO
"""

import tw2.core as twc
from tw2.core.resources import encoder
from tw2.protovis.core import resources as res
from tw2.protovis.core import pvobjects as pvo

pv = pvo.PVObjects()

class PVMark(twc.Widget):
    template = "mako:tw2.protovis.core.templates.mark"
    resources = [res.pv_js]

    _initialized = twc.Variable('(bool)', default=False)
    _pv_prop_funcs = twc.Variable('(list) of JSSymbols', default=[])
    pvcls = twc.Param()

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

class PVWidget(PVMark):
    template = "mako:tw2.protovis.core.templates.widget"
    resources = [res.pv_js]

    p_data = twc.Param('(list) data for the widget')
    p_width = twc.Param('The width of the panel, in pixel.', default=400)
    p_height = twc.Param('The height of the panel, in pixels.', default=200)
    p_bottom = twc.Param('The bottom margin, in pixels.', default=20)
    p_top = twc.Param('The top margin, in pixels.', default=5)
    p_left = twc.Param('The left margin, in pixels.', default=20)
    p_right = twc.Param('The right margin, in pixels.', default=10)

    init_js = twc.Param('JSSymbol', default=twc.JSSymbol(src=''))
    _adds = twc.Variable(default=[])
    pvcls = pv.Panel

    def init(self):
        self._adds = []
        return super(PVWidget, self).init()
    
    def handlerFunctionClosure(self, name):
        def handlerFunction(*args, **kwargs):
            if not self._initialized:
                raise ValueError, "panel not initialized.  call .init() first"
            if kwargs:
                raise ValueError, "keyword arguments are disallowed"
            
            if name == 'add':
                m = PVMark(pvcls=args[0]).req().init()
                self._adds.append(m)
                return m
  
            f = twc.JSSymbol(src=".%s(%s)" % (name, encoder.encode(args)[1:-1]))
            if f not in self._pv_prop_funcs:
                self._pv_prop_funcs.append(f)
            
            return self
        return handlerFunction

