# -*- coding: utf-8 -*-
"""
Created on Mon Dec  3 21:41:36 2018

@author: unmesh
"""
import numpy as np
import matplotlib 
matplotlib.use('Agg')
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D # This import has side effects required for the kwarg projection='3d' in the call to fig.add_subplot
import matplotlib.pyplot as plt
import random
import sys
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#from sklearn.neighbors.kde import KernelDensity
#from scipy.stats import gaussian_kde
#from scipy.stats import kurtosis, skew


import os

os.system('rm log_1.dat')
###################################################################################
tot=np.int(sys.argv[1])
fold=np.int(sys.argv[2])
beads=np.array(str(sys.argv[3]).split(','),int)
sec=str(sys.argv[4]).split(',')
temp=np.array(str(sys.argv[5]).split(','),int)
dim=np.int(sys.argv[6])
###################################################################################


def files(res2):
        f=open(res2,'r')
        a=f.readlines()
        f.close
        
        coord=[]
        for i in range(0,len(a)):
            x=a[i].split()
            coord.append(x)
        coord=np.array(coord,float)
        return (coord)

def cut(xx0,fol,bead,count):
        dd=np.split(xx0,bead)
        s=[]
        for i in range (len(dd[0])):
            for j in range (bead):
               s.append(dd[j][i])
        s=np.array(s,float)
        del dd
        return (s)



#############1.histogram########################################## 
new_colour = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f','#bcbd22', '#17becf']

h=np.array(temp)
hh=np.array([0])
sec2=np.concatenate((hh,h))


fig = plt.figure()

min01=np.zeros((tot),float)
max01=np.zeros((tot),float)
mean01=np.zeros((tot),float)
std01=np.zeros((tot),float)

for i in range(1,tot+1):
    res2="dell{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,1]-coord[:,2]
    x0=np.split(xxx0,fold)
    kkk=np.zeros((fold,100),float)


    xedges=np.histogram(x0[0], bins=100,range=[1.5, 5.5], density=True)[1]
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    dx=(xedges[1]-xedges[0])


    mean=0
    std=0
    mmax=0
    mmin=0
    for j in range(fold):
        ggg=np.histogram(x0[j], bins=100,range=[1.5, 5.5], density=True)[0]
        kkk[j]=ggg
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        mmax=mmax+np.amax(x0[j])/fold
        mmin=mmin+np.amin(x0[j])/fold

    
    gg=np.mean(kkk,axis=0)
    pp=np.std(kkk,axis=0)

#    plt.errorbar(xcenters,gg,yerr=pp,markersize=1, capsize=2,lw=0.5,fmt='--o',color=new_colour[i-1],mfc='white')
    plt.plot(xcenters,gg-np.amin(gg), '-o', markersize=2, lw=2  ,color=new_colour[i-1],mfc='white',label=sec[i-1])

    plt.ylabel('Free energy (meV)',size=10)
    plt.xlabel(r'$\delta_o $ (Å)',size=10)
    plt.legend(prop={'size': 6},loc=9, bbox_to_anchor=(0.6,0.7))
    plt.xticks(np.arange(-1.0,1.1,0.2),size=10)
    plt.yticks(size=10)
    plt.xlim(-1.0,1.0)
    plt.ylim(-2,100)

    min01[i-1]=mmin
    max01[i-1]=mmax
    mean01[i-1]=mean
    std01[i-1]=std

    del x0

    res2="ddel{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,3]
    x0=np.split(xxx0,fold)
    kkk=np.zeros((fold,100),float)


    xedges=np.histogram(x0[0], bins=100,range=[1.5, 5.5], density=True)[1]
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    dx=(xedges[1]-xedges[0])


    mean=0
    std=0
    mmax=0
    mmin=0
    for j in range(fold):
        ggg=np.histogram(x0[j], bins=100,range=[1.5, 5.5], density=True)[0]
        kkk[j]=ggg
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        mmax=mmax+np.amax(x0[j])/fold
        mmin=mmin+np.amin(x0[j])/fold

    
    gg=np.mean(kkk,axis=0)
    pp=np.std(kkk,axis=0)


    for iii in range(len(gg)):
        print (xcenters[iii],gg[iii]-np.amin(gg),pp[iii])
    print ('&')

    ax1 = fig.add_subplot(211)

    if  i==1:
        plt.plot(xcenters,gg-np.amin(gg), '--or', markersize=2, lw=2  ,mfc='white',label=sec[i-1]+' :BOMD')
    elif  i==2:
        plt.plot(xcenters,gg-np.amin(gg), '--xr', markersize=2, lw=2  ,mfc='white',label=sec[i-1]+' :BOMD')


    min01[i-1]=mmin
    max01[i-1]=mmax
    mean01[i-1]=mean
    std01[i-1]=std
  
   print (sec[i-1],mmin,mmax,mean,std)

    del x0


plt.axvline(x=0.0, color = 'k',linewidth=1.0, linestyle = '--')

####################################################################################################################################
min01=np.zeros((tot),float)
max01=np.zeros((tot),float)
mean01=np.zeros((tot),float)
std01=np.zeros((tot),float)

for i in range(1,tot+1):
    res2="ddell{}".format(i)
    coord=files(res2)

    fold=1
    xxx0=coord[:,3]
    xx0=cut(xxx0,fold,beads[i-1],i)
    x0=np.split(xx0,fold)
    kkk=np.zeros((fold,100),float)


    xedges=np.histogram(x0[0], bins=100,range=[1.5, 5.5], density=True)[1]
    xcenters = (xedges[:-1] + xedges[1:]) / 2
    dx=(xedges[1]-xedges[0])


    mean=0
    std=0
    mmax=0
    mmin=0
    for j in range(fold):
        ggg=np.histogram(x0[j], bins=100,range=[1.5, 5.5], density=True)[0]
        kkk[j]=ggg
        mean=mean+np.mean(x0[j])/fold
        std=std+np.std(x0[j])/fold
        mmax=mmax+np.amax(x0[j])/fold
        mmin=mmin+np.amin(x0[j])/fold

    
    gg=np.mean(kkk,axis=0)
    pp=np.std(kkk,axis=0)


    if  i==1:
        plt.plot(xcenters,gg-np.amin(gg), '--or', markersize=2, lw=2  ,mfc='white',label='PIGLET')
    elif  i==2:
        plt.plot(xcenters,gg-np.amin(gg), '--xr', markersize=2, lw=2  ,mfc='white',label='PIGLET')

    plt.ylabel('prob. density',size=10)
    plt.xlabel(r'$d_{C\cdots O}$ (Å)',size=10)
    plt.legend(prop={'size': 6},loc=0,ncol=2) #bbox_to_anchor=(0.75,1.0))
    plt.xticks(np.arange(2.0,5.0,0.4),size=10)
    plt.yticks(size=10)
    plt.xlim(2.8,4.2)
#    plt.ylim(-2,100)

    min01[i-1]=mmin
    max01[i-1]=mmax
    mean01[i-1]=mean
    std01[i-1]=std

    print (sec[i-1],mmin,mmax,mean,std)

    del x0




#########################################################################################################################################
plt.subplots_adjust(wspace=0.4,hspace=0.4)
plt.savefig("fig_temp_1_1.jpg", dpi=500, bbox_inches = 'tight',    pad_inches = 0.1)
fig.savefig('fig_temp_1_1.pdf')
#plt.show()