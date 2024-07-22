import numpy as np
import cv2
import matplotlib.pyplot as plt

# resize images 
bg = cv2.imread("Module_2/Week2_Vector/GreenBackground.png")
bg = cv2.cvtColor(bg, cv2.COLOR_BGR2RGB)
bg = cv2.resize(bg,(678,381))
                
new_bg = cv2.imread("Module_2/Week2_Vector/NewBackground.jpg")
new_bg = cv2.cvtColor(new_bg, cv2.COLOR_BGR2RGB)
new_bg = cv2.resize(new_bg,(678,381))

obj = cv2.imread("Module_2/Week2_Vector/Object.png")
obj = cv2.cvtColor(obj, cv2.COLOR_BGR2RGB)
obj = cv2.resize(obj,(678,381))

# compute difference between object and bg
def compute_difference(bg,obj):
    return cv2.absdiff(bg,obj)
# compute binary mask
def compute_binary_mask(differece_single_channel):
    mask_binary = cv2.threshold(differece_single_channel,1,255,cv2.THRESH_BINARY)[1]
    return mask_binary

diff = compute_difference(bg,obj)
binary_msk = compute_binary_mask(diff)
plt.imshow(binary_msk)
plt.show()
target_img = np.where(binary_msk > 0,obj,new_bg)
plt.imshow(target_img)
plt.show()



