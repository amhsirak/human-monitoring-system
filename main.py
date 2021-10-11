from lib.centroidtracker import CentroidTracker
from lib.trackableobject import TrackableObject
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
