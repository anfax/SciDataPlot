# %% [markdown]
# # Plot the data of "ion1testold"

# %% [markdown]
#  Import Packets and Set Gengeric Information, parameters

# %%
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
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
  "font.family": "TimeNewroman",
  "font.size": 12,
})
plt.rcParams['figure.figsize'] = (8,6)
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
#from mpl_toolkits.mplot3d import Axes3D
for ifile in range(10,70,10):
    dir="D:\\doc\\data\\ion1testold\\DifferentDelatTimeOfPumpAndProbe\\dteq"+str(ifile)+"fs\\"
    #dir="D:\\doc\\data\\ion1testold\\t500t840\\44\\"
    #dir='D:\\doc\\data\\ion1testold\\NoAlignment\\41\\'
    print(dir)

    f=open(dir+"alog.dat",encoding="utf-8")
    print(f.read())
    levels=100
    figureDPI=1200
    figureType="jpeg"
    timeUnit="fs"
    ps2fs=1000
    scaleFactor=1000

    # %% [markdown]
    # Get the time points from the data

    # %%
    if os.path.exists(dir+'laser.dat'):
        TimeBegin =(min(np.loadtxt(dir+'Laser.dat')[:,0]))
        TimeEnd   =(max(np.loadtxt(dir+'Laser.dat')[:,0]))
    elif os.path.exists(dir+'laserField.dat'):
        TimeBegin =(min(np.loadtxt(dir+'Laserfield.dat')[:,0]))
        TimeEnd   =(max(np.loadtxt(dir+'Laserfield.dat')[:,0]))
    else:
        print('Cant find the data file')
    TimeTurn  =(min(np.loadtxt(dir+'ori_ali_1.dat')[:,0])) 
    dt=np.loadtxt(dir+'Laser.dat')[1,0]-np.loadtxt(dir+'Laser.dat')[0,0]
    print(dt)
    turnPoint =int((TimeTurn-TimeBegin)/dt)
    if TimeEnd<5:
        print('The unit of time is ps! Turn to fs with times ps2fs(*1000))')
        TimeBegin = TimeBegin*scaleFactor
        TimeEnd = TimeEnd*scaleFactor
        TimeTurn = TimeTurn*scaleFactor


    print(turnPoint)
    print(' Begin time:',TimeBegin,timeUnit+'\n End time:',TimeEnd,timeUnit+' \n Turn time:',TimeTurn,timeUnit)

    # %% [markdown]
    # Plot absorption of the dimsension of the internuclear distance

    # %%
    if os.path.exists(dir+'absb.dat'):
        data=np.loadtxt(dir+'Absb.dat') #get data form dir+'absb.dat'
    else:
        data=np.loadtxt(dir+'Absorption.dat')
    x=data[:,0]
    y1=data[:,1]
    plt.xlabel("$\t{R}$ (a.u.) ")
    plt.ylabel("Absorptivity")
    #x=x
    #y=y1
    #plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.95,"(a)")
    plt.plot(x,y1,'k-')
    #plt.savefig(dir+"Absorption."+figureType,bbox_inches="tight",transparent=True,dpi=figureDPI)
    ###plt.show()

    # %% [markdown]
    # Plot potential energy of electric states

    # %%
    if os.path.exists(dir+'pott.dat'):
        data=np.loadtxt(dir+"Pott.dat")
    else:
        data=np.loadtxt(dir+"PotentialEnergy.dat")

    x=data[:,0]
    y1=data[:,1]
    y2=data[:,2]
    y3=data[:,3]
    plt.xlabel("$\t{R}$ (a.u.) ")
    plt.ylabel("Energy (a.u.)")
    plt.plot(x,y1,'k-',x,y2,'r-.',x,y3,'b--')
    plt.legend(['$X^1\Sigma^+$','$A^1 \Sigma ^+$','$X^2 \Sigma ^+$'],loc=(0.8,0.75))
    #plt.savefig(dir+"pott."+figureType,bbox_inches="tight",transparent=True,dpi=figureDPI)

    # %% [markdown]
    # Plot Initial wave function 

    # %%
    import scipy.ndimage
    plt.figure(figsize=(8,6))
    if os.path.exists(dir+"wave2d.dat"):
        DataAng =np.loadtxt(dir+"wave2d.dat")
    else:   
        DataAng =np.loadtxt(dir+"InitialWavePacket.dat")
    #DataAng=scipy.ndimage.zoom(DataAng,1)
    #plt.style.use('_mpl-gallery-nogrid')
    x=DataAng[:,0]
    y=DataAng[:,1]
    z=DataAng[:,2]
    plt.xlim(-5, 5)
    plt.ylim(-5, 5)
    ax=plt.tricontourf(x,y,z,levels,cmap='jet')

    #interpolation='spline16'
    plt.colorbar()
    plt.xlabel("$\tR$ (a.u.)")
    plt.ylabel("$\tR$ (a.u.)")
    #plt.savefig(dir+"InitialWavePacket."+figureType,bbox_inches = 'tight',transparent=True,dpi=figureDPI)
    ##plt.show()

    # %% [markdown]
    # Plot the electronic field of the lasers

    # %%
    if os.path.exists(dir+"Laser.dat"):
        data=np.loadtxt(dir+"Laser.dat")
    else:
        data=np.loadtxt(dir+"LaserField.dat")

    x =data[:,0]*scaleFactor
    y1=data[:,1]
    x2=data[turnPoint:,0]*scaleFactor
    y2=data[turnPoint:,2]
    y3=data[turnPoint:,3]
    import matplotlib.gridspec as gridspec
    fig = plt.figure(tight_layout=True)
    gs = gridspec.GridSpec(2, 2)
    ax = fig.add_subplot(gs[0,:])
    ax.plot(x,y1,'k-')
    x=x
    y=y1
    plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.95,"(a)")
    ax.set_ylabel('Intensity (a.u.)')
    ax.set_xlabel('Time (fs)')
    for i in range(2):
        ax = fig.add_subplot(gs[1, i])
        if i==0:
            ax.plot(x2,y2,'r-')
            x=x2
            y=y2
            plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.95,"(b)")
        if i==1:
            ax.plot(x2,y3,'b-')
            x=x2
            y=y3
            plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.95,"(c)")
        ax.set_ylabel('Intensity (a.u.)')
        ax.set_xlabel('Time (fs)')
        if i == 0:
            for tick in ax.get_xticklabels():
                tick.set_rotation(55)
    fig.align_labels()  # same as fig.align_xlabels(); fig.align_ylabels()
    ##plt.show()

    # %%
    if os.path.exists(dir+"Laser.dat"):
        data=np.loadtxt(dir+"Laser.dat")
    else:
        data=np.loadtxt(dir+"LaserField.dat")

    x=data[:,0]*scaleFactor
    y1=data[:,1]
    y2=data[:,2]
    y3=data[:,3]

    plt.subplot(3,1,1)
    #plt.grid(False)
    x=x
    y=y1
    plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.9,"(a)")
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel("Intensity (a.u.)")
    plt.xlim(TimeBegin,TimeEnd)
    plt.plot(x,y1,'k-')

    plt.subplot(3,1,2)
    #plt.grid(False)
    #plt.title("(b)",loc="left")
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel("Intensity (a.u.)")
    plt.xlim(TimeTurn,TimeEnd)
    plt.plot(x,y2,'k-')
    x=x
    y=y2
    plt.text(TimeTurn+(TimeEnd-TimeTurn)*0.95,min(y)+(max(y)-min(y))*0.9,"(b)")

    plt.subplot(3,1,3)
    #plt.grid(False)
    x=x
    y=y3
    plt.text(TimeTurn+(TimeEnd-TimeTurn)*0.95,min(y)+(max(y)-min(y))*0.9,"(c)")

    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel("Intensity (a.u.)")
    plt.xlim(TimeTurn,TimeEnd)
    plt.plot(x,y3,'k-')

    # %% [markdown]
    # Plot the Potential energy and dipole moment

    # %%
    plt.subplot(1,2,1)
    if os.path.exists(dir+"pott.dat"):
        data=np.loadtxt(dir+"Pott.dat")
    else:
        data=np.loadtxt(dir+"PotentialEnergy.dat")

    x=data[:,0]
    y1=data[:,1]
    y2=data[:,2]
    y3=data[:,3]
    #plt.grid(False)
    x=x
    y=y3
    plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.95,"(a)")
    plt.xlabel('$\\textit{R}$ (a.u.)')
    plt.ylabel("Intensity (a.u.)")
    plt.plot(x,y1,'k-',x,y2,'r-.',x,y3,'b--')
    plt.legend(['$X^1\Sigma^+$','$A^1 \Sigma ^+$','$X^2 \Sigma ^+$'],loc=(0.6,0.75))
    plt.subplot(1,2,2)
    if os.path.exists(dir+"Dipole.dat"):
        data=np.loadtxt(dir+"Dipole.dat")
    else:
        data=np.loadtxt(dir+"DipoleMoment.dat")

    x=data[:,0]
    y=data[:,2]
    plt.text(min(x)+(max(x)-min(x))*0.95,min(y)+(max(y)-min(y))*0.9,"(b)")
    plt.xlabel("$\\textit{R}$  (a.u.)")
    plt.ylabel("Intensity (a.u.)")
    plt.plot(data[:,0],data[:,1],'k-',data[:,0],data[:,2],'r-.',data[:,0],data[:,3],'b--')
    plt.legend(["$\mu_{X^1\Sigma^+ - X^1\Sigma^+} $","$\mu_{A^1\Sigma^+ - A^1\Sigma^+} $","$\mu_{A^1\Sigma^+ - X^2\Sigma^+} $"],loc=(0.5,0.08))
    plt.tight_layout()
    #plt.savefig(dir+"PotentialEnergyAndDipoleMent."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()


    # %% [markdown]
    # Plot orientation and alignment of the groud state

    # %%
    if os.path.exists(dir+"cos1.dat"):
        data=np.loadtxt(dir+"cos1.dat")
    else:
        data=np.loadtxt(dir+"orientationAndAlignment.dat")

    x=data[:,0]*scaleFactor
    y1=data[:,1]
    y2=data[:,2]
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Time ('+timeUnit+')')
    ax1.set_ylabel('$\\langle{\\rm  cos} \\theta \\rangle$', color=color)
    ax1.plot(x, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('$\\langle{\\rm cos^2} \\theta \\rangle$', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y2,'--', color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.savefig(dir+"OrientationAndAlignment."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()

    # %% [markdown]
    # Plot evolution of angle-resolved wave packets

    # %%
    plt.figure(figsize=(12,9))
    if os.path.exists(dir+"vgr_ang.dat"):
        plt.subplot(2,2,1)
        DataAng =np.loadtxt(dir+"vgr_ang.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(a)",loc='left')
        plt.xlim(TimeBegin, TimeEnd )
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,2)
        DataAng =np.loadtxt(dir+"Exc_ang.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(b)",loc='left')
        plt.xlim(TimeTurn,TimeEnd)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,3)
        DataAng =np.loadtxt(dir+"Ion_ang.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.title("(c)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,4)
        DataAng =np.loadtxt(dir+"TotalAngDis.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(d)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
    elif so.path.exists(dir+"GroAngWave.dat"):
        plt.subplot(2,2,1)
        DataAng =np.loadtxt(dir+"GroAngWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(a)",loc='left')
        plt.xlim(TimeBegin, TimeEnd )
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,2)
        DataAng =np.loadtxt(dir+"ExcAngWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(b)",loc='left')
        plt.xlim(TimeTurn,TimeEnd)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,3)
        DataAng =np.loadtxt(dir+"IonAngWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.title("(c)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
        plt.subplot(2,2,4)
        DataAng =np.loadtxt(dir+"TotalAngDis.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(d)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$\\theta$ (degrees)")
    else :
        print("No data available")
    plt.savefig(dir+"WaveAngDis."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()


    # %% [markdown]
    # Plot evolution of internuclear distance-resolved wave packages

    # %%
    plt.figure(figsize=(12,9))
    if os.path.exists(dir+"vgr_rad.dat"):     
        plt.subplot(2,2,1)
        DataAng =np.loadtxt(dir+"vgr_rad.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(a)",loc='left')
        plt.xlim(TimeTurn, TimeEnd )
        plt.ylim(1.75,10.0)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,2)
        DataAng =np.loadtxt(dir+"Exc_rad.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(b)",loc='left')
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,3)
        DataAng =np.loadtxt(dir+"Ion_rad.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.title("(c)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,4)
        DataAng =np.loadtxt(dir+"TotalRadDis.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.title("(d)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
    elif os.path.exists(dir+"GroRadWave.dat"):
        plt.subplot(2,2,1)
        DataAng =np.loadtxt(dir+"GroRadWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(a)",loc='left')
        plt.xlim(TimeTurn, TimeEnd )
        plt.ylim(1.75,10.0)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,2)
        DataAng =np.loadtxt(dir+"ExcRadWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.title("(b)",loc='left')
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,3)
        DataAng =np.loadtxt(dir+"IonRadWave.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.title("(c)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
        plt.subplot(2,2,4)
        DataAng =np.loadtxt(dir+"TotalRadDis.dat")
        #plt.style.use('_mpl-gallery-nogrid')
        x=DataAng[:,0]*scaleFactor
        y=DataAng[:,1]
        z=DataAng[:,2]
        plt.xlim(TimeTurn,TimeEnd)
        plt.ylim(1.75,10.0)
        plt.title("(d)",loc='left')
        plt.tricontourf(x,y,z,levels,cmap='jet')
        plt.colorbar()
        plt.xlabel("Time ("+timeUnit+")")
        plt.ylabel("$R$ (a.u.)")
    else:
        print("No rad-resovled wave data available")
    plt.savefig(dir+"WaveRadDis."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()


    # %% [markdown]
    # Plot population of electronic states

    # %%
    if os.path.exists(dir+"popu.dat"):
        data=np.loadtxt(dir+"Popu.dat")
    elif os.path.exists(dir+"PopulationOfState.dat"):
        data = np.loadtxt(dir+"PopulationOfState.dat")
    else:
        print("No PopulationOfState dataset found.")
    plt.xlim(TimeTurn,TimeEnd)
    plt.plot(data[:,0]*scaleFactor,data[:,1],'k-',data[:,0]*scaleFactor,data[:,2],'r-',data[:,0]*scaleFactor,1-data[:,1]-data[:,2],'b-')
    plt.legend(["Gro","Exc","Ion"],loc=(0.83,0.79))
    plt.xlabel("Time ("+timeUnit+")")
    plt.ylabel("Population")
    plt.savefig(dir+"PopulationOfState."+figureType,dpi=figureDPI,bbox_inches="tight")

    # %% [markdown]
    # Plot population of vibrational states

    # %%
    plt.figure(figsize=(12,9))
    plt.subplot(2,1,1)
    DataPop =np.loadtxt(dir+"p_vgr_v.dat")
    #plt.style.use('_mpl-gallery-nogrid')
    x=DataPop[:,0]*scaleFactor
    y=DataPop[:,1]
    z=DataPop[:,2]
    plt.xlim(TimeBegin,TimeEnd)
    plt.ylim(0,5)
    plt.title("(a)",loc='left')
    plt.tricontourf(x,y,z,cmap='jet')
    plt.colorbar()
    plt.xlabel("Time ("+timeUnit+")")
    plt.ylabel("Vibrational quantum number v")

    plt.subplot(2,1,2)
    DataPop =np.loadtxt(dir+"p_exc_v.dat")
    #plt.style.use('_mpl-gallery-nogrid')
    x=DataPop[:,0]*scaleFactor
    y=DataPop[:,1]
    z=DataPop[:,2]
    plt.xlim(TimeTurn,TimeEnd)
    plt.ylim(0,20)
    plt.title("(b)",loc='left')
    plt.tricontourf(x,y,z)
    plt.colorbar()
    plt.xlabel("Time ("+timeUnit+")")
    plt.ylabel("Vibrational quantum number v")
    plt.savefig(dir+"P_v."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()

    # %%
    plt.figure(figsize=(12,9))
    plt.subplot(2,1,1)
    DataPop =np.loadtxt(dir+"p_vgr_v.dat")
    #plt.style.use('_mpl-gallery-nogrid')
    x=DataPop[:,0]*scaleFactor
    y=DataPop[:,1]
    z=DataPop[:,2]
    ny=int((max(y)-min(y))/(y[2]-y[1]))+1
    nx=int((max(x)-min(x))/(x[ny]-x[0]))+1
    zMesh=np.zeros((ny,nx))
    for i in range(1,nx):
        for j in range(1,ny):
            zMesh[j-1,i-1]=z[(i-1)*ny+j-1]
    print('nx= ',nx,' ny= ',ny)
    print('xMax= ',max(x),' xMin= ',min(x),' yMax= ',max(y),' yMin= ',min(y))
    print('x[50]',x[50])
    print(x[0])
    print(zMesh)
    xMesh=np.linspace(min(x),max(x),nx)
    yMesh=np.linspace(min(y),max(y),ny)
    #xx,yy,zz=np.meshgrid(xMesh,yMesh,zMesh)
    plt.pcolormesh(xMesh,yMesh,zMesh,cmap='jet')
    plt.ylim(-0.5,5.5)
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel('Vibrational quantum state')
    plt.colorbar()
    plt.subplot(2,1,2)
    DataPop =np.loadtxt(dir+"p_exc_v.dat")
    #plt.style.use('_mpl-gallery-nogrid')
    x=DataPop[:,0]*scaleFactor
    y=DataPop[:,1]
    z=DataPop[:,2]
    ny=int((max(y)-min(y))/(y[2]-y[1]))+1
    nx=int((max(x)-min(x))/(x[ny]-x[0]))+1
    zMesh=np.zeros((ny,nx))
    for i in range(1,nx):
        for j in range(1,ny):
            zMesh[j-1,i-1]=z[(i-1)*ny+j-1]
    print('nx= ',nx,' ny= ',ny)
    print('xMax= ',max(x),' xMin= ',min(x),' yMax= ',max(y),' yMin= ',min(y))
    print('x[50]',x[50])
    print(x[0])
    print(zMesh)
    xMesh=np.linspace(min(x),max(x),nx)
    yMesh=np.linspace(min(y),max(y),ny)
    #xx,yy,zz=np.meshgrid(xMesh,yMesh,zMesh)
    plt.pcolormesh(xMesh,yMesh,zMesh,cmap='jet')
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel('Vibrational quantum state')
    plt.ylim(-0.5,20.5)
    plt.colorbar()

    # %% [markdown]
    # 

    # %% [markdown]
    # Plot orientation and alignment of the electronic states

    # %%
    data=np.loadtxt(dir+"ori_ali_1.dat")
    x=data[:,0]*scaleFactor
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
    plt.savefig(dir+"GroundAlignmentAndOrientation."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()

    # %%
    data=np.loadtxt(dir+"ori_ali_2.dat")
    x=data[:,0]*scaleFactor
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
    plt.savefig(dir+"ExcitedAlignmentAndOrientation."+figureType,bbox_inches = 'tight',dpi=figureDPI)
    ##plt.show()

    # %%
    import os
    os.startfile(dir)

