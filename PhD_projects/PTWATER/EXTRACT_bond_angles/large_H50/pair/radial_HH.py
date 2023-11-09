import numpy as np
import os
import math
import time

import sys

res=str(sys.argv[1])
filename2=str(sys.argv[2])
zzmin=float(sys.argv[3])
zzmax=float(sys.argv[4])
dx=float(sys.argv[5])

os.system('rm tempo')
filename='tempo'

atoms=1692

start_time = time.time()
vec1=np.array([[19.4,0.0,0.0],[0.0,19.2,0.0],[0.0,0.0,70]],float)
ivec1=np.linalg.inv(vec1)

rmax=9.6
rmin=0.0
#dx=0.2
bins=int((rmax-rmin)/dx)
h=zzmax-zzmin

f=open(res,'r')
aa=f.readlines()
f.close

frames=int(len(aa)/(atoms+2))

    
mo=np.zeros((frames,bins), dtype=float)
mo1=np.zeros((frames,bins), dtype=float)
mo2=np.zeros((frames,bins), dtype=float)

for i in range(frames):
    print (i)
    cord=[]
    for j in range(1664+2-56,1664+2):
       t1=aa[j+(i)*(atoms+2)].split()
       cord.append(t1[3])

    cord=np.array(cord,float)
    mean=np.mean(cord)
   
    del cord
 
#########################################################################
    coord=[]
    coord2=[]
    coord3=[]
    for j in range(2,1442,3):
       t1=aa[j+1+(i)*(atoms+2)].split()
       t2=np.array(t1[1:],float)
       t2[2]=t2[2]-mean
       
       t1=aa[j+2+(i)*(atoms+2)].split()
       t3=np.array(t1[1:],float)
       t3[2]=t3[2]-mean

       if (float(t2[2])) > zzmin and (float(t2[2])) <= zzmax:
           coord.append(t2)
           coord3.append(t2)
       if (float(t3[2])) > zzmin and (float(t3[2])) <= zzmax:
           coord.append(t3)
           coord3.append(t3)

    for j in range(2+1664,atoms+2,1):
       t1=aa[j+(i)*(atoms+2)].split()
       t2=np.array(t1[1:],float)
       t2[2]=t2[2]-mean

       if (float(t2[2])) > zzmin and (float(t2[2])) <= zzmax :
           coord2.append(t2)

       if (float(t2[2])) > 1.9 and (float(t2[2])) > zzmin and (float(t2[2])) <= zzmax :
           coord3.append(t2)

    sam=np.array(coord,float)
    sam12=np.array(coord2,float)
    sam13=np.array(coord3,float)

#########################################################################
    for j in range(len(sam)-1):
        a=np.array(sam[j],float)
        for k in range(j+1,len(sam)):
               b=np.array(sam[k],float)

               hh1=[]
               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb=np.array(b+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb-a)
                      hh1.append(h1)
   
               hh1=np.array(hh1,float)
               rrmin=np.amin(hh1)

               for x in range(bins):
                    if rrmin >= float(rmin+x*dx) and rrmin <  float(rmin+(x+1)*dx):
       
                        inside=rmin+ x*dx 
                        outside=rmin + (x+1) * dx
       
                        if float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           vol=(4/3)*math.pi*(outside**3-inside**3)
       
                        elif float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) > float(zzmax):
                           p=a[2]+outside-zzmax
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=a[2]+inside-zzmax
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           p=(-a[2]+outside)+zzmin
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=(-a[2]+inside)+zzmin
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) > float(zzmax):
                           vol=math.pi*h*(outside**2-inside**2)

                                                 
                        mo[i,x]=mo[i,x] + (1.0/(dx*vol))
                        del vol
        del a
    mo[i,:]=mo[i,:]*((vec1[0][0]*vec1[1][1]*h)/(0.5*len(sam)*(len(sam)-1)))

########################################################################
    for j in range(len(sam12)-1):
        a=np.array(sam12[j],float)
        for k in range(j+1,len(sam12)):
               b=np.array(sam12[k],float)

               hh1=[]
               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb=np.array(b+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb-a)
                      hh1.append(h1)
   
               hh1=np.array(hh1,float)
               rrmin=np.amin(hh1)

               for x in range(bins):
                    if rrmin >= float(rmin+x*dx) and rrmin <  float(rmin+(x+1)*dx):
       
                        inside=rmin+ x*dx 
                        outside=rmin + (x+1) * dx
       
                        if float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           vol=(4/3)*math.pi*(outside**3-inside**3)
       
                        elif float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) > float(zzmax):
                           p=a[2]+outside-zzmax
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=a[2]+inside-zzmax
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           p=(-a[2]+outside)+zzmin
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=(-a[2]+inside)+zzmin
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) > float(zzmax):
                           vol=math.pi*h*(outside**2-inside**2)

                                                 
                        mo1[i,x]=mo1[i,x] + (1.0/(dx*vol))
                        del vol
        del a
    mo1[i,:]=mo1[i,:]*((vec1[0][0]*vec1[1][1]*h)/(0.5*len(sam12)*(len(sam12)-1)))

########################################################################
    for j in range(len(sam13)-1):
        a=np.array(sam13[j],float)
        for k in range(j+1,len(sam13)):
               b=np.array(sam13[k],float)

               hh1=[]
               for k1 in range(-1,2):
                   for k2 in range(-1,2):

                      bb=np.array(b+k1*vec1[0,:]+k2*vec1[1,:],float)
                      h1=np.linalg.norm(bb-a)
                      hh1.append(h1)
   
               hh1=np.array(hh1,float)
               rrmin=np.amin(hh1)

               for x in range(bins):
                    if rrmin >= float(rmin+x*dx) and rrmin <  float(rmin+(x+1)*dx):
       
                        inside=rmin+ x*dx 
                        outside=rmin + (x+1) * dx
       
                        if float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           vol=(4/3)*math.pi*(outside**3-inside**3)
       
                        elif float(a[2] - outside) >= float(zzmin) and float(a[2] + outside) > float(zzmax):
                           p=a[2]+outside-zzmax
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=a[2]+inside-zzmax
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) <= float(zzmax):
                           p=(-a[2]+outside)+zzmin
                           volt=(4/3)*math.pi*(outside**3-inside**3)
                           volo=((1/3)*math.pi*p**2*(3*outside-p))
                           p=(-a[2]+inside)+zzmin
                           voli=((1/3)*math.pi*p**2*(3*inside-p))
                           vol=volt-(volo-voli)
                           del volt,voli,volo
       
                        elif float(a[2] - outside) < float(zzmin) and float(a[2] + outside) > float(zzmax):
                           vol=math.pi*h*(outside**2-inside**2)

                                                 
                        mo2[i,x]=mo2[i,x] + (1.0/(dx*vol))
                        del vol
        del a
    mo2[i,:]=mo2[i,:]*((vec1[0][0]*vec1[1][1]*h)/(0.5*len(sam13)*(len(sam13)-1)))

    


for x in range(bins):
        f=open(filename,'a')
        f.write("%.3f  \t %.3f \t %.3f \t %.3f \n" %(rmin+(x+1)*dx-dx/2,np.mean(np.array(mo[:,x]*dx)),np.mean(np.array(mo1[:,x]*dx)),np.mean(np.array(mo2[:,x]*dx))))
        f.close()



os.system('mv tempo %s '%filename2)
os.system('rm tempo')
print("--- %s seconds ---" % (time.time() - start_time))
