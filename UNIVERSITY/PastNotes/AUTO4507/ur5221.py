import cv2
import numpy as np
import time
import socket
HOST = "192.168.0.9" # the remote host
PORT = 30002 # The same part used by server

# Connect to the UR5 robot
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# Load image
image = cv2.imread("UR5eImage.jpg")
kernel = np.ones((5,5), np.float32) / 30
dst = cv2.filter2D(image, -1, kernel)

grey_image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)
grey_image = cv2.GaussianBlur(grey_image, (5, 5), 0)

_, thresh = cv2.threshold(grey_image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
thresh = cv2.medianBlur(thresh, 5)
thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

edged = cv2.Canny(thresh, 230, 255)

contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Get camera image dimensions
height, width = grey_image.shape

# Camera frame center
cam_center_x = width // 2
cam_center_y = height // 2

def move_to_contour(x, y):
    """ Moves UR5 towards the detected object """
    threshold = 10  # Pixel threshold for stopping
    speed = 0.05  # Linear movement speed

    while True:
        # Compute direction
        move_x = (x - cam_center_x) / width  # Normalize movement
        move_y = (y - cam_center_y) / height

        # Convert to robot movement (adjust scale factors)
        dx = move_x * speed  # Scale factor for movement
        dy = -move_y * speed  # Negative due to coordinate system differences

        # Move robot
        pose = s.send("get_actual_tcp_pose()" + "\n") # Get current pose [x, y, z, rx, ry, rz]
        new_pose = [pose[0] + dx, pose[1] + dy, pose[2], pose[3], pose[4], pose[5]]
        s.send("movel(new_pose, acc=0.3, vel=speed)" + "\n")

        # Get updated camera frame and reprocess to check if object is centered
        # (In real implementation, update x, y using live camera feed)
        if abs(x - cam_center_x) < threshold and abs(y - cam_center_y) < threshold:
            print(f"Object centered at ({x}, {y})")
            break

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    center_x, center_y = x + w // 2, y + h // 2
    move_to_contour(center_x, center_y)

s.close()
