import cv2
# give the video that you want to reverse
cap = cv2.VideoCapture("videoinverse.mp4")

# properties of video
frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
hieght = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)
# initializing the output of the video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter("revesed.avi",fourcc,fps,(int(hieght*.5),int(width*.5)))

frame_index = frames - 1

if (cap.isOpened()):
    
    while(frame_index != 0):
        # set last frame to read first
        cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
        ret, frame = cap.read()
        
        frame = cv2.resize(frame, (int(hieght*.5),int(width*.5)))
        if ret == True:
            out.write(frame)
        frame_index = frame_index-1
        
out.release()
cap.release()