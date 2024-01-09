# program to capture single image from webcam in python 

# importing OpenCV library 
import cv2 as cv

our_img_array=[None]*120
index=0;

cam = None
cam_port = 0

def init_cam(cp = 0):
    global cam
    # initialize the camera 
    # If you have multiple camera connected with 
    # current device, assign a value in cam_port 
    # variable according to that 
    cam_port = cp
    cam = cv.VideoCapture(cam_port) 


def capture():
    # reading the input using the camera 
    result, image = cam.read() 

    # If image will detected without any error, 
    # show result 
    if result: 
        # showing result, it take frame name and image 
        # output 
        #imshow("GeeksForGeeks", image) 

        # saving image in local storage 
        #imwrite("GeeksForGeeks.png", image) 

        # If keyboard interrupt occurs, destroy image 
        # window 
        #waitKey(0) 
        #destroyWindow("GeeksForGeeks") 
        return image

    # If captured image is corrupted, moving to else part 
    else: 
        print("No image detected. Please! try again") 
        return None

def test():
    init_cam(0)
    img = capture()
    if(img!=None):
        imshow("GeeksForGeeks", image) 

        # saving image in local storage 
        #imwrite("GeeksForGeeks.png", image) 

        # If keyboard interrupt occurs, destroy image 
        # window 
        waitKey(0) 
        destroyWindow("GeeksForGeeks") 
    

def main():
    test()
    
if __name__ == '__main__':
    main()