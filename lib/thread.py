import cv2, threading, queue

class Threading:
    def __init__(self,src):
        self.cap = cv2.VideoCapture(src)
        # defining empty queue and thread
        self.q = queue.Queue()
        thread = threading.Thread(target = self._reader)
        thread.daemon = True
        thread.start()

        # read the frames as soon as they are available
        # Threading helps to remove OpenCV's internal buffer and reduces the frame lag
        def _reader(self):
            while True:
                # read the frames
                ret, frame = self.cap.read() 
                if not ret:
                    break
                if not self.q.empty():
                    try:
                        self.q.get_nowait()
                    except queue.Empty:
                        pass
                # store the frames in a queue instead of the buffer
                self.q.put(frame) 

        def read(self):
            # fetch frames from the queue one by one
            return self.q.get() 

        def release(self):
            # release hw resource
            return self.cap.release()
        