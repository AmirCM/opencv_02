import cv2 as cv

cap = cv.VideoCapture(0)  # 0 is camera index
if not cap.isOpened():
    print('Error during opening camera!!!\n')
    exit()
cv.namedWindow('Video', cv.WINDOW_AUTOSIZE)
i = 0
while True:
    start = cv.getTickCount()
    ret, frame = cap.read()

    if not ret:  # if frame is read correctly ret is True
        print("Can't receive frame (stream end?). Exiting ...")
        break
    cv.imshow('Video', frame)

    k = cv.waitKey(1)

    if k == ord('q'):  # press q for quite
        break
    elif k == ord('s'):  # press s for save image
        cv.imwrite('screen_' + str(i) + '.jpg', frame)
        i += 1
    end = cv.getTickCount()
    time = (end - start)/cv.getTickFrequency()
    print(f'FPS: {1/time}')
cap.release()
cv.destroyAllWindows()
