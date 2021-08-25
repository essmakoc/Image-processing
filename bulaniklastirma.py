import cv2
import matplotlib.pyplot as plt
import numpy as np

import warnings
warnings.filterwarnings("ignore")

img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

plt.figure()
plt.imshow(img)
plt.axis("off"), plt.title("orijinal")
plt.show()


"""
    -ortalama bulanıklaştırma yontemi
        kutu piksel alanının ortalamasını alıyor
"""

dst2 = cv2.blur(img, ksize = (3, 3))
plt.figure()
plt.imshow(dst2)
plt.axis("off"), plt.title("ortalama bulanıklaştırma")
plt.show()


"""
    -gaussian blur
        kutucukta x ve y yonlerinde sigma degerleri 2 boyutlu gaus

"""

gb = cv2.GaussianBlur(img, ksize = (3, 3), sigmaX = 7)
plt.figure()
plt.imshow(gb)
plt.axis("off"), plt.title("gaussian bulanıklaştırma")
plt.show()

"""
    -medyan bulanıklaştırma
        kutucukta ortadaki deger alinir

"""

mb = cv2.medianBlur(img, ksize = 3)
plt.figure()
plt.imshow(mb)
plt.axis("off"), plt.title("medyan bulanıklaştırma")
plt.show()




def gaussianNoise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var**0.5
    
    gauss = np.random.normal(mean, sigma, (row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    
    return noisy



#ice aktar normalize et
img = cv2.imread("C:/Users/ASUS/.spyder-py3/Image processing/NYC.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)/255

plt.figure()
plt.imshow(img)
plt.axis("off"), plt.title("orijinal")
plt.show()



# Resme noisy ekledik
gaussianNoiseImage = gaussianNoise(img)
plt.figure()
plt.imshow(gaussianNoiseImage)
plt.axis("off"), plt.title("Gaussian Noise Image")
plt.show()


#gaus bulanıklaştırma
gb2 = cv2.GaussianBlur(gaussianNoiseImage, ksize = (3, 3), sigmaX = 7)
plt.figure()
plt.imshow(gb2)
plt.axis("off"), plt.title("With gaussian bulanıklaştırma")
plt.show()




def saltPepperNoise(image):
    row, col, ch = image.shape
    s_vs_p = 0.5
     
    amount = 0.004
    
    noisy = np.copy(image)
    
    #salt
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i - 1, int(num_salt)) for i in image.shape]
    noisy[coords] = 1  
    
    
    #pepper
    num_pepper = np.ceil(amount * image.size * (1 - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    noisy[coords] = 0
    
    return noisy

spImage = saltPepperNoise(img)
plt.figure()
plt.imshow(spImage)
plt.axis("off"), plt.title("SP Image")
plt.show()


#
mb2 = cv2.medianBlur(spImage.astype(np.float32()), ksize = 3)
plt.figure()
plt.imshow(mb2)
plt.axis("off"), plt.title("With medyan blur")
plt.show()



    





