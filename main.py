from lib.centroidtracker import CentroidTracker
from lib.trackableobject import TrackableObject
from lib import config
from imutils.video import VideoStream
from imutils.video import FPS
import argparse, imutils
import time, schedule, csv
import time, dlib, cv2, datetime
from itertools import zip_longest
import numpy as np

t0 = time.time()

def run():
    ap = argparse.ArgumentParser()
    ap.add_argument('-p', 'prototxt', required=True, help='Path to Caffe deploy prototxt file')
    ap.add_argument('-m', '--model', required=True, help='Path to Caffe pre-trained model')
    ap.add_argument('-i', '--input', type=str, help='Path to optional input video file')
    ap.add_argument('-o', '--ouput', type=str, help='Path to optional output video file')
    ap.add_argument('-c', '--confidence', type=float, default=0.4, help='Minimum probability to filter weak detections')
    ap.add_argument('-s', '--skip-frames', type=int, default=30, help='# of skip frames between detections')
    args = vars(ap.parse_args())

    # classes the model was trained to detect
    CLASSES = ['background', 'aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep','sofa', 'train', 'tvmonitor']

    # load our serialized model from disk
    print('[INFO] loading model...')
    net = cv2.dnn.readNetFromCaffe(args['prototxt'], args['model'])

    # if video path is not supplied, use IP/Webcam
    if not args.get('input', False):
        print('[INFO] STarting the live stream...')
        vs = VideoStream(config.url).start()
        time.sleep(2.0)
    else:
        print('[INFO] Starting the video...')
        vs = cv2.VideoCapture(args['input'])
    
    # initialise the video writer
    writer = None

    # initialize the frame dimensions (we'll set them as soon as we read
	# the first frame from the video)
    W = None
    H = None 

    # instantiate our centroid tracker, then initialise a list 
    # to store each of our dlib correlation trackers, and a dict to
    # map each unique object ID to a TrackableObject
    ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
    trackers = []
    trackableObjects = {}

    # initialise the total number of frames processed thus far, along with 
    # the total no. of objects that have moved either up or down
    totalFrames = 0
    totalDown = 0
    totalUp = 0
    x = []
    empty = []
    empty1 = []

    # start the frames per second throughput estimator
    fps = FPS().start()

    # loop over incoming frames from the video stream
    while True:
        # grab the next frame and handle if we are reading from
        # either VideoCapture or VideoStream
        frame = vs.read()
        frame = frame[1] if args.get('input', False) else frame

        # if we are viewing a video and we did not grab a frame
        # then we have reached end of the video
        if args['input'] is not None and frame is None: 
            break

        # resize the frame to have a max width of 500px(the less 
        # data we have, the faster we can process it), then
        # convert the frame from BGR to RGB for dlib
        frame = imutils.resize(frame,width=500)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # if the frame dimensions are empty, set them
        if W is None or H is None:
            (H, W) = frame.shape[:2]

        # if we are supposed to be writing a video to disk, initialize the writer
        if args['output'] is not None and writer is None:
            fourcc = cv2.VideoWriter_fourcc(*'MJPG')
            writer = cv2.VideoWriter(args['output'], fourcc, 30, (W,H), True)

        # initialize the current status along with our list of bounding box rects returned by either
        # 1. Our object detector or 2. Correlation trackers
        status = 'Waiting'
        rects = []

        # check to see if we should run a more computionally expensive
        # object detection method to aid our tracker
        if totalFrames % args['skip_frames'] == 0:
            # set the status and initialize our new set of object trackers
            status = 'Detecting'
            trackers = []

            # convert the frame to a blob and pass the blob through the 
            # network and obtain the detections
            blob = cv2.dnn.blobFromImage(frame, 0.007843, (W,H), 127.5)
            net.setInput(blob)
            detections = net.foward()

        # loop over detections
        for i in np.arange(0, detections.shape[2]):
            # extract the confidence (probability) associated with the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections by requiring a min confidence
            if confidence > args['confidence']:
                # extract the index of the class label from the detections list
                idx = int(detections[0, 0, i, 1])

                # if the class label is not a person, ignore it 
                if CLASSES[idx] != 'person':
                    continue