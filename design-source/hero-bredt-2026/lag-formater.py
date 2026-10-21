import cv2, numpy as np, os
im=cv2.imread('regweb_binder_ref.jpg').astype(np.float32); h,w=im.shape[:2]   # 1984x992 native
pad=566
seg=im[:,1560:1984]
piece=np.concatenate([seg[:,::-1],seg,seg[:,::-1]],axis=1)[:,:pad]
piece=cv2.GaussianBlur(piece,(0,0),sigmaX=35,sigmaY=1.2)
ext=np.concatenate([im,piece],axis=1)
j=w; bw=90
blur=cv2.GaussianBlur(ext[:,j-bw-60:j+bw+60],(0,0),sigmaX=30,sigmaY=1.2)[:,60:60+2*bw]
a=np.clip(np.arange(2*bw)/(2*bw-1),0,1)[None,:,None]
ext[:,j-bw:j+bw]=ext[:,j-bw:j+bw]*(1-a)+blur*a
rng=np.random.default_rng(1); ext[:,w:]+=rng.normal(0,1.0,ext[:,w:].shape[:2])[...,None]
ext=np.clip(ext,0,255).astype(np.uint8)       # 2550x992
O='formater'; os.makedirs(O,exist_ok=True)
cv2.imwrite(f'{O}/regweb-hero-utvidet-2550x992-native.png',ext)
def crop(x,wc,hc=992): return ext[:hc,x:x+wc]
def save(img,name,q=92,size=None):
    if size: img=cv2.resize(img,size,interpolation=cv2.INTER_LANCZOS4)
    cv2.imwrite(f'{O}/{name}.jpg',img,[cv2.IMWRITE_JPEG_QUALITY,q])
    print(name,img.shape[1],img.shape[0])
# bredt 2,577:1  (crop 2557x992 from x=0..2557 -> use full width 2550, trim height to ratio)
wide=ext[:, :]; ch=int(round(2550*1242/3200)); top=(992-ch)//2
wide=ext[top:top+ch]
save(wide,'regweb-hero-bredt-2550x989-native')
save(wide,'regweb-hero-bredt-3200x1242',size=(3200,1242))
save(wide,'regweb-hero-bredt-6400x2484-interpolert',q=90,size=(6400,2484))
# 16:9
c=crop(250,1764); save(c,'regweb-hero-16x9-1764x992-native'); save(c,'regweb-hero-16x9-1920x1080',size=(1920,1080)); save(c,'regweb-hero-16x9-3840x2160-interpolert',q=90,size=(3840,2160))
# 1:1
c=crop(640,992); save(c,'regweb-hero-1x1-992-native'); save(c,'regweb-hero-1x1-1080',size=(1080,1080)); save(c,'regweb-hero-1x1-2048-interpolert',q=90,size=(2048,2048))
# 4:5
c=crop(700,794); save(c,'regweb-hero-4x5-794x992-native'); save(c,'regweb-hero-4x5-1080x1350',size=(1080,1350)); save(c,'regweb-hero-4x5-1600x2000-interpolert',q=90,size=(1600,2000))
# 9:16
c=crop(700,558); save(c,'regweb-hero-9x16-558x992-native'); save(c,'regweb-hero-9x16-1080x1920',size=(1080,1920))
# OG / delingsbilde 1200x630
c=crop(260,1890); save(c,'regweb-hero-delingsbilde-1890x992-native'); save(c,'regweb-hero-delingsbilde-1200x630',q=88,size=(1200,630)); save(c,'regweb-hero-delingsbilde-2400x1260-interpolert',q=88,size=(2400,1260))
# original 2:1 and transparent cutout (native)
cv2.imwrite(f'{O}/regweb-perm-og-blyant-utklipp-gjennomsiktig-native.png',cv2.imread('cutout.png',cv2.IMREAD_UNCHANGED))
