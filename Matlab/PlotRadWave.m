figure(1);
subplot(2,2,1)
data=textread('F:\dataofion1\vgr_rad.dat');
x=data(:,1);
y=data(:,2);
z1=data(:,3);
[x1,y1]=meshgrid(min(x):0.01:max(x),min(y):0.01:max(y));
z=griddata(x,y,z1,x1,y1);
contourf(x1,y1,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ground State');
clear;
subplot(2,2,2)
data=textread('F:\dataofion1\exc_rad.dat');
x=data(:,1);
y=data(:,2);
z1=data(:,3);
[x1,y1]=meshgrid(min(x):0.01:max(x),min(y):0.01:max(y));
z=griddata(x,y,z1,x1,y1);
contourf(x1,y1,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Excited State');
clear;
subplot(2,2,3)
data=textread('F:\dataofion1\ion_rad.dat');
x=data(:,1);
y=data(:,2);
z1=data(:,3);
[x1,y1]=meshgrid(min(x):0.01:max(x),min(y):0.01:max(y));
z=griddata(x,y,z1,x1,y1);
contourf(x1,y1,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ionized State');
clear;
subplot(2,2,4)
data=textread('F:\dataofion1\totalraddis.dat');
x=data(:,1);
y=data(:,2);
z1=data(:,3);
[x1,y1]=meshgrid(min(x):0.01:max(x),min(y):0.01:max(y));
z=griddata(x,y,z1,x1,y1);
contourf(x1,y1,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Total States');

print(gcf,'-djpeg',['F:dataofion1\totalraddis.jpeg']);
clear;