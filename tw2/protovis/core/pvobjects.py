
import tw2.core as twc

# A convenience class to make writing visualizations easier
class PVObjects(object):
    """ Represents an anchor on a given mark. """
    Anchor = twc.JSSymbol(src='pv.Anchor')

    """ Represents an area mark: the solid area between two
    series of connected line segments."""
    Area = twc.JSSymbol(src='pv.Area')

    """ Represents a bar: an axis-aligned rectangle that can be
    stroked and filled. """
    Bar = twc.JSSymbol(src='pv.Bar')

    class Behavior(twc.JSSymbol):
        """ Represents a reusable interaction; applies an interactive
        behavior to a given mark. """
        src='pv.Behavior'

        """ Implements interactive dragging starting with mousedown events. """
        drag = twc.JSSymbol(src='pv.Behavior.drag')

        """ Implements interactive panning starting with mousedown events. """
        pan = twc.JSSymbol(src='pv.Behavior.pan')

        """ Implements interactive fuzzy pointing, identifying marks that
        are in close proximity to the mouse cursor. """
        point = twc.JSSymbol(src='pv.Behavior.point')

        """ Implements interactive resizing of a selection starting with
        mousedown events. """
        resize = twc.JSSymbol(src='pv.Behavior.resize')

        """ Implements interactive selecting starting with mousedown events."""
        select = twc.JSSymbol(src='pv.Behavior.select')

        """ Implements interactive zooming using mousewheel events. """
        zoom = twc.JSSymbol(src='pv.Behavior.zoom')

    class Color(twc.JSSymbol):
        """ Represents an abstract (possibly translucent) color. """
        src='pv.Color'

        """ Represents a color in HSL space. """
        Hsl = twc.JSSymbol(src='pv.Color.Hsl')

        """ Represents a color in RGB space. """
        Rgb = twc.JSSymbol(src='pv.Color.Rgb')

    """ A collection of standard color palettes for categorical encoding. """
    Colors = twc.JSSymbol(src='pv.Colors')

    class Constraint(twc.JSSymbol):
        """ Represents a constraint that acts on particles. """
        src='pv.Constraint'

        """ Constrains particles to within fixed rectangular bounds. """
        bound = twc.JSSymbol(src='pv.Constraint.bound')

        """ Constraints circles to avoid overlap. """
        collision = twc.JSSymbol(src='pv.Constraint.collision')

        """ Constraints particles to a fixed position. """
        position = twc.JSSymbol(src='pv.Constraint.position')

    class Dom(twc.JSSymbol):
        """ Represets a DOM operator for the specified map. """
        src='pv.Dom'

        """ Represents a Node in the W3C Document Object Model. """
        Node = twc.JSSymbol(src='pv.Dom.Node')

    """ Represents a dot; a dot is simply a sized glyph centered at a
    given point that can also be stroked and filled. """
    Dot = twc.JSSymbol(src='pv.Dot')

    """ Represents a flatten operator for the specified array. """
    Flatten = twc.JSSymbol(src='pv.Flatten')

    class Force(twc.JSSymbol):
        """ Represents a force that acts on particles. """
        src='pv.Force'

        """ An n-body force, as defined by Coulomb's law or Newton's
        law of gravitation, inversely proportional to the square of
        the distance between particles. """
        charge = twc.JSSymbol(src='pv.Force.charge')

        """ Implements a drag force, simulating friction. """
        drag = twc.JSSymbol(src='pv.Force.drag')

        """ Implements a spring force, per Hooke's law. """
        spring = twc.JSSymbol(src='pv.Force.spring')

    class Format(twc.JSSymbol):
        """ Represents an abstract text formatter and parser. """
        src='pv.Format'

        """ The format string is in the same format expected by the
        strftime function in C. """
        date = twc.JSSymbol(src='pv.Format.date')

        """ Represents a number format, converting between a number
        and a string. """
        number = twc.JSSymbol(src='pv.Format.number')

        """ Represents a time format, converting between a number
        representing a duration in milliseconds, and a string. """
        time = twc.JSSymbol(src='pv.Format.time')

    class Geo(object):
        """ Represents a pair of geographic coordinates. """
        LatLng = twc.JSSymbol(src='pv.Geo.LatLng')

        """ Represents a geographic projection. """
        Projection = twc.JSSymbol(src='pv.Geo.Projection')

        projections = twc.JSSymbol(src='pv.Geo.projections')

        """ Represents a geographic scale; a mapping between
        latitude-longitude coordinates and screen pixel coordinates. """
        scale = twc.JSSymbol(src='pv.Geo.scale')

        """ Tick functions for geographic scales. """
        scaleticks = twc.JSSymbol(src='pv.Geo.scale#ticks')

    class histogram(twc.JSSymbol):
        """ Represents a histogram operator. """
        src='pv.histogram'

        """ Represents a bin returned by the pv.histogram operator. """
        Bin = twc.JSSymbol(src='pv.histogram.Bin')

    """ Represents an image, either a static resource or a dynamically-
    generated pixel buffer. """
    Image = twc.JSSymbol(src='pv.Image')

    """ Represents a text label, allowing textual annotation of
    other marks or arbitrary text within the visualization. """
    Label = twc.JSSymbol(src='pv.Label')

    class Layout(twc.JSSymbol):
        """ Represents an abstract layout, encapsulating a visualization
        technique such as a streamgraph or treemap. """
        src='pv.Layout'

        """ Implements a layout for arc diagrams. """
        Arc = twc.JSSymbol(src='pv.Layout.Arc')

        Bullet = twc.JSSymbol(src='pv.Layout.Bullet')

        """ Implements a hierarchical layout using the cluster
        (or dendrogram) algorithm. """
        Cluster = twc.JSSymbol(src='pv.Layout.Cluster')

        """ A variant of cluster layout that is space-filling. """
        Cluster.Fill = twc.JSSymbol(src='pv.Layout.Cluster.Fill')

        """ Implements force-directed network layout as a node-link diagram. """
        Force = twc.JSSymbol(src='pv.Layout.Force')

        """ Implements a grid layout with regularly-sized rows and columns. """
        Grid = twc.JSSymbol(src='pv.Layout.Grid')

        """ Represents an abstract layout for hierarchy diagrams. """
        Hierarchy = twc.JSSymbol(src='pv.Layout.Hierarchy')

        """ Implements a horizon layout, which is a variation of a
        single-series area chart where the area is folded into multiple
        bands. """
        Horizon = twc.JSSymbol(src='pv.Layout.Horizon')

        """ Implements a hierarchical layout using the indent algorithm. """
        Indent = twc.JSSymbol(src='pv.Layout.Indent')

        """ Implements a network visualization using a matrix view. """
        Matrix = twc.JSSymbol(src='pv.Layout.Matrix')

        """ Represents an abstract layout for network diagrams. """
        Network = twc.JSSymbol(src='pv.Layout.Network')

        """ Represents a link in a network layout. """
        Network.Link = twc.JSSymbol(src='pv.Layout.Network.Link')

        """ Represents a node in a network layout. """
        Network.Node = twc.JSSymbol(src='pv.Layout.Network.Node')

        """ Implements a hierarchical layout using circle-packing. """
        Pack = twc.JSSymbol(src='pv.Layout.Pack')

        """ Implemeents a hierarchical layout using the partition
        (or sunburst, icicle) algorithm. """
        Partition = twc.JSSymbol(src='pv.Layout.Partition')

        """ A variant of partition layout that is space-filling. """
        Partition.Fill = twc.JSSymbol(src='pv.Layout.Partition.Fill')

        """ Implements a network visualization using a node-link diagram
        where nodes are rolled up along two dimensions. """
        Rollup = twc.JSSymbol(src='pv.Layout.Rollup')

        """ Implements a layout for stacked visualizations, ranging
        from simple stacked bar charts to more elaborate "streamgraphs"
        composed of stacked areas. """
        Stack = twc.JSSymbol(src='pv.Layout.Stack')

        """ Implements a node-link tree diagram using the
        Reingold-Tilford "tidy" tree layout algorithm. """
        Tree = twc.JSSymbol(src='pv.Layout.Tree')

        """ Implements a space-filling rectangular layout, with the
        hierarchy represented via containment. """
        Treemap = twc.JSSymbol(src='pv.Layout.Treemap')

    """ Represents a series of connected line segments, or polyline,
    that can be stroked with a configurable color and thickness. """
    Line = twc.JSSymbol(src='pv.Line')

    """ Represents a data-driven graphical mark. """
    Mark = twc.JSSymbol(src='pv.Mark')

    """ Represents a Nest operator for the specified array. """
    Nest = twc.JSSymbol(src='pv.Nest')

    """ Represents a container mark. """
    Panel = twc.JSSymbol(src='pv.Panel')

    """ A weighted particle that can participate in a force simulation. """
    Particle = twc.JSSymbol(src='pv.Particle')

    class Quadtree(twc.JSSymbol):
        """ Represents a quadtree: a two-dimensional recursive
        spatial subdivision. """
        src='pv.Quadtree'

        """ A node in a quadtree. """
        Node = twc.JSSymbol(src='pv.Quadtree.Node')

    """ Represents a horizontal or vertical rule. """
    Rule = twc.JSSymbol(src='pv.Rule')

    class Scale(twc.JSSymbol):
        """ Represents a scale; a function that performs a transformation
        from data domain to visual range. """
        src='pv.Scale'

        """ Represents a linear scale; a function that
        performs a linear transformation. """
        linear = twc.JSSymbol(src='pv.Scale.linear')

        """ Represents a log scale. """
        log = twc.JSSymbol(src='pv.Scale.log')

        """ Represents an ordinal scale. """
        ordinal = twc.JSSymbol(src='pv.Scale.ordinal')

        """ Represents a quantile scale; a function that maps
        from a value within a sortable domain to a quantized
        numeric range. """
        quantile = twc.JSSymbol(src='pv.Scale.quantile')

        """ Represents an abstract quantitative scale; a function
        that performs a numeric transformation. """
        quantitative = twc.JSSymbol(src='pv.Scale.quantitative')

        """ Represents a root scale; a function that
        performs a power transformation. """
        root = twc.JSSymbol(src='pv.Scale.root')

    """ Represents a particle simulation. """
    Simulation = twc.JSSymbol(src='pv.Simulation')

    """ Represents a transformation matrix. """
    Transform = twc.JSSymbol(src='pv.Transform')

    """ Represents a tree operator for the specified array. """
    Tree = twc.JSSymbol(src='pv.Tree')

    """ Represents a two-dimensional vector; a 2-tuple (x, y). """
    Vector = twc.JSSymbol(src='pv.Vector')

    """ Protovis major and minor version numbers. """
    version = twc.JSSymbol(src='pv.version')

    """ Represents a wedge, or pie slice. """
    Wedge = twc.JSSymbol(src='pv.Wedge')
