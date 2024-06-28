# Import all required packages
import cv2
import numpy as np
import os
import time
import mss
import pyautogui as pg

# File path
os.chdir('D:\GitHub\Whiteout-Survival')

# Load mission images
mission_1 = cv2.imread('target_mission_1.png', cv2.IMREAD_GRAYSCALE)
mission_2 = cv2.imread('target_mission_2.png', cv2.IMREAD_GRAYSCALE)
mission_3 = cv2.imread('target_mission_3.png', cv2.IMREAD_GRAYSCALE)

# Initialise mission location on screen
exclusive_mission_monitor_left = {'left': 850,
        'top': 490,
        'width': 195,
        'height': 220
        }

# Initialise mission location on screen
exclusive_mission_monitor_right = {'left': 1015,
        'top': 490,
        'width': 195,
        'height': 220
        }

# Create an MSS instance
with mss.mss() as sct:
    while True:
        # Capture the screen
        screen = sct.grab(exclusive_mission_monitor_left)
        
        # Convert the screen to a NumPy array
        img = np.array(screen)
        
        # Convert the screen to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Perform template matching
        result1 = cv2.matchTemplate(img_gray, mission_1, cv2.TM_CCOEFF_NORMED)
        result2 = cv2.matchTemplate(img_gray, mission_2, cv2.TM_CCOEFF_NORMED)
        result3 = cv2.matchTemplate(img_gray, mission_3, cv2.TM_CCOEFF_NORMED)

        # Set a threshold to identify matching regions
        threshold = 0.85
        
        # Check if the target mission has spawned
        if result1.max() < threshold and result2.max() < threshold and result3.max() < threshold:            
            # Refresh left mission
            pg.moveTo(947,580,0.2)
            pg.click(947,580)
            pg.moveTo(1029,677,0.5)
            pg.click()
            pg.moveTo(1193,686,0.5)
            pg.click()
            
        #######################################################################
        # Capture the screen
        screen = sct.grab(exclusive_mission_monitor_right)
        
        # Convert the screen to a NumPy array
        img = np.array(screen)
        
        # Convert the screen to grayscale
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Perform template matching
        result1 = cv2.matchTemplate(img_gray, mission_1, cv2.TM_CCOEFF_NORMED)
        result2 = cv2.matchTemplate(img_gray, mission_2, cv2.TM_CCOEFF_NORMED)
        result3 = cv2.matchTemplate(img_gray, mission_3, cv2.TM_CCOEFF_NORMED)
        
        if result1.max() < threshold and result2.max() < threshold and result3.max() < threshold:
            # Refresh right mission
            pg.moveTo(1109,580,0.2)
            pg.click(1109,580)
            pg.moveTo(1029,677,0.5)
            pg.click()
            pg.moveTo(1193,686,0.5)
            pg.click()
                
        # Wait for specified time before the next capture
        time.sleep(302)

