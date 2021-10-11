from scipy.spatial import distance as dist
import numpy as np

class CentroidTracker():
    def __init__(self,maxDisappeared=50, maxDistance=50):
        # initialize next unique object ID along with 2 ordered dicts to
        # 1. Keep track of mapping a given object ID to its centroid (key: ObjectID, value: centroid co-ordinates)
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
                # has been marked as missing, deregister it
                if self.disappeared[objectID] > self.maxDisappeared:
                    self.deregister(objectID)
            # return early as there are no centroids or tracking information to update
            return self.objects
        
        # initialize an array of input centroids for the current frame
        inputCentroids = np.zeros((len(rects),2), dtype='int')

        # loop over the bounding box rectangles
        for(i,(startX, startY, endX, endY)) in enumerate(rects):
            # use the bounding box coordinates to derive the centroid
            cX = int((startX + endX) / 2.0)
            cY = int((startY + endY) / 2.0)
            inputCentroids[i] = (cX, cY)

        # if not tracking any objects then take the input centroids and register each of them
        if len(self.objects) == 0:
            for i in range(0, len(inputCentroids)):
                self.register(inputCentroids[i])

        # if we are currently tracking objects then we need to
		# try to match the input centroids to existing object centroids
        else:
            # grab the set of object IDs and corresponding centroids
            objectIDs = list(self.objects.keys())
            objectCentroids = list(self.objects.value())

            # compute the distance between each pair of object centroids and input centroids resp.
            # our goal will be to match an input centroid to an existing object centroid
            D = dist.cdist(np.array(objectCentroids), inputCentroids)

            # in order to perform this matching we must:
            # 1. Find the smallest value in each row and 
            # 2. Sort the row indexes based on their minimum values so that 
            # the row with the msallest value is at the *front* of the index list
            rows = D.min(axis=1).argsort()

            # then we perform a similar process on the columns by finding the smallest value in each column and 
            # then sorting using the previously computed row index list
            cols = D.argmin(axis=1)[rows]

            # in order to determine if we need to update, register or deregister an object
            # we need to keep a track of which of the rows and cols indexes have already been examined
            usedRows = set()
            usedCols = set()

            # loop over the combination of (row,col) index tuples
            for (row,col) in zip(rows,cols):
                # if we have already examined either the row or the col value before, ignore it
                # val
                if row in usedRows or col in usedCols:
                    continue
                
                # if the distance between the centroids is greater than max distance
                # do not associate the two centroids to the same object
                if D[row,col] > self.maxDistance:
                    continue

                # otherwise grab the object ID for the current row, set its new centroids
                # and reset the disappeared counter
                objectID = objectIDs[row]
                self.objects[objectID] = inputCentroids[col]
                self.disappeared[objectID] = 0

                # indicate that we have examined each of the rows and cols indexes
                usedRows.add(row)
                usedCols.add(col)

            # compute both the row and column index we have NOT yet examined
            unusedRows = set(range(0, D.shape[0])).difference(usedRows)
            unusedCols = set(range(0, D.shape[1])).difference(usedCols)

            # in the event that the number of object centroids is
			# equal or greater than the number of input centroids
			# we need to check and see if some of these objects have
			# potentially disappeared
            if D.shape[0] >= D.shape[1]:
				# loop over the unused row indexes
                for row in unusedRows:
					# grab the object ID for the corresponding row
					# index and increment the disappeared counter
                    objectID = objectIDs[row]
                    self.disappeared[objectID] += 1

					# check to see if the number of consecutive
					# frames the object has been marked "disappeared"
					# for warrants deregistering the object
                    if self.disappeared[objectID] > self.maxDisappeared:
                        self.deregister(objectID)

			# otherwise, if the number of input centroids is greater
			# than the number of existing object centroids we need to
			# register each new input centroid as a trackable object
            else:
                for col in unusedCols:
                    self.register(inputCentroids[col])

		# return the set of trackable objects
		return self.objects
            