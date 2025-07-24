import cv2
import numpy as np

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

contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    epsilon = 0.048 * cv2.arcLength(contour, True)  
    approx = cv2.approxPolyDP(contour, epsilon, True)
    
    x, y, w, h = cv2.boundingRect(approx)
    
    if len(approx) == 3:
        shape_name = "Triangle"
    
    elif len(approx) == 4:
        shape_name = "Square"
    
    else:
        epsilon = 0.015 * cv2.arcLength(contour, True)  
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