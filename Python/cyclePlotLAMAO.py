print('Working directory',dir)
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
import os
from matplotlib import ticker
plt.rcParams['ytick.right']  =plt.rcParams['xtick.top'] =True
xminorLocator=MultipleLocator(2)

def cm2inch(value):
    return value/2.54

plt.rcParams['figure.figsize'] = (cm2inch(8), cm2inch(6.5))
plt.rcParams['lines.linewidth'] = 1
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.labelsize'] = 6
plt.rcParams['ytick.labelsize'] = 6
plt.rcParams['legend.fontsize'] =6

from matplotlib import rcParams
config = {
    "text.usetex": False,
    "font.family":'serif',
    # "font.family":'stix',
    "font.size": 8,
    "mathtext.fontset":'stix',
    # "font.serif": ['SimSun'],
}
rcParams.update(config)

maxlist=[]
from mpl_toolkits.mplot3d import Axes3D
import numpy 
def setlabel(ax, label, loc=2, borderpad=0.6, **kwargs):
    legend = ax.get_legend()
    if legend:
        ax.add_artist(legend)
    line, = ax.plot(numpy.NaN,numpy.NaN,color='none',label=label,fillstyle='full')
    label_legend = ax.legend(handles=[line],
                             loc=[0.85,0.85],
                             handlelength=0.0,
                             handleheight=0.0,
                             handletextpad=0.0,
                             borderaxespad=0.0,
                             borderpad=borderpad,
                             frameon=False,
                             shadow=True,
                             facecolor='gray',
                             prop={'weight':'bold','size':8},
                             **kwargs)
    label_legend.remove()
    ax.add_artist(label_legend)
    line.remove()
def setlabelm(ax, label, loc, borderpad=0.6, **kwargs):
    legend = ax.get_legend()
    if legend:
        ax.add_artist(legend)
    line, = ax.plot(numpy.NaN,numpy.NaN,color='none',label=label)
    label_legend = ax.legend(handles=[line],
                             loc=loc,
                             handlelength=0,
                             handleheight=0,
                             handletextpad=0,
                             borderaxespad=0,
                             borderpad=borderpad,
                             frameon=False,
                             shadow=True,
                             facecolor='gray',
                             prop={'weight':'bold','size':8},
                             **kwargs)
    label_legend.remove()
    ax.add_artist(label_legend)
    line.remove()
def sciforyax(ax):
    formatter=ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.yaxis.set_major_formatter(formatter)
def sciforxax(ax):
    formatter=ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True)
    formatter.set_powerlimits((0,0))
    ax.xaxis.set_major_formatter(formatter)
cbformat=ticker.ScalarFormatter(useMathText=True,useOffset=True)
cbformat.set_powerlimits((-0,0))
cbformat.format="%.2f"

import matplotlib.ticker
class OOMFormatter(matplotlib.ticker.ScalarFormatter):
    def __init__(self, order=0, fformat="%.3f", offset=True, mathText=True):
        self.oom = order
        self.fformat = fformat
        matplotlib.ticker.ScalarFormatter.__init__(self,useOffset=offset,useMathText=mathText)
    def _set_order_of_magnitude(self):
        self.orderOfMagnitude = self.oom
    def _set_format(self, vmin=None, vmax=None):
        self.format = self.fformat
        if self._useMathText:
             self.format = r'$\mathdefault{%s}$' % self.format
def fee(d):
    import os
    if (os.path.exists(d)):
        # print("The file exists. ")
        sz= os.path.getsize(d)
        if not sz:
            print(d," is empty!")
            return False
        else: 
            print("Size of ",d," is ", sz/1024,'KB' )
            return True
    else:
        print(d, " is not exists! ")
        return  False 
        
import  imageio
import os
def compose_gif(image_list,gif_name,myduration):
    frames=[]
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(gif_name,frames,'GIF',duration=myduration)
    return


levels=100
figureDPI=1200
figureType="jpeg"
timeUnit="fs"

totdir='D:\\dataofh2o\\'
totdir='D:\\doc\\data\\ori\\h2o\\wavelength\\'
dirlist=os.listdir(totdir)
n=len(dirlist)

