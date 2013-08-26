""" Samples of how to use tw2.protovis.core

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PVWidget, pv
from tw2.core import JSSymbol

import random


class js(JSSymbol):
    def __init__(self, src):
        super(js, self).__init__(src=src)


class DemoPVWidget(PVWidget):
    def __init__(self, *args, **kwargs):
        self.p_data = [
        [random.random() + 0.1 for j in range(4)] for i in range(3)]
        super(DemoPVWidget, self).__init__(*args, **kwargs)
        # Sizing and scales.
        self.init_js = js(
            """
            var data = %s;
            var n = data.length;
            var m = data[0].length;
            var w = %i,
                h = %i,
                x = pv.Scale.linear(0, 1.1).range(0, w),
                y = pv.Scale.ordinal(pv.range(n)).splitBanded(0, h, 4/5);
            """ % (self.p_data, self.p_width, self.p_height))

        self.setupRootPanel()

        # The bars.
        bar = self.add(pv.Panel) \
            .data(js('data')) \
            .top(js('function() y(this.index)')) \
            .height(js('y.range().band')) \
          .add(pv.Bar) \
            .data(js('function(d) d')) \
            .top(js('function() this.index * y.range().band / m')) \
            .height(js('y.range().band / m')) \
            .left(0) \
            .width(js('x')) \
            .fillStyle(js('pv.Colors.category20().by(pv.index)'))

        # The value label.
        bar.anchor("right").add(pv.Label) \
            .textStyle("white") \
            .text(js('function(d) d.toFixed(1)'))

        # The variable label.
        bar._parent.anchor("left").add(pv.Label) \
            .textAlign("right") \
            .textMargin(5) \
            .text(js('function() "ABCDEFGHIJK".charAt(this.parent.index)'))

        # X-axis ticks.
        self.add(pv.Rule) \
            .data(js('x.ticks(5)')) \
            .left(js('x')) \
            .strokeStyle(
                js('function(d) d ? "rgba(255,255,255,.3)" : "#000"')
            )\
            .add(pv.Rule) \
            .bottom(0) \
            .height(5) \
            .strokeStyle("#000") \
          .anchor("bottom").add(pv.Label) \
            .text(js('x.tickFormat'))
