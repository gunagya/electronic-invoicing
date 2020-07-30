import cv2
import numpy as np
import pytesseract

#Tool for debugging

def show_image(wname, img):
	cv2.namedWindow(wname, cv2.WINDOW_NORMAL)
	cv2.imshow(wname, img)

def run_ocr(img):
	results = pytesseract.image_to_data(img, output_type=pytesseract.Output.DICT)
	min_conf=80

	for i in range(0, len(results["text"])):
		# extract the bounding box coordinates of the text region from
		# the current result
		x = results["left"][i]
		y = results["top"][i]
		w = results["width"][i]
		h = results["height"][i]
		# extract the OCR text itself along with the confidence of the
		# text localization
		text = results["text"][i]
		conf = int(results["conf"][i])
		if conf > min_conf:
			# display the confidence and text to our terminal
			print("Confidence: {}".format(conf))
			print("Text: {}".format(text))
			print("")
			# strip out non-ASCII text so we can draw the text on the image
			# using OpenCV, then draw a bounding box around the text along
			# with the text itself
			text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
			cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
			cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
	
	show_image("OCR Results", img)
	
def otsu_binarization(img):
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	_ ,bin_img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
	bin_img = cv2.dilate(bin_img ,cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20)),iterations = 1)
	return bin_img
	
img=cv2.imread('../Images/page_image.jpg')
run_ocr(img)
cv2.waitKey(0)
