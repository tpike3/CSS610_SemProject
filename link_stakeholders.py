##############################################################################
# Author: Christopher M. Parrett
# Homework #2, due 08FEB2017
# Computational Social Science 610: Agent Based Modeling and Simulation
# Spring 2017, Department of Computational and Data Sciences,
# Under the most excellent tutelage of Dr. R Axtell, George Mason Univ
#
# Developed on a Windows 10 platform, AMD PhenomII X6 3.3GHz w/ 8GB RAM
# using Python 3.5.2 | Anaconda 4.2.0 (64-bit).
##############################################################################
##############################################################################

from link import *
from entity import *

##############################################################################
##############################################################################
# CLASS::
#
# Purpose:
#
#
class LINK_STAKEHOLDERS(LINK):
    def __init__(self,orig,dest):
        LINK.__init__(orig,dest)
        self.s = Entity(0,0,0)
        self.scbo = Entity(0,0,0)
        self.sintereu = 0

        self.scboeu = (0,0)

    def setS(self,x,v): self.setEntity(x,v)
    def setScbo(self,x,v): self.setEntity(x,v)
    def setSintereu(self,x): self.sintereu = x

    def getS(self,x): return self.getEntity(x)
    def getScbo(self,x): return self.getEntity(x)
    def getSintereu(self): return self.sintereu

    def getScboeu(self,idx): return self.scboeu[idx]
    def setScboeu(self,idx,x): self.scboeu[idx] = x
