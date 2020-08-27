import numpy as np
import sys, os
import tensorflow as tf
from tensorflow.python.keras.preprocessing import image as kp_image
from PIL import Image #to read images

print("usage :  python test_python.py  miNoir_miBlanc.png  miBlanc_miNoir.png ")

def test_(path1,path2):

	maxi=256
	 
	img0 = Image.open(path1) #image mi blanc mi noir
	img1 = Image.open(path2) #image mi noir mi blanc

	L = max(img0.size)
	scale = maxi/L
	 
	img0 = img0.resize((round(img0.size[0]*scale), round(img0.size[1]*scale)), Image.ANTIALIAS)
	img1 = img1.resize((round(img1.size[0]*scale), round(img1.size[1]*scale)), Image.ANTIALIAS)

	#processing
	img0 = kp_image.img_to_array(img0)
	img1 = kp_image.img_to_array(img1)
	img0=img0[:,:,0]
	img1=img1[:,:,0]
	img_res = (img0+img1)/2  
	result = (img_res).astype(np.uint8)  

	img4 =  Image.fromarray((result).astype(np.uint8)) 
	return img4     

if __name__ == "__main__":
	path1=sys.argv[1]
	path2=sys.argv[2]
	img = test_(path1,path2)
	img.save("out.png")


 
 