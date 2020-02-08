
# pip3 install opencv-python

import sys
import cv2

clear_text = sys.argv[2]+"-msg-"
message = ''.join([ format(ord(i), "08b") for i in clear_text ])

image = cv2.imread(sys.argv[1])

data_index = 0
data_len = len(message)
max_bytes = image.shape[0] * image.shape[1] * 3 // 8
if len(clear_text) > max_bytes:
	raise ValueError(">>> ERROR: The selected image is not big enough to hold the message.")

for row in image:
    for pixel in row:
        r = format(pixel[0], "08b")
        g = format(pixel[1], "08b")
        b = format(pixel[2], "08b")
        
        if data_index < data_len:
        	pixel[0] = int(r[:-1] + message[data_index], 2)
        	data_index += 1
        if data_index < data_len:
        	pixel[1] = int(g[:-1] + message[data_index], 2)
        	data_index += 1
       	if data_index < data_len:
       		pixel[2] = int(b[:-1] + message[data_index], 2)
       		data_index += 1
       	if data_index >= data_len:
       		break

cv2.imwrite("output.PNG", image)
print(">>> Image encoded.")