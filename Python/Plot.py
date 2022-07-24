 # %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
plt.rcParams['ytick.right']  =plt.rcParams['xtick.top'] =True
xminorLocator=MultipleLocator(2)
#plt.rcParams['set_minor_locator']=xminorLocator
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["TimeNewroman"]})
# for Palatino and other serif fonts use:
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})
# It's also possible to use the reduced notation by directly setting font.family:
plt.rcParams.update({
  "text.usetex": True,
  "font.family": "TimeNewroman"
})
#from mpl_toolkits.mplot3d import Axes3D
dir="D:\\DataOfPro\\"
plt.rcParams['figure.figsize'] = (8,6)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
f=open(dir+"alog.dat",encoding="utf-8")
print(f.read())
import os
os.startfile(dir)

# %%
TimeBegin =int(min(np.loadtxt(dir+'LaserField.dat')[:,0]))
TimeEnd =int(max(np.loadtxt(dir+'LaserField.dat')[:,0]))
TimeTurn =int(min(np.loadtxt(dir+'PopulationOfState.dat')[:,0]))
print(' Begin time:',TimeBegin,'fs \n End time:',TimeEnd, 'fs \n Turn time:',TimeTurn,'fs')


# %%
data=np.loadtxt(dir+'Absorption.dat')
x=data[:,0]
y1=data[:,1]
plt.xlabel("$\t{R}$ (a.u.) ")
plt.ylabel("Absorptivity")
plt.plot(x,y1,'k-')
plt.savefig(dir+"Absorption.png",bbox_inches="tight",transparent=True,dpi=600)


# %%

