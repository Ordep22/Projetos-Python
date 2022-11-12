import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont


img = cv.imread("/Users/PedroVitorPereira/PycharmProjects/CursodePython/TCC-1/Frame vagoes Grabcut/1.jpg")
#img = img1[0:225, 400:1000]

grey = cv.cvtColor(img, cv.COLOR_BGRA2GRAY)
kernel = np.ones((5,5),np.uint8)
# Blurring and erasing little details
grey = cv.GaussianBlur(grey,(9,9),1)
grey = cv.morphologyEx(grey, cv.MORPH_OPEN, kernel)
grey = cv.morphologyEx(grey, cv.MORPH_CLOSE, kernel)
canny = cv.Canny(grey,190,200)
circles = cv.HoughCircles(grey,cv.HOUGH_GRADIENT,dp=1.8,minDist=95,param1=200,param2=35,minRadius=35,maxRadius=110)


circles = np.uint16(np.around(circles))
cimg = img.copy()
for i in circles[0, :]:

    # draw the outer circle
    cv.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # draw the center of the circle
    #cv.circle(cimg, (i[0], i[1]), 2, (255, 0, 0), 10)


# Convert to PIL Image
cv2_im_rgb = cv.cvtColor(cimg, cv.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im_rgb)
draw = ImageDraw.Draw(pil_im)
# Choose a font

# Draw the text
nun_bob = np.shape(circles)
print(nun_bob)
#draw.text((0, 0), f'O foram identificadas {nun_bob[1]} bobinas', fill = "green",font = 0)
draw.text((5, 5), f'O foram identificadas {nun_bob[1]} bobinas', fill ="red", align ="right")
# Save the image
print(circles)
cv_im_processed = pil_im.getim()
cv.imshow("cv2_im_processed", cv_im_processed)
cv.waitKey()
plt.show()