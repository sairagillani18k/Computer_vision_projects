import cv2
print("###########################################################")
###################################################################################
# image read
image = cv2.imread("smape.png")
if image.any():   
    cv2.imshow("sample read",image)
cv2.waitKey(0)

# write the image
cv2.imwrite("sample.jpg",image)
###########################################################################################
print("########################################################################################")
#############################################################################################
# read video from camera
# capture video from defult camera argument is zero
# instance of video capture
video = cv2.VideoCapture(0)
opened = video.isOpened()

if(opened):
    # break loop when esc pressed its assci value is 27
    while video.isOpened():
        #ret is return boolean it show camera capture the frame or not
        ret,frame = video.read()
        if(ret == True):
            cv2.imshow("video",frame)
            if(cv2.waitKey(2) == 27):
                break
##################################################################################
print("########################################################################")
####################################################################################
# Video write
cap = cv2.VideoCapture(0)
opened = cap.isOpened()

# get properties of video that captured
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
fps = cap.get(cv2.CAP_PROP_FPS)


# fourcc coding schame : write and read compressed video
fourcc = cv2.VideoWriter_fourcc(*'MJPG')

# video writer
out = cv2.VideoWriter('sample.avi',fourcc,fps,(int(height),int(width)))
if(opened):
    while(cap.isOpened):
        ret,frame = cap.read()
        if(ret == True):
            out.write(frame)
            cv2.imshow("video",frame)
            if cv2.waitKey(2) == 27:
                break
            
out.release()
cap.release()
cv2.destroyAllWindows()