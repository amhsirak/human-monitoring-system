from scipy.spatial import distance as dist
import numpy as np

class CentroidTracker():
    def __init__(self,maxDisappeared=50, maxDistance=50):
        # initialize next unique object ID along with 2 ordered dicts to
        # 1. Keep track of mapping a given object ID to its centroid(key:ObjectID,value:centroid co-ordinates)
        # 2. No. of consecutive frames a particular object ID (key) has been marked as “lost”
        self.nextObjectID = 0
        self.objects = {}
        self.disappeared = {}
        # the maximum no. of consecutive frames a given object has to be 
        # lost/disappeared for until we remove it from our tracker 
        self.maxDisappeared = maxDisappeared
        # store the maximum distance between centroids to associate an object
        # if distance is larger than max distance we'll start to mark the object as "disappeared"
        self.maxDistance = maxDistance

    def register(self,centroid):
        # when registering an object we use the next available object ID to store the centroid
        self.objects[self.nextObjectID] = centroid
        self.disappeared[self.nextObjectID] = 0
        self.nextObjectID += 1

    def deregister(self,objectID):
        # to deregister an object ID we delete the object ID from both our respective dicts
        del self.objects[objectID]
        del self.disappeared[objectID]

    def update(self,rects):
        # check to see if the list of input bounding box rectangles is empty
        if len(rects) == 0:
            # loop over any existing tracked objects and mark them as disappeared
            for objectID in list(self.disappeared.keys()):
                self.disappeared[objectID] += 1
                # if we have reached a maximum number of consecutive frames where a given object
                # has been as missing, deregister it
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)
            # return early as there are no centroids or tracking information to update
            return self.objects