

# Matplotlib library


import matplotlib.pyplot as plt
from matplotlib import cm

# Numpy library
import numpy as np

from skimage import io
import skimage

from skimage import exposure
#img1 = io.imread('images/lena-grey.bmp')

#io.imshow(img1)

#img1 = io.imread('images/vibot-color.jpg',as_grey = True)

img1 = io.imread('images/lena-grey.bmp')


print "shape: "+str(np.shape(img1))


#print "type: "+str(np.dtype(img1[0,0]))

img2 = skimage.img_as_float(img1)



plt.imshow(img2, cmap = cm.Greys_r)
plt.show()


io.imsave('images_generated/lena-grey-float.bmp',img2)



plt.imshow(exposure.histogram(img2,nbins = 2))

plt.show()

'''
plt.hist(img2, bins = 'auto')

plt.show()
'''

hist, bin = np.histogram(img2, bins = 50)

plt.imshow(hist)

plt.show()




print "bye"
