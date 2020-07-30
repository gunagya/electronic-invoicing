import cv2

def show_image(wname, img):
	cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
	cv2.imshow(wname, img)

img_loc = '../Images/Sample12/page_1.jpg'
img = cv2.imread(img_loc, cv2.IMREAD_GRAYSCALE)

#img=

show_image("Image", img)
cv2.waitKey(0)
