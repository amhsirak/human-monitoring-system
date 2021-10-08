from scipy.spatial import distance as dist
from collections import OrderedDict
import numpy as np

class CentroidTracker():
    def __init__(self,maxDisappeared=50):
        # initialize next unique object ID along with 2 
        # ordered dicts to keep track of mapping
        # a given object ID to its centroid and no. of 
        # consecutive frames it has been marked as
        # "disapeared" respectively
        self.nextObjectID = 0
        self.objects = OrderedDict()
        self.disappeared = OrderedDict()