# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 22:46:56 2024

@author: User
"""

import cv2
import numpy as np
import os
import time
import mss
import pyautogui as pg

# File path
os.chdir('D:\GitHub\Whiteout-Survival')

# Load the template image
template = cv2.imread('help_button.png', cv2.IMREAD_GRAYSCALE)
w, h = template.shape[::-1]

# Define the screen capture region (adjust this to your game window's position and size)
# monitor = {'left': 850,
#         'top': 490,
#         'width': 195,
#         'height': 220
#         }

# Right box
monitor = {'left': 1615,
        'top': 790,
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
        threshold = 0.88
        locations = np.where(result >= threshold)
        
        
        if result.max() >= threshold:
            # Click help
            pg.moveTo(1710,910,0.1)
            pg.click()
            
        time.sleep(1)

# Release resources
cv2.destroyAllWindows()
