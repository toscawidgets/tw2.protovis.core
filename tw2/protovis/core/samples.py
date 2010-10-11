""" Samples of how to use tw2.protovis.core

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PVWidget, pv
from tw2.core import JSSymbol

class js(JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)


class DemoPVWidget(PVWidget):
    def __init__(self, *args, **kwargs):
        super(DemoPVWidget, self).__init__(*args, **kwargs)
        data = [1, 1.2, 1.7, 1.5, .7, .3]
        # Sizing and scales.
        self.init_js = js(
            """
            var data = %s,
                w = %i,
                h = %i,
                x = pv.Scale.linear(0, 1,1).range(0, w),
                y = pv.Scale.ordinal(pv.range(10)).splitBanded(0, h, 4/5);
            """ % (data, self.p_width, self.p_height))

        self.setupRootPanel()

        # The bars.
        bar = self.add(pv.Bar).data(js('data'))\
                .top(js('function() y(this.index)'))\
                .height(js('y.range().band'))\
                .left(0)\
                .width(js('x'))

        # The value label.
        bar.anchor("right").add(pv.Label)\
                .textStyle("white")\
                .text(js('function(d) d.toFixed(1)'))

        # The variable label.
        bar.anchor("left").add(pv.Label)\
            .textMargin(5)\
            .textAlign("right")\
            .text(js('function() "ABCDEFGHIJK".charAt(this.index)'))

        # X-axis ticks.
        self.add(pv.Rule)\
            .data(js('x.ticks(5)'))\
            .left(js('x'))\
            .strokeStyle(js('function(d) d ? "rgba(255,255,255,.3)" : "#000"'))\
          .add(pv.Rule)\
            .bottom(0)\
            .height(5)\
            .strokeStyle("#000")\
          .anchor("bottom").add(pv.Label)\
            .text(js('x.tickFormat'))

