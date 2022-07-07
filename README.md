# Finger control
Tracking the movement of fingers through the angle between vectors
This script allows you to easily control the movement of the game unit by bending the fingers, commands (Thumb: Forward "W", Index finger: Back "S", Small finger: Right "D", Middle finger : Left "A")

<img width="772" alt="hand_landmarks" src="https://user-images.githubusercontent.com/101418967/177830425-8d65aefb-4373-4dd2-87a5-96cc954ce548.png">



Bending the thumb triggers the "W" button decreasing the angle less than 120 degrees (the angle is between points [4,3,2])

Bending the index finger triggers the "S" button, decreasing the angle less than 110 degrees (the angle is between the points [7,6,5])

Bending the middle finger triggers the "A" button, decreasing the angle less than 110 degrees (the angle is between points [11,10,9])

Bending the little finger triggers the "D" button, decreasing the angle less than 110 degrees (the angle is between points [19,18,17])
