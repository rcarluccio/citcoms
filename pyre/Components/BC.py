#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

from pyre.components.Component import Component

class BC(Component):


    def __init__(self):
        Component.__init__(self, "bc", "bc")
        return



    def setProperties(self):
        import CitcomS.Regional as Regional
	Regional.BC_set_properties(self.inventory)
        return



    class Inventory(Component.Inventory):

        import pyre.properties


        inventory = [

            pyre.properties.bool("topvbc",False),
            pyre.properties.float("topvbxval",0.0),
            pyre.properties.float("topvbyval",0.0),

            pyre.properties.bool("botvbc",False),
            pyre.properties.float("botvbxval",0.0),
            pyre.properties.float("botvbyval",0.0),

            pyre.properties.bool("toptbc",False),
            pyre.properties.float("toptbcval",0.0),

            pyre.properties.bool("bottbc",False),
            pyre.properties.float("bottbcval",0.0),


	    # these parameters are for 'lith_age',
	    # put them here temporalily
            pyre.properties.bool("temperature_bound_adj",False),
            pyre.properties.float("depth_bound_adj",0.157),
            pyre.properties.float("width_bound_adj",0.08727)

            ]

# version
__id__ = "$Id: BC.py,v 1.4 2003/07/23 05:29:58 ces74 Exp $"

# End of file
