import os
import PIL
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dataset_path = "D:\RandomDatasetler\words"

image_heights = []
image_widths = []
image_names = []
for files in os.listdir(dataset_path):
    for file in os.listdir(os.path.join(dataset_path, files)):
        image = PIL.Image.open(dataset_path + "\\" + files + "\\" + file)
        width, height = image.size
        image_widths.append(width)
        image_heights.append(height)
        image_names.append(dataset_path + "\\" + files + "\\" + file)
max_width_index = image_widths.index(max(image_widths))
max_height_index = image_heights.index(max(image_heights))
print("Max Height : ", max(image_heights), "Max Width : ", max(image_widths))
print("Average Height : ", sum(image_heights) / len(image_heights),
      "Average Width : ", sum(image_widths) / len(image_widths))
print("Image with Max height : ", image_names[max_height_index])
print("Image with Max width : ", image_names[max_width_index])

fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
imgplot = plt.imshow(mpimg.imread(image_names[max_width_index]))
ax.set_title('Max Width')

ax = fig.add_subplot(1, 2, 2)
imgplot = plt.imshow(mpimg.imread(image_names[max_height_index]))
imgplot.set_clim(0.0, 0.7)
ax.set_title('Max Height')
plt.show()