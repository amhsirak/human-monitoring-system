class TrackableObject:
    def __init__(self, objectID, centroid):
        # store the object ID, then initialise a list of centroids
        # using the current centroid
        self.objectID = objectID
        self.centroids = [centroid]

        # initialise a boolean to indicate if the object
        # has been already counted or not
        self.counted = False