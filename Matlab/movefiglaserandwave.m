

xrange=[-0.01 0.501];
radupper=15;
for i=0:1:15
    for j=0:5:5
        dir=['F:\doc\ion1\deltat\dteq',num2str(i),num2str(j),'fs\'];
f=figure(1);
set(gcf,'position',[800,600,800,600]);
        subplot(3,2,[1,2])
name_file=[dir,'laser.dat'];
 if (exist(name_file) ~= 0)
data=textread(name_file);
x=data(:,1);
y=data(:,2);
z=data(:,3);
v=data(:,4);
%y_3=data_1(:,4);
plot(x,y,'k-',x,z,'r-',x,v,'b-','linewidth',1);
xlim(xrange);
xlabel('Time (ps)');
ylabel('E(t) (a.u.)');
subplot(3,2,3);
data=textread([dir,'vgr_rad.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ground State');

subplot(3,2,4);
data=textread([dir,'exc_rad.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Excited State');

subplot(3,2,5);
data=textread([dir,'ion_rad.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ionized State');

subplot(3,2,6);
data=textread([dir,'totalraddis.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Total State');
%exportgraphics(f,'laserandwave.jpeg','Resolution',300)
print(gcf,'-djpeg',[dir,'laserandwave.jpeg']);
 end
    end
end
dir=['F:\doc\ion1\deltat\dteq',num2str(i),num2str(j),'fs\'];
for i=0:1:15
    for j=0:5:5
name_file=[dir,'laserandwave.jpeg'];
if (exist(name_file) ~= 0)
A=imread(name_file);
[I,map]=rgb2ind(A,256);
if(i==0)
    imwrite(I,map,'F:\doc\ion1\movefig.gif','DelayTime',0.5,'LoopCount',Inf)
else
    imwrite(I,map,'F:\doc\ion1\movefig.gif','WriteMode','overwirte','DelayTime',0.5)
end
end 
 end
    end
