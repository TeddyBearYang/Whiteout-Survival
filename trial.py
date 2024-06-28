# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:46:56 2024

@author: User
"""

import cv2
import numpy as np
import mss
import os
import mss.tools

# File path
os.chdir('D:\GitHub\Whiteout-Survival')

# Load the template image
template = cv2.imread('target_mission_3.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

# Define the screen capture region (adjust this to your game window's position and size)
# monitor = {'left': 850,
#         'top': 490,
#         'width': 195,
#         'height': 220
#         }

# Right box
monitor = {'left': 1015,
        'top': 490,
        'width': 195,
        'height': 220
        }

# Create an MSS instance
with mss.mss() as sct:
    while True:
        # Capture the screen
        screen = sct.grab(monitor)
        
        # Convert the screen to a NumPy array
        img = np.array(screen)
        
        # Convert the screen to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Perform template matching
        result = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
        
        # Set a threshold to identify matching regions
        threshold = 0.75
        locations = np.where(result >= threshold)
        
        # Draw rectangles around the matched regions
        for pt in zip(*locations[::-1]):
            cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)
        
        # Display the result
        cv2.imshow('Detected', img)
        
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cv2.destroyAllWindows()
