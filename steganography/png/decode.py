import sys
import cv2

image = cv2.imread(sys.argv[1])
binary_data = ""
for row in image:
    for pixel in row:
        r = format(pixel[0], "08b")
        g = format(pixel[1], "08b")
        b = format(pixel[2], "08b")
        binary_data += r[-1]
        binary_data += g[-1]
        binary_data += b[-1]

all_bytes = [ binary_data[i: i+8] for i in range(0, len(binary_data), 8) ]
decoded_data = ""
for byte in all_bytes:
    decoded_data += chr(int(byte, 2))
    if decoded_data[-5:] == "-msg-":
        break
print(">>> Decoded data:")
print(decoded_data[:-5])