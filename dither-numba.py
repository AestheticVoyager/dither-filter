import numpy as np
from PIL import Image
import numba

@numba.jit("f4[:,:,:](f4[:,:,:])", nopython=True, nogil=True)
def floyd_steinberg(image):
    Lx, Ly, Lc = image.shape
    for j in range(Ly):
        for i in range(Lx):
            for c in range(Lc):
                rounded = round(image[i,j,c])
                err = image[i,j,c] - rounded
                image[i,j,c] = rounded
                if i<Lx-1:
                    image[i+1,j,c] += (7/16)*err
                if j<Ly-1:
                    image[i,j+1,c] += (5/16)*err
                    if i>0:
                        image[i-1,j+1,c] += (1/16)*err
                    if i<Lx-1:
                         image[i+1,j+1,c] += (3/16)*err
    return image

@numba.jit("f4[:,:,:](f4[:,:,:])", nopython=True, nogil=True)
def atkinson(image):
    frac = 8
    Lx, Ly, Lc = image.shape
    for j in range(Ly):
        for i in range(Lx):
            for c in range(Lc):
                rounded = round(image[i,j,c])
                err = image[i,j,c] - rounded
                image[i,j,c] = rounded
                if i<Lx-1:
                    image[i+1,j,c] += err / frac
                if i<Lx-2:
                    image[i+2,j,c] += err /frac
                if j<Ly-1:
                    image[i,j+1,c] += err / frac
                    if i>0:
                        image[i-1,j+1,c] += err / frac
                    if i<Lx-1:
                        image[i+1,j+1,c] += err / frac
                if j<Ly-2:
                    image[i,j+2,c] += err / frac
    return image

# Large Color Image
image = Image.open('./test.JPG')
data = np.array(image).astype(np.float32) / 255.
data_fs = floyd_steinberg(data.copy())
data_atk = atkinson(data.copy())

# Save the images
Image.fromarray((data_fs * 255).astype(np.uint8)).save('floyd_steinberg.jpg')
Image.fromarray((data_atk * 255).astype(np.uint8)).save('atkinson.jpg')

