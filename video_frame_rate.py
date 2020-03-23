import cv2 as cv
import time
from queue import Queue
from threading import Thread


class FileVideoStream:
    def __init__(self, path, queueSize=128):
        self.stream = cv.VideoCapture(path)
        self.stopped = False
        # initialize the queue used to store frames read from
        # the video file
        self.Q = Queue(maxsize=queueSize)

    def start(self):
        # start a thread to read frames from the file video stream
        t = Thread(target=self.update, args=())
        t.daemon = True
        t.start()
        return self

    def update(self):
        while True:
            if self.stopped:
                return

            if not self.Q.full():
                # read the next frame from the file
                grabbed, fr = self.stream.read()
                self.Q.put(fr)

    def read(self):
        return self.Q.get()

    def stop(self):
        self.stopped = True


cv.namedWindow('Video', cv.WINDOW_AUTOSIZE)
video = FileVideoStream(0).start()

while True:
    start_time = time.time()
    frame = video.read()
    cv.imshow('Video', frame)

    k = cv.waitKey(1)
    if k == ord('q'):  # press q for quite
        break
    print(f"FPS: {1//(time.time() - start_time)}")
cv.destroyAllWindows()