maxslist=[]
for i in range(n-1):
    dir=totdir+dirlist[i]+'\\'
    print('Working directory',dir)
    print(i,dir)
    print("\n")
    # f=open(dir+"alog.txt",encoding="utf-8")
    # print(f.read(1500))
    TimeBegin=0
    TimeEnd=10

    data=np.loadtxt(dir+'pulse.dat')
    t=data[:,0]
    v=data[:,1]
    plt.plot(t,v,'k-')
    plt.xlim(TimeBegin,TimeEnd)
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel('$E(t)$ (a.u.)')
    plt.savefig(dir+'pluse'+figureType,bbox_inches='tight',dpi=figureDPI)
    # plt.show()
    plt.close()

    data=np.loadtxt(dir+'J.dat')
    t=data[:,0]
    v=data[:,1]
    plt.plot(t,v,'k-')
    plt.xlabel('Time ('+timeUnit+')')
    plt.ylabel('$\\langle J\\rangle$')
    # plt.savefig(dir+'J'+figureType,bbox_inches='tight',dpi=figureDPI)
    # plt.show()
    plt.close()
    maxlist=[]
    maxlist.append((i+1)*100)
    plt.figure(figsize=(8*2/2.54,13/2.54))
    file=dir+'cos1Zz.dat'
    if fee(file):
        i=1
        ax=plt.subplot(2,2,i)
        setlabel(ax,'(a)')
        data=np.loadtxt(file)
        t=data[:,0]
        v=data[:,1]
        plt.plot(t,v,'k-')
        plt.xlim(TimeBegin,TimeEnd)
        dv=max(v)-min(v)
        maxlist.append(max(abs(v)))
        plt.ylim(min(v)-0.2*dv,max(v)+0.2*dv)
        plt.xlabel('Time ('+timeUnit+')')
        plt.ylabel('$\\langle \\mathrm{cos} \\theta \\rangle _{Zz}$')
    file=dir+'cos2Zz.dat'
    if fee(file):
        i=i+1
        ax=plt.subplot(2,2,i)
        setlabel(ax,'(b)')
        data=np.loadtxt(file)
        t=data[:,0]
        v=data[:,1]
        maxlist.append(max(abs(v)))
        plt.plot(t,v,'k-')
        plt.xlim(TimeBegin,TimeEnd)
        dv=max(v)-min(v)
        plt.ylim(min(v)-0.2*dv,max(v)+0.2*dv)
        plt.xlabel('Time ('+timeUnit+')')
        plt.ylabel('$\\langle \\mathrm{cos}^2 \\theta \\rangle _{Zz}$')
    file=dir+'cos2Xx.dat'
    if fee(file):
        i=i+1
        ax=plt.subplot(2,2,i)
        setlabel(ax,'(c)')
        data=np.loadtxt(file)
        t=data[:,0]
        v=data[:,1]
        maxlist.append(max(abs(v)))
        plt.plot(t,v,'k-')
        plt.xlim(0,5)
        dv=max(v)-min(v)
        plt.ylim(min(v)-0.2*dv,max(v)+0.2*dv)
        plt.xlabel('Time ('+timeUnit+')')
        plt.ylabel('$\\langle \\mathrm{cos} ^2\\theta \\rangle _{Xx}$')
    file=dir+'cos2Yy.dat'
    if fee(file):
        i=i+1
        ax=plt.subplot(2,2,i)
        setlabel(ax,'(d)')
        data=np.loadtxt(file)
        t=data[:,0]
        v=data[:,1]
        maxlist.append(max(abs(v)))
        plt.plot(t,v,'k-')
        plt.xlim(TimeBegin,TimeEnd)
        dv=max(v)-min(v)
        maxori=max(abs(v))
        print(maxori)
        plt.ylim(min(v)-0.2*dv,max(v)+0.2*dv)
        plt.xlabel('Time ('+timeUnit+')')
        plt.ylabel('$\\langle \\mathrm{cos} ^2\\theta \\rangle _{Yy}$')
    plt.savefig(dir+'cos'+str(maxori)+'.'+figureType,dpi=figureDPI)
    # plt.show()
    plt.close()
    maxslist.append(maxlist)
    
print(maxslist)
np.savetxt(totdir+'maxs.dat',maxslist)
ax=gca()
for i in range(len(maxslist[0,:])):
    plt.plot(maxslist[:,0],maxslist[:,i+1])
    