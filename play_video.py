########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json, cv2
import cv2
import os
import keyboard
import time
#multiprocessing import Process ???





def playvideo():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)

    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    img_counter = 1
    timer = 0
    processed = 0

    while rval:
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        img_name = "img_frame{}.jpg".format(img_counter)
        # print("Created img_frame{}.jpg".format(img_counter))
        key = cv2.waitKey(25) # milliseconds # 1000/25 = 40 FPS
        print("timer",timer)
        if timer % 40 == 0:
            print('Tip :  {}'.format(4-(timer / 40)), end='\r')

        # start processing the image emotions when timer is in multiple of 4
        if timer / 40 == 4 :
            cv2.imwrite(img_name, frame)
            processed+=1

            # function call to process image
            # find_emotion(img_name)

            key = cv2.waitKey(50) # milliseconds
            timer=1
            if os.path.isfile(img_name):
                os.remove(img_name)
                continue
                # deleting the image after processing it
                print("Deleted img_frame{}.jpg".format(i))
            else: ## Show an error ##
                print("Error: %s file not found" % myfile)
                continue
        timer+=1

        # take less frames
        # end processing this frame
        img_counter += 1

        if key == 27 or processed == 18:  # exit on ESC
            break

    cv2.destroyWindow("preview")
    # print('API calls made or number frames processed for emotion detection : {}'.format(processed))
    vc.release()

    #print("\n\n\tAll images deleted. Memory freed. Enjoy Lappy. ;)")

def printit():
    # run your code
    print('Time :  ', end='\r')
    end = time.time()
    elapsed = int(end - start)
    print('Time :  {}'.format(elapsed), end='\r')




if __name__ == '__main__':
    start = time.time()
    # printit()
    # find_emotions()
    playvideo()