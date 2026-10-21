import cv2, numpy as np
im=cv2.imread('regweb_binder_ref.jpg').astype(np.float32); h,w=im.shape[:2]
pad=566
seg=im[:,1560:1984]
piece=np.concatenate([seg[:,::-1],seg,seg[:,::-1]],axis=1)[:,:pad]
piece=cv2.GaussianBlur(piece,(0,0),sigmaX=35,sigmaY=1.2)
# seam blend: widen working strip around the join
ext=np.concatenate([im,piece],axis=1)
j=w; bw=90
left=ext[:,j-bw:j].copy(); 
blur=cv2.GaussianBlur(ext[:,j-bw-60:j+bw+60],(0,0),sigmaX=30,sigmaY=1.2)[:,60:60+2*bw]
a=np.clip((np.arange(2*bw)-0)/(2*bw-1),0,1)[None,:,None]
ext[:,j-bw:j+bw]=ext[:,j-bw:j+bw]*(1-a)+blur*a
rng=np.random.default_rng(1); g=rng.normal(0,1.0,ext[:,w:].shape[:2])[...,None]; ext[:,w:]+=g
out=np.clip(ext,0,255).astype(np.uint8)
out=cv2.resize(out,(3200,int(round(out.shape[0]*3200/out.shape[1]))),interpolation=cv2.INTER_LANCZOS4)
top=(out.shape[0]-1242)//2; out=out[top:top+1242]
cv2.imwrite('heroP_3200.jpg',out,[cv2.IMWRITE_JPEG_QUALITY,92])
cv2.imwrite('heroP_prev.jpg',cv2.resize(out,(1600,621),interpolation=cv2.INTER_AREA)); print(out.shape)
