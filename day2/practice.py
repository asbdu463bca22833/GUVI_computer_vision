import cv2
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("image.jpg")
rows,cols=image.shape[:2]
(h, w) = image.shape[:2]

flipped = cv2.flip(image, 1)

cropped = image[50:100,100:300]

resize = cv2.resize(image,(200,400))

M = np.float32([[1,0,-10],[0,1,0]])
translate = cv2.warpAffine(image,M,(cols,rows))

RM = cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated = cv2.warpAffine(image, RM, (w,h))

scaled = cv2.resize(image,None,fx=2,fy=2)

line = cv2.line(image, (500,50), (200,50),(0,255,0),3)

rect = cv2.rectangle(image,(120,120),(150,100),(255,0,0),3)

circle = cv2.circle(image,(30,30),50,(0,0,255),1)
cv2.putText(image,"Open CV",(50,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
plt.imshow(cv2.cvtColor(line,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()

cv2.imwrite("output.jpg",image)