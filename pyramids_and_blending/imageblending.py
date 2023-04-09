import cv2
import numpy as np
import matplotlib.pyplot as plt

#Reading images
face_boy = cv2.imread("FaceA.jpg")
face_boy = cv2.cvtColor(face_boy, cv2.COLOR_BGR2RGB)

face_girl = cv2.imread("FaceB.jpg")
face_girl = cv2.cvtColor(face_girl, cv2.COLOR_BGR2RGB)

mask = cv2.imread("mask.jpg")
mask = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)


face_boy = cv2.resize(face_boy,dsize = (256,256))
face_girl = cv2.resize(face_girl,dsize =  (256,256))
mask = cv2.resize(mask, dsize =  (256,256))

#mask normalize
mask = mask//255

boy = face_boy.copy()
girl = face_girl.copy()
filter = mask.copy()

#shapes of images
print(boy.shape)
print(girl.shape)
print(filter.shape)


"""
g_pyr = gaussian pyramid
lp_pyr = laplacian pyramid
"""
# Gaussian pyramid
g_pyr_boy = [face_boy]
# rang floor(log(min_dim_size)/log2) - 4
rang = 4 
for i in range(rang):
    boy = cv2.pyrDown(boy)
    g_pyr_boy.append(boy)
    
g_pyr_girl = [face_girl]
for i in range(rang):
    girl = cv2.pyrDown(girl)
    g_pyr_girl.append(girl)

fig, ax = plt.subplots(1, len(g_pyr_girl), figsize=(20, 4))
for i in range(len(g_pyr_girl)):
    ax[i].imshow(g_pyr_girl[i])
    ax[i].set_title('Level ' + str(i))
fig.savefig("gaussian pyramid")
   
g_pyr_mask = [mask]
for i in range(rang):
    filter = cv2.pyrDown(filter)
    g_pyr_mask.append(filter)
    
    
# Laplacian pyramid
boy_last_pyramid = g_pyr_boy[-1]   
lp_pyr_boy = [boy_last_pyramid]

for i in range(rang,0,-1):
    gaussian_expanded = cv2.pyrUp(g_pyr_boy[i])
    laplacian = cv2.subtract(g_pyr_boy[i-1],gaussian_expanded)
    lp_pyr_boy.append(laplacian)

girl_last_pyramid = g_pyr_girl[-1]
lp_pyr_girl = [girl_last_pyramid]

for i in range(rang,0,-1):
    gaussian_expanded = cv2.pyrUp(g_pyr_girl[i])
    laplacian = cv2.subtract(g_pyr_girl[i-1],gaussian_expanded)
    lp_pyr_girl.append(laplacian)
    
fig, ax = plt.subplots(1, len(lp_pyr_girl), figsize=(20, 4))
for i in range(len(lp_pyr_girl)):
    ax[i].imshow(lp_pyr_girl[i])
    ax[i].set_title('Level ' + str(i))
fig.savefig("laplacian pyramid")
 
# for blending    
g_pyr_mask = reversed(g_pyr_mask)
boy_girl_mask_blend = []

for boy,girl,mask in zip(lp_pyr_boy,lp_pyr_girl,g_pyr_mask):
    
    blending = (mask*boy) + ((1-mask)*girl)
    boy_girl_mask_blend.append(blending)
    

#plot the boy girl mask blending level by level

fig, ax = plt.subplots(1, len(boy_girl_mask_blend), figsize=(20, 4))
for i in range(len(boy_girl_mask_blend)):
    ax[i].imshow(boy_girl_mask_blend[i])
    ax[i].set_title('Level ' + str(i))
fig.savefig("laplacian")

# reconstruct the image form level by level blending 
for i in range(len(boy_girl_mask_blend)-1):
    final = cv2.pyrUp(boy_girl_mask_blend[i])
    boy_girl_mask_blend[i+1] = final + boy_girl_mask_blend[i+1]
    
# write the image
image = boy_girl_mask_blend[-1]
fig, ax = plt.subplots(1, 1, figsize=(20, 4))
ax.imshow(image)
fig.savefig("blended_image")
#show the blending image
cv2.imshow("blend",boy_girl_mask_blend[-1])
cv2.waitKey(0)

