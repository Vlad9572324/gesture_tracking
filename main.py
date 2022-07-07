import cv2
import presskeyforgame
import numpy as np
import mediapipe as mp
import pyautogui, sys





mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_holistic = mp.solutions.holistic
xc=0
gfl=0
p = [0 for i in range(21)]              
p1 = [0 for i in range(21)]
joint_list = [[4, 3, 2],[7, 6, 5], [11, 10, 9], [15, 14, 13], [19, 18, 17]]  #Finger joint sequence
angles=[]
cap = cv2.VideoCapture(0)
with mp_holistic.Holistic(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as holistic:
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("Ignoring empty camera frame.")
            break
        if gfl==0:
            imageHeight, imageWidth, _ = image.shape
            imageHeight2=imageHeight/2
            imageWidth2=imageWidth/2
            print(imageHeight2,imageWidth2)
            gfl+=1

        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = holistic.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        #
        mp_drawing.draw_landmarks(
            image,
            results.face_landmarks,
            mp_holistic.FACEMESH_CONTOURS,
            landmark_drawing_spec=None,
            connection_drawing_spec=mp_drawing_styles
                .get_default_face_mesh_tesselation_style())
        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_holistic.POSE_CONNECTIONS, landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style())
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style())
        
        if results.right_hand_landmarks:


            
            RHL = results.right_hand_landmarks
            
            
            width, height = int(RHL.landmark[8].x * imageHeight), int(RHL.landmark[8].y* imageWidth)
           



            #print(width,height)
            xc=0
            for joint in joint_list:
                a = np.array([RHL.landmark[joint[0]].x, RHL.landmark[joint[0]].y])
                b = np.array([RHL.landmark[joint[1]].x, RHL.landmark[joint[1]].y])
                c = np.array([RHL.landmark[joint[2]].x, RHL.landmark[joint[2]].y])
                #                 # Calculate the radians
                radians_fingers = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
                angle = np.abs(radians_fingers * 180.0 / np.pi)  #
                xc+= 1
                #if xc==5:
                    #print(RHL.landmark)
                if angle > 180.0:

                    angle = 360 - angle

                cv2.putText(image, str(round(angle, 2)), tuple(np.multiply(b, [640, 480]).astype(int)),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                if xc==1:
                    if angle<120:
                        presskeyforgame.hold(17, 1) # ГАЗ "W"
                        
                   # else:
                        #mouse.release(Button.left)
                if xc == 2:
                    if angle<110:
                        presskeyforgame.hold(31, 1) # "S"

                if xc==3:
                    if angle<110:
                        presskeyforgame.hold(30, 1)#лево "A"
                if xc==5:
                    if angle<110:
                        presskeyforgame.hold(32, 1)#право "D"




        # cv2.imshow('MediaPipe Holistic', cv2.flip(image, 1))
        cv2.imshow('Mediapipe Holistic', image)  # Cancel the mirror flip
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
