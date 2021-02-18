import cv2
import os
import time #to give us time between recognition
import uuid

#IDEA: MAKE MUSIC HAND SIGN

image_source = 'images\\rec_images'


labels = ['stop', 'forward', 'forward_left', 'forward_right', 'fast_forward', 'fast_forward_left', 'fast_forward_right', 'reverse']

no_image = 40


for item in labels:
    os.mkdir(image_source+"\\"+item)
    cap = cv2.VideoCapture(0) #WEBCAM (access)
    print('Collecting {}'.format(item))
    time.sleep(3)

    for imgnum in range(no_image):
        ret, frame = cap.read()
        img_name = os.path.join(image_source, item, item + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            #individual unique name ensured

        cv2.imwrite(img_name, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break #CHECK

    cap.release()

    
