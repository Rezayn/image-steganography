from PIL import Image
import numpy as np
img = Image.open('rr.png')
pixel = np.array(img)

with open('test.txt', 'r') as f:
    text = f.read()

texts = ''.join([format(ord(i), "08b") for i in text])


hidden = ""
bin_list = []
msg = ""
text_list = []
for i in range(8):
    for j in range(2359):
        hidden += format(pixel[i][j], '08b')[7]
print(hidden)

start = 0
end = 8
for i in range(len(hidden)//8):
    bin = hidden[start:end]
    b = texts[start:end]
    bin_list.append(bin)
    text_list.append(b)
    start = end
    end += 8

for i in bin_list:
    msg += chr(int(i,2))
print(msg)

