import cv2
import numpy as np

image = cv2.imread("image.jpg")
rows, cols = image.shape[:2]

tx, ty = 100, 50
translation_matrix = np.float32([[1, 0, tx],[0, 1, ty]])
translated=cv2.warpAffine(image, translation_matrix, (cols, rows))
cv2.warpAffine(image, translation_matrix, (cols, rows))
angle =45
rotation_matrix = cv2.getRotationMatrix2D ((cols/2, rows/2), angle, 1)
rotated=cv2.warpAffine(image, rotation_matrix, (cols, rows))
scaled = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)


cv2.imwrite('translation.jpg', translated)
cv2.imwrite('rotation.jpg', rotated)
cv2.imwrite('scaled.jpg', scaled)