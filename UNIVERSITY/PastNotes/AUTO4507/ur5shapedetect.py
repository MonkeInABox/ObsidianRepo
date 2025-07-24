# Echo client program
import socket
import time
import requests
import cv2
import numpy as np

HOST = "192.168.0.3" # the remote host
PORT = 30002 # The same part used by server
CAMERA_PORT = 4242
count = 0

#width 63 h 44
#643 -230 203 2.28 -2.46 0.465
while count < 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (HOST, PORT) )
    time.sleep(0.5)

    # GET AND SAVE IMAGE
    resp = None
    try:
        resp = requests.get(f"http://{HOST}:{CAMERA_PORT}/current.jpg?type=color", stream=True)
    except:
        pass

    if resp == None:
        print("No image")
    else:
        print("image taken")

        # Saving image for testing purposes
        file = open("UR5eImage.jpg", "wb")
        file.write(resp.content)
        file.close()

        # change time to get more or less frames per second
        time.sleep(0.05)

        image = cv2.imread("UR5eImage.jpg")
        kernel = np.ones((5,5), np.float32) / 30
        dst = cv2.filter2D(image, -1, kernel)

        grey_image = cv2.cvtColor(dst, cv2.COLOR_BGR2GRAY)

        grey_image = cv2.GaussianBlur(grey_image, (5, 5), 0)

        _, thresh = cv2.threshold(grey_image, 150, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        thresh = cv2.medianBlur(thresh, 5)
        thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

        edged = cv2.Canny(thresh, 230, 255)

        contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            epsilon = 0.049 * cv2.arcLength(contour, True)  
            approx = cv2.approxPolyDP(contour, epsilon, True)
            
            x, y, w, h = cv2.boundingRect(approx)
            
            if len(approx) == 3:
                shape_name = "Triangle"
            
            elif len(approx) == 4:
                shape_name = "Square"
            
            else:
                epsilon = 0.02 * cv2.arcLength(contour, True)  
                approx = cv2.approxPolyDP(contour, epsilon, True)
                
                hull = cv2.convexHull(contour, returnPoints=False)
                hull = np.sort(hull)
                defects = cv2.convexityDefects(contour, hull)
                concave_defects = defects.shape[0]
                if concave_defects != 0 and len(approx) > 7:
                    shape_name = "Star"
                else:
                    shape_name = "Semicircle"
            M=cv2.moments(contour)
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            print(f"Shape: {shape_name}, Position: {cX}, {cY}")
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 3)
            cv2.putText(image, shape_name, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        cv2.imshow("Shape Detection", image)
        print("Number of contours = " + str(len(contours)))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    
    count += 1
    data = s.recv(1024)

    s.close()

    #print("Received", repr(data))