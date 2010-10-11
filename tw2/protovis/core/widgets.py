"""
TODO
"""

import tw2.core as twc
from tw2.core.resources import encoder
from tw2.protovis.core import resources as res
from tw2.protovis.core import pvobjects as pvo
import uuid

pv = pvo.PVObjects()

class PVMark(twc.Widget):
    template = "mako:tw2.protovis.core.templates.mark"
    resources = [res.pv_js]

    _initialized = twc.Variable('(bool)', default=False)
    _pv_prop_funcs = twc.Variable('(list) of JSSymbols', default=[])
    _adds = twc.Variable(default=[])
    pvcls = twc.Param()
    parent_js_id = twc.Variable(default=None)
    js_id = twc.Variable(default=None)
    add_method = twc.Variable(default=None)

    def init(self):
        self._pv_prop_funcs = []
        self._initialized = True
        self._adds = []
        return self

    def setupRootPanel(self):
        """ setup root panel... typically done at the start of .prepare """
        self.init().width(self.p_width).height(self.p_height) \
                   .bottom(self.p_bottom).top(self.p_top) \
                   .left(self.p_left).right(self.p_right)

    def hFuncClosure(self, name):
        class NameExtensionWrapper(PVMark):
            mrk, pre = twc.Variable(), twc.Variable()
            def __getattr__(self, name):
                return self.mrk.hFuncClosure('%s.%s' % (self.pre, name))

        # Special exceptions.  These aren't protovis methods.  Just properties
        if name in ['label', 'layer', 'link', 'node', '_parent']:
            if name in ['_parent']:
                name = name[1:]
            return NameExtensionWrapper(mrk=self, pre=name).req().init()

        def handlerFunction(*args, **kwargs):
            if not self._initialized:
                raise ValueError, "panel not initialized.  call .init() first"
            if kwargs:
                raise ValueError, "keyword arguments are disallowed"

            if name.endswith('add'):
                js_id = "%s_%s" % (
                    args[0].src.replace('.',''),
                    str(uuid.uuid4()).replace('-','')
                )
                m = PVMark(
                    pvcls=args[0],
                    js_id=js_id,
                    parent_js_id=self.js_id,
                    add_method=name,
                ).req().init()
                self._adds.append(m)
                return m

            src=".%s(%s)" % (name, encoder.encode(args)[1:-1])

            if name.endswith('anchor'):
                return NameExtensionWrapper(mrk=self, pre=src[1:]).req().init()
               
            f = twc.JSSymbol(src=src)
            if f not in self._pv_prop_funcs:
                self._pv_prop_funcs.append(f)
            
            return self

        return handlerFunction

    def __getattr__(self, name):
        return self.hFuncClosure(name)

class PVWidget(PVMark):
    template = "mako:tw2.protovis.core.templates.widget"

    p_data = twc.Param('(list) data for the widget')
    p_width = twc.Param('The width of the panel, in pixel.', default=400)
    p_height = twc.Param('The height of the panel, in pixels.', default=200)
    p_bottom = twc.Param('The bottom margin, in pixels.', default=20)
    p_top = twc.Param('The top margin, in pixels.', default=5)
    p_left = twc.Param('The left margin, in pixels.', default=20)
    p_right = twc.Param('The right margin, in pixels.', default=10)

    init_js = twc.Param('JSSymbol', default=twc.JSSymbol(src=''))
    pvcls = pv.Panel
    parent_js_id = None
    js_id = 'vis'
    add_method = 'add'
