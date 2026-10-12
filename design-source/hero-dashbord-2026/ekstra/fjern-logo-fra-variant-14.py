import cv2, numpy as np
im=cv2.imread('../varianter/Regweb-Forsidebilde-14.jpg').astype(np.float64)
H,W=im.shape[:2]
x0,x1,y0,y1=640,1110,0,215
yy,xx=np.mgrid[y0:y1,x0:x1]
mask=np.zeros((H,W),np.uint8); mask[44:196,684:1040]=1   # logo + shadow
fitm=~mask[y0:y1,x0:x1].astype(bool); fitm &= ~((xx<672)&(yy>165)) & ~((xx>1095)&(yy>60))
def feats(x,y,d=3):
    u=(x-870)/220.;v=(y-107)/110.
    return np.stack([u**i*v**j for i in range(d+1) for j in range(d+1-i)],-1)
F=feats(xx,yy)
out=im.copy(); rng=np.random.default_rng(1)
fill=np.zeros((y1-y0,x1-x0,3))
res=[]
for c in range(3):
    A=F[fitm]; b=im[y0:y1,x0:x1,c][fitm]
    k,*_=np.linalg.lstsq(A,b,rcond=None)
    fill[...,c]=F@k; res.append((A@k-b).std())
print('resid',res)
# grain from nearby clean area
clean=im[0:40,700:1000]; g=clean-cv2.GaussianBlur(clean,(0,0),3); sig=g.std(); print('grain',sig)
fill+=rng.normal(0,sig,fill.shape)
m=cv2.GaussianBlur(mask[y0:y1,x0:x1].astype(np.float64),(0,0),5)[...,None]
m=np.clip(m*1.6,0,1)
m[:, :1]=0
out[y0:y1,x0:x1]=im[y0:y1,x0:x1]*(1-m)+fill*m
cv2.imwrite('Regweb-Forsidebilde-14-uten-logo.png',np.clip(out,0,255).astype(np.uint8))
c=np.clip(out,0,255).astype(np.uint8)[0:260,560:1160]
cv2.imwrite('crop_after.png',cv2.resize(c,None,fx=1.6,fy=1.6))
cv2.imwrite('crop_after_contrast.png',cv2.resize(np.clip((c.astype(float)-c.mean((0,1)))*6+128,0,255).astype(np.uint8),None,fx=1.6,fy=1.6))
