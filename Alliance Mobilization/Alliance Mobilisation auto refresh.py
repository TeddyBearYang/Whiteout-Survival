# Import all required packages
import cv2
import numpy as np
import os
import time
import mss
import pyautogui as pg

# Set a threshold to identify matching regions and refresh time
threshold = 0.98
refresh = 300

# Choose which side of mission to enable auto refresh
left = 1
right = 1

# File path
os.chdir('D:\GitHub\Whiteout-Survival\Alliance Mobilization')

# Load mission images
mission_1 = cv2.imread('target_mission_1.png', cv2.IMREAD_GRAYSCALE)
mission_2 = cv2.imread('target_mission_2.png', cv2.IMREAD_GRAYSCALE)

# Initialise left mission location on screen
exclusive_mission_monitor_left = {'left': 1335,
        'top': 490,
        'width': 195,
        'height': 220
        }

# Initialise right mission location on screen
exclusive_mission_monitor_right = {'left': 1500,
        'top': 490,
        'width': 195,
        'height': 220
        }

# Initialise loop counter
i = 1

# Create an MSS instance
with mss.mss() as sct:
    while True:
        ############# Left mission #################
        # Check if left side is enabled
        if left == 1:
        
            # Capture the screen
            screen = sct.grab(exclusive_mission_monitor_left)
            
            # Convert the screen to a NumPy array
            img = np.array(screen)
            
            # Convert the screen to grayscale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Perform template matching
            result1 = cv2.matchTemplate(img_gray, mission_1, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img_gray, mission_2, cv2.TM_CCOEFF_NORMED)
            
            # Check if the target mission has spawned
            if result1.max() < threshold and result2.max() < threshold:           
                # Refresh left mission
                pg.moveTo(1460,580,0.2)
                pg.click(1460,580)
                pg.moveTo(1515,677,0.2)
                pg.click()
                pg.moveTo(1690,657,0.2)
                pg.click()
                
            # Save image and print similarity score
            cv2.imwrite('left_mission_image'+str(i)+'.png', img)
            print('Left mission ' + str(i) + ' similarity score with target mission 1 & 2 is: '
                  + str(round(result1.max(),3)) + ' and ' + str(round(result2.max(),3)))
            
            time.sleep(1)
        
        ################ Right mission ###############################################
        # Check if right side is enabled
        if right == 1:
        
            # Capture the screen
            screen = sct.grab(exclusive_mission_monitor_right)
    
            # Convert the screen to a NumPy array
            img = np.array(screen)
    
            # Convert the screen to grayscale
            img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
            # Perform template matching
            result1 = cv2.matchTemplate(img_gray, mission_1, cv2.TM_CCOEFF_NORMED)
            result2 = cv2.matchTemplate(img_gray, mission_2, cv2.TM_CCOEFF_NORMED)
            # result3 = cv2.matchTemplate(img_gray, mission_3, cv2.TM_CCOEFF_NORMED)
            
            if result1.max() < threshold and result2.max() < threshold:
                # Refresh right mission
                pg.moveTo(1609,580,0.2)
                pg.click(1609,580)
                pg.moveTo(1515,677,0.2)
                pg.click()
                pg.moveTo(1690,657,0.2)
                time.sleep(1)
                pg.click()
            
            # Save image
            cv2.imwrite('right_mission_image'+str(i)+'.png', img)
            print('Right mission ' + str(i) + ' similarity score with target mission 1 & 2 is: '
                  + str(round(result1.max(),3)) + ' and ' + str(round(result2.max(),3)))
            
        # Update counter
        i += 1
                
        # Wait for specified time before the next capture
        time.sleep(refresh + 1)

