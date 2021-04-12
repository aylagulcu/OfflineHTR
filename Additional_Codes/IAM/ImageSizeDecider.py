import os
import PIL
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
dir_path = "D:\\Authors"


file_names = []
image_heights = []
image_widths = []

for foldername in os.listdir(dir_path):
    for filename in os.listdir(os.path.join(dir_path, foldername)):
        image = PIL.Image.open(dir_path + "\\" + foldername + "\\" + filename)
        width, height = image.size
        
        file_names.append(dir_path + "\\" + foldername + "\\" + filename)
        image_widths.append(width)
        image_heights.append(height)


maxw_index = np.argmax(image_widths)
maxh_index = np.argmax(image_heights)

print("Max Height : ",image_heights[maxh_index] , 
"Max Width : ", image_widths[maxw_index])
print("Index of max width image : ",  str(maxw_index),"File Location :", file_names[maxw_index] )
print("Index of max height image : ",str(maxh_index), "File Location :", file_names[maxh_index] )
print("Avarage Height : ", sum(image_heights) / len(image_heights),
      "Avarage Width : ", sum(image_widths) / len(image_widths))


fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot =plt.imshow(mpimg.imread(file_names[maxw_index]), cmap="gray")
ax.set_title('Max Width')

ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(mpimg.imread(file_names[maxh_index]),cmap="gray")
imgplot.set_clim(0.0, 0.7)
ax.set_title('Max Height')





