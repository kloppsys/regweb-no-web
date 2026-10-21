import cv2, numpy as np
im=cv2.imread('regweb_binder_ref.jpg'); h,w=im.shape[:2]
mask=np.full((h,w),cv2.GC_BGD,np.uint8)
# binder: probable fg region, sure fg core
mask[95:870,770:1075]=cv2.GC_PR_FGD
mask[150:800,800:1040]=cv2.GC_FGD
# pencil
mask[800:900,1060:1495]=cv2.GC_PR_FGD
bgd=np.zeros((1,65)); fgd=np.zeros((1,65))
cv2.grabCut(im,mask,None,bgd,fgd,8,cv2.GC_INIT_WITH_MASK)
m=((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD)).astype(np.uint8)*255
m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
cv2.imwrite('mask_raw.png',m)
vis=im.copy(); vis[m==0]=(vis[m==0]*0.25+np.array([0,0,255])*0.75).astype(np.uint8)
cv2.imwrite('mask_vis.jpg',vis)
