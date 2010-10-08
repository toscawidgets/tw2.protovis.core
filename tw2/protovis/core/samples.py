""" Samples of how to use tw2.jit

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PVPanel, pv
from tw2.core import JSSymbol

class DemoPVPanel(PVPanel):
    def __init__(self, *args, **kwargs):
        super(DemoPVPanel, self).__init__(*args, **kwargs)
        self.init().height(150).width(175) \
            .add(pv.Rule) \
            .data(map(lambda x : x/2.0, range(4))) \
            .bottom(JSSymbol(src='function(d) { return d * 80 + .5 }')) \
            .add(pv.Label) \
            .add(pv.Bar) \
            .data([1, 1.2, 1.7, 1.5, .7, .3]) \
            .width(20) \
            .height(JSSymbol(src='function(d) { return d * 80 }')) \
            .bottom(0) \
            .left(JSSymbol(src='function(d) { return this.index * 25 + 25 }'))
