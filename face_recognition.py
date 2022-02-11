import cv2
import os
import time
import sys
# Import numpy for matrices calculations
import numpy as np

# Create Local Binary Patterns Histograms for face recognization
#recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Load the trained mode
recognizer.read('trainer/trainer.yml')
##recognizer.read('/home/pi/Desktop/face_recog_folder/Raspberry-Face-Recognition-master/trainer/trainer.yml')

# Load prebuilt model for Frontal Face
cascadePath = "haarcascade_frontalface_default.xml"

# Create classifier from prebuilt model
faceCascade = cv2.CascadeClassifier(cascadePath);

# Set the font style
font = cv2.FONT_HERSHEY_SIMPLEX

# Initialize and start the video frame capture
cam = cv2.VideoCapture(0)

flag = []
count1=0
count2=0
count3=0
sample =0
lecture=0
mon=0
count=0


##account_sid = "AC4c80a8d4e94004afc637499ca50ddc59"
##auth_token = "d7008f6cd8700dd6fac792bc35f7bfa7"
##
##client = Client(account_sid, auth_token)



while True:

        # Read the video frame
        ret, im =cam.read()

        # Convert the captured frame into grayscale
        gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

        # Get all face from the video frame
        faces = faceCascade.detectMultiScale(gray, 1.2,5)

        # For each face in faces
        for(x,y,w,h) in faces:

            # Create rectangle around the face
            cv2.rectangle(im, (x-20,y-20), (x+w+20,y+h+20), (0,255,0), 4)

            # Recognize the face belongs to which ID
            Id,i = recognizer.predict(gray[y:y+h,x:x+w])
            #id = int(os.path.split(imagePath)[-1].split(".")[1])
            
            print(i)
            # Check the ID if exist
            if i < 70:
                sample= sample+1

                if Id == 1 :
                    #flag[1]=1
                    count1=1
                    Id = "nikitha"
                    print("nikitha")
                    lecture=1
                    sample=0
                    break
                
                if Id == 2 :
                    #flag[1]=1
                    count1=1
                    Id = "gunasri"
                    print("gunasri")
                    lecture=1
                    sample=0
                    break

                if Id == 3:
                    # flag[1]=1
                    count1 = 1
                    Id = "neelam"
                    print("neelam")
                    lecture = 1
                    sample = 0
                    break
                   

               
            else:
                count=count+1

                if count > 10:
                    count=0
                    print(Id)
                 
                    Id = "unknown"
                   
                    print('UNKNOWN PERSON')

                                     
            
            # Put text describe who is in the picture
            cv2.rectangle(im, (x-22,y-90), (x+w+22, y-22), (0,255,0), -1)
            cv2.putText(im, str(Id), (x,y-40), font, 2, (255,255,255), 3)

            # Display the video frame with the bounded rectangle
        cv2.imshow('im',im)


        # If 'q' is pressed, close program
        if cv2.waitKey(20) & 0xFF == ord('q'): #if cv2.waitKey(10) & 0xFF == ord('q'):
            break
           
cam.release()

# Close all windows
cv2.destroyAllWindows()
