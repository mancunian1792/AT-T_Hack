########### Python 3.6 #############
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json
import cv2
import os
import time


#global paramter
ans = {}
ans['answer'] = 'sad'

def face_emotion():
    emotion_recognition_url = "https://eastus.api.cognitive.microsoft.com/face/v1.0/detect?%s"
    headers = {
        # Request headers
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': '2fe46b07420145988dfe17fa53d95c06',
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'emotion',
    })

    try:
        with open("./img_frame161.jpg", "rb") as imageFile:
            image_data = imageFile.read()
            # body = bytearray(f)
        response = requests.post(emotion_recognition_url, headers=headers, data=image_data, params=params)
        parsed = json.loads(response.text)

        frame_num = 1
        sad_count = 0
        happy_count = 0
        for face in parsed:
            print(face['faceAttributes']['emotion'])
            result =  (face['faceAttributes']['emotion']['sadness'] + face['faceAttributes']['emotion']['neutral'] + face['faceAttributes']['emotion']['fear'] +
            face['faceAttributes']['emotion']['disgust'] + face['faceAttributes']['emotion']['contempt'] +
            face['faceAttributes']['emotion']['anger'])

            print('result', result)

            if result > face['faceAttributes']['emotion']['happiness']:
                sad_count+=1
            else:
                happy_count+=1


        if sad_count > happy_count:
            ans['answer'] = 'sad'
            ans['flag'] = True
            print('\t >> Don\'t be sad ? I am here to help. I \'ll change the song for you.')
        else:
            ans['answer'] ='happy'
            print('\t >> I think you like this artist.')
            #frame_num+=1

    except Exception as e:
        print(e)
        print("[Errno {0}] {1}".format(e.errno, e.strerror))



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
            print("image saved")
            exit(0)
            processed+=1

            # function call to process image
            # face_emotion(img_name)

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




if __name__ == '__main__':
    face_emotion()
    # playvideo()