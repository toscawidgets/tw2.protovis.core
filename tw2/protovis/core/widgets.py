"""
TODO
"""

import tw2.core as twc
from tw2.protovis.core import resources as res

class PVPanel(twc.Widget):
    template = "genshi:tw2.protovis.core.templates.panel"
    resources = [res.pv_js]
   
    width = twc.Param('(string) widget width', default='150', attribute=True)
    height = twc.Param('(string) widget height', default='150', attribute=True)

