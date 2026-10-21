import cv2, numpy as np
im=cv2.imread('regweb_binder_ref.jpg'); m=cv2.imread('mask_raw.png',0)
m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
n,lab,st,_=cv2.connectedComponentsWithStats(m)
order=sorted(range(1,n),key=lambda i:-st[i,4])
out=np.zeros_like(m)
for k,i in enumerate(order[:2]):
    comp=(lab==i).astype(np.uint8)*255
    cs,_=cv2.findContours(comp,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    hull=cv2.convexHull(np.vstack(cs))
    if k==0: print('binder bbox',st[i][:4])
    cv2.fillConvexPoly(out,hull,255)
    if k==1: print('pencil bbox',st[i][:4])
# slight erode to remove halo, then soften
out=cv2.erode(out,np.ones((3,3),np.uint8))
a=cv2.GaussianBlur(out,(0,0),0.9)
rgba=np.dstack([im,a]); cv2.imwrite('cutout.png',rgba)
bg=np.full_like(im,(70,200,70)); al=(a/255.)[...,None]; comp=(im*al+bg*(1-al)).astype(np.uint8)
cv2.imwrite('cut_check.jpg',comp)
cv2.imwrite('cut_crop1.jpg',cv2.resize(comp[80:300,740:1100],None,fx=3,fy=3,interpolation=cv2.INTER_NEAREST))
cv2.imwrite('cut_crop2.jpg',cv2.resize(comp[780:900,740:1500],None,fx=2,fy=2,interpolation=cv2.INTER_NEAREST))
