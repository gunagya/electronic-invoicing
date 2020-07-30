import os
import cv2
from pdf2image import convert_from_path

invoice_dir = '../Sample Invoices/'
image_dir = '../Images/'

def convert_pdf():
	for dirpath, dirnames, files in os.walk(invoice_dir):
		for file_name in files:
			pages = convert_from_path(invoice_dir+file_name, 500)
			print('Saving '+file_name[:-4]+' ...')
			os.mkdir(image_dir+file_name[:-4])
			for page_no, page in enumerate(pages, 1):
				page.save(image_dir+file_name[:-4]+'/page_'+str(page_no)+'.jpg', 'JPEG')
	print('Converted pdf files to images')

def clean(img):
	return img
	
def clean_all():
	for dirpath, dirnames, files in os.walk(image_dir):
		print('Cleaning '+dirpath+' ...')
		for file_name in files:
			img=cv2.imread(dirpath+'/'+file_name)
			img=clean(img)
			cv2.imwrite(dirpath+'/'+file_name, img)
	print('Finished cleaning images')
		 

clean_all()
