import cv2 as cv


def mouse_callback(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print(x, y)


events = [i for i in dir(cv) if 'EVENT' in i]
print(events)

cap = cv.VideoCapture(0)  # 1 is camera index
if not cap.isOpened():
    print('Error during opening camera!!!\n')
    exit()
cv.namedWindow('Video', cv.WINDOW_AUTOSIZE)
cv.setMouseCallback('Video', mouse_callback)
i = 0
while True:
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

cap.release()
cv.destroyAllWindows()
