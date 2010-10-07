
import tw2.core as twc
from tw2.protovis.core.defaults import __basename__, __version__
modname = ".".join(__name__.split('.')[:-1])

pv_js = twc.JSLink(
    modname=modname, filename='static/%s/%s/protovis.js' % (
        __basename__, __version__))