data=np.loadtxt(dir+"PotentialEnergy.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]
y3=data[:,3]
plt.xlabel("$\t{R}$ (a.u.) ")
plt.ylabel("Energy (a.u.)")
plt.plot(x,y1,'k-',x,y2,'r-.',x,y3,'b--')
plt.legend(['$X^1\Sigma^+$','$A^1 \Sigma ^+$','$X^2 \Sigma ^+$'],loc=(0.8,0.75))
plt.savefig(dir+"pott.png",bbox_inches="tight",transparent=True,dpi=600)

# %%

import scipy.ndimage
DataAng =np.loadtxt(dir+"InitialWavePacket.dat")
#DataAng=scipy.ndimage.zoom(DataAng,1)
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
plt.xlim(-5, 5)
plt.ylim(-5, 5)
ax=plt.tricontourf(x,y,z)
#interpolation='spline16'
plt.colorbar()
plt.xlabel("$\tR$ (a.u.)")
plt.ylabel("$\tR$ (a.u.)")
plt.savefig(dir+"InitialWavePacket.jpeg",bbox_inches = 'tight',transparent=True,dpi=600)
plt.show()

# %%
data=np.loadtxt(dir+"LaserField.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]
y3=data[:,3]
#plt.grid(False)
plt.xlabel('Time (fs)')
plt.ylabel("Intensity (a.u.)")
plt.xlim(TimeBegin, TimeEnd)
plt.plot(x,y1,'k-',x,y2,'r-',x,y3,'b-')
plt.legend(["Align","Pump","Probe"],loc=(0.75,0.7))
plt.savefig(dir+"LaserFiled.jpeg",bbox_inches = 'tight',transparent=True,dpi=600)
plt.show()

# %%
data=np.loadtxt(dir+"LaserField.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]
y3=data[:,3]
data1=np.loadtxt(dir+"laser_fre1.dat")
data2=np.loadtxt(dir+"laser_fre2.dat")
data3=np.loadtxt(dir+"laser_fre3.dat")
plt.subplot(2,3,1)
#plt.grid(False)
plt.title("(a)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Intensity (a.u.)")
plt.xlim(TimeBegin,TimeEnd)
plt.plot(x,y1,'k-')

plt.subplot(2,3,2)
#plt.grid(False)
plt.title("(b)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Intensity (a.u.)")
plt.xlim(TimeTurn,TimeEnd)
plt.plot(x,y2,'k-')

plt.subplot(2,3,3)
#plt.grid(False)
plt.title("(c)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Intensity (a.u.)")
plt.xlim(TimeTurn,TimeEnd)
plt.plot(x,y3,'k-')

plt.subplot(2,3,4)
#plt.grid(False)
plt.title("(d)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Frequency (a.u.)")
#plt.xlim(TimeTurn,TimeEnd)
plt.plot(data1[:,0],data1[:,1],'k-')

plt.subplot(2,3,5)
#plt.grid(False)
plt.title("(e)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Frequency (a.u.)")
#plt.xlim(TimeTurn,TimeEnd)
plt.plot(data2[:,0],data2[:,1],'k-')

plt.subplot(2,3,6)
#plt.grid(False)
plt.title("(f)",loc="left")
plt.xlabel('Time (fs)')
plt.ylabel("Frequency (a.u.)")
#plt.xlim(TimeTurn,TimeEnd)
plt.plot(data3[:,0],data3[:,1],'k-')

plt.tight_layout()
plt.savefig(dir+"LaserFileds.jpeg",bbox_inches = 'tight',transparent=True,dpi=600)


# %%

plt.subplot(1,2,1)
data=np.loadtxt(dir+"PotentialEnergy.dat")
print (dir+"ok")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]
y3=data[:,3]
#plt.grid(False)
plt.title("(a)",loc='left')
plt.xlabel('$\\textit{R}$ (a.u.)')
plt.ylabel("Intensity (a.u.)")
plt.plot(x,y1,'k-',x,y2,'r-.',x,y3,'b--')
plt.legend(['$X^1\Sigma^+$','$A^1 \Sigma ^+$','$X^2 \Sigma ^+$'],loc=(0.6,0.75))
plt.subplot(1,2,2)
data2=np.loadtxt(dir+"DipoleMoment.dat")
plt.title("(b)",loc='left')
plt.xlabel("$\\textit{R}$  (a.u.)")
plt.ylabel("Intensity (a.u.)")
plt.plot(data2[:,0],data2[:,1],'k-',data2[:,0],data2[:,2],'r--',data2[:,0],data2[:,3],'b-.')
plt.legend(["$\mu_{X^1\Sigma^+ - X^1\Sigma^+} $","$\mu_{A^1\Sigma^+ - A^1\Sigma^+} $","$\mu_{A^1\Sigma^+ - X^2\Sigma^+} $"],loc=(0.5,0.08))
plt.tight_layout()
plt.savefig(dir+"PotentialEnergyAndDipoleMent.jpeg",bbox_inches = 'tight',dpi=600)
#plt.show()


# %%
data=np.loadtxt(dir+"OrientationAndAlignment.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (fs)')
ax1.set_ylabel('$\\langle{\\rm  cos} \\theta \\rangle$', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('$\\langle{\\rm cos^2} \\theta \\rangle$', color=color)  # we already handled the x-label with ax1
ax2.plot(x, y2,'--', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(dir+"OrientationAndAlignment.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
data=np.loadtxt(dir+"ori_ali_1.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (fs)')
ax1.set_ylabel('$\\langle{\\rm cos} \\theta \\rangle$', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('$\\langle {\\rm cos^2} \\theta \\rangle$', color=color)  # we already handled the x-label with ax1
ax2.plot(x, y2,'--', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(dir+"GroundAlignmentAndOrientation.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
data=np.loadtxt(dir+"ori_ali_2.dat")
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Time (fs)')
ax1.set_ylabel('$\\langle {\\rm cos} \\theta \\rangle$', color=color)
ax1.plot(x, y1, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('$\\langle {\\rm cos^2} \\theta \\rangle$', color=color)  # we already handled the x-label with ax1
ax2.plot(x, y2,'--', color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.savefig(dir+"ExcitAlignmentAndOrientation.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
plt.figure(figsize=(12,9))
plt.subplot(2,2,1)
DataAng =np.loadtxt(dir+"GroAngWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 50)
plt.title("(a)",loc='left')
plt.xlim(TimeBegin, TimeEnd )
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (Degrees)")
plt.subplot(2,2,2)
DataAng =np.loadtxt(dir+"ExcAngWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 100)
plt.title("(b)",loc='left')
plt.xlim(TimeTurn,TimeEnd)
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (Degrees)")
plt.subplot(2,2,3)
DataAng =np.loadtxt(dir+"IonAngWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
plt.xlim(TimeTurn,TimeEnd)
levels=np.linspace(z.min(), z.max(), 30)
plt.title("(c)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (Degrees)")
plt.subplot(2,2,4)
DataAng =np.loadtxt(dir+"TotalAngDis.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 30)
plt.title("(d)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (Degrees)")
plt.savefig(dir+"WaveAngDis.png",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
plt.figure(figsize=(12,9))
plt.subplot(2,2,1)
DataAng =np.loadtxt(dir+"GroRadWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 50)
plt.title("(a)",loc='left')
plt.xlim(TimeBegin+5, TimeEnd-5 )
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.subplot(2,2,2)
DataAng =np.loadtxt(dir+"ExcRadWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 100)
plt.title("(b)",loc='left')
plt.xlim(TimeTurn+5,TimeEnd-5)
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.subplot(2,2,3)
DataAng =np.loadtxt(dir+"IonRadWave.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
plt.xlim(TimeTurn+5,TimeEnd-5)
levels=np.linspace(z.min(), z.max(), 30)
plt.title("(c)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.subplot(2,2,4)
DataAng =np.loadtxt(dir+"TotalRadDis.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataAng[:,0]
y=DataAng[:,1]
z=DataAng[:,2]
levels=np.linspace(z.min(), z.max(), 30)
plt.title('(d)',loc='left')
ax=plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.savefig(dir+"WaveRadDis.png",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
data=np.loadtxt(dir+"PopulationOfState.dat")
plt.xlim(TimeTurn,TimeEnd)
ax=plt.plot(data[:,0],data[:,1],'k-',data[:,0],data[:,2],'r-',data[:,0],1-data[:,1]-data[:,2],'b-')
plt.legend(["Gro","Exc","Ion"],loc=(0.8,0.7))
plt.xlabel("Time (fs)")
plt.ylabel("Population")
plt.savefig(dir+"popu.jpeg",dpi=600,bbox_inches="tight")

# %%
plt.figure(figsize=(12,9))
plt.subplot(2,1,1)
DataPop =np.loadtxt(dir+"p_vgr_v.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(a)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Vibrational quantum number v")

plt.subplot(2,1,2)
DataPop =np.loadtxt(dir+"p_exc_v.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(b)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Vibrational quantum number v")
plt.savefig(dir+"P_v.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
plt.figure(figsize=(12,9))
plt.subplot(2,1,1)
DataPop =np.loadtxt(dir+"qua_int_ang.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(a)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (degree)")

plt.subplot(2,1,2)
DataPop =np.loadtxt(dir+"qua_int_rad.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(b)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.savefig(dir+"qua_int.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%
plt.figure(figsize=(12,9))
plt.subplot(2,1,1)
DataPop =np.loadtxt(dir+"Ang_dt.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(a)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("Angle (degree)")

plt.subplot(2,1,2)
DataPop =np.loadtxt(dir+"Rad_dt.dat")
#plt.style.use('_mpl-gallery-nogrid')
x=DataPop[:,0]
y=DataPop[:,1]
z=DataPop[:,2]
levels=np.linspace(z.min(), z.max())
plt.ylim(0,20)
plt.title("(b)",loc='left')
plt.tricontourf(x,y,z)
plt.colorbar()
plt.xlabel("Time (fs)")
plt.ylabel("$\tR$ (a.u.)")
plt.savefig(dir+"qua_int.jpeg",bbox_inches = 'tight',dpi=600)
plt.show()

# %%



