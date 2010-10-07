""" Samples of how to use tw2.jit

Each class exposed in the widgets submodule has an accompanying Demo<class>
widget here with some parameters filled out.

The demos implemented here are what is displayed in the tw2.devtools
WidgetBrowser.
"""
from widgets import PVPanel
from tw2.core import JSSymbol

class DemoPVPanel(PVPanel):
    def prepare(self):
        super(DemoPVPanel, self).prepare()
        self.height(150)
        self.width(175)
        self.add(JSSymbol(src='pv.Rule'))
        self.data(JSSymbol(src='pv.range(0,2,.5)'))
        self.bottom(JSSymbol(src='function(d) { return d * 80 + .5 }'))
        self.add(JSSymbol(src='pv.Label'))

        self.add(JSSymbol(src='pv.Bar'))
        self.data([1, 1.2, 1.7, 1.5, .7, .3])
        self.width(20)
        self.height(JSSymbol(src='function(d) { return d * 80 }'))
        self.bottom(0)
        self.left(JSSymbol(src='function(d) { return this.index * 25 + 25 }'))
