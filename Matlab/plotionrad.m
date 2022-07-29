clear;
xrange=[-0.01 0.51];
radrange=[1.75 15];
radupper=15;

for i=0:5:5
    for j=0:1:15
    h_fig=figure('Visible','off');
    set(0,'DefaultFigureVisible', 'off')
dir=['F:\doc\ion1\deltat\dteq',num2str(j),num2str(i),'fs\'];
name_file=[dir,'laser.dat'];
 if (exist(name_file) ~= 0)
data=textread(name_file);
x=data(:,1);
y=data(:,2);
z=data(:,3);
v=data(:,4);
%y_3=data_1(:,4);
figure(101);
plot(x,y,'k-',x,z,'r-',x,v,'b-','linewidth',1);
xlim(xrange);
xlabel('Time (ps)');
ylabel('E(t) (a.u.)');
%title('The first laser');
print(gcf,'-djpeg',[dir,'laser1.jpeg']);
% figure(11)
% data=textread([dir,'laser_fre.dat']);
% x=data(:,1);
% y=data(:,2);
% plot(x,y,'k-','linewidth',1);
 figure(2);
data=textread([dir,'pott.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
v=data(:,4);
plot(x,y,'k-',x,z,'r-',x,v,'g','linewidth',0.66);
xlabel('Radius (a.u.)'),ylabel('Potential Energy (a.u.)');
legend({'Ground state','excited state','ionization state'},'FontSize',7,'Location','northeast');
title('Potential Energy');
xlim(radrange)
print(gcf,'-djpeg',[dir,'Potential_Energy.jpeg']);


figure(3);
data=textread([dir,'absb.dat']);
x=data(:,1);
y=data(:,2);
plot(x,y,'k-','linewidth',0.66),xlabel('Radius (a.u.)'),ylabel('Absorbing Potential');
ylim([-0.1 1.1]);
xlim(radrange);
title('Abs');
print(gcf,'-djpeg',[dir,'absb.jpeg']);






figure(8);
data=textread([dir,'popu.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
v=data(:,4);
plot(x,y,'k-',x,z,'r-',x,v,'g-','linewidth',0.9),xlabel('Time (ps)'),ylabel('Population');
legend({'Ground state','excited state','ionized state'},'FontSize',7,'Location','northeast');
title('Population of Different State');
xlim(xrange);

print(gcf,'-djpeg',[dir,'Population_of_different_state.jpeg']);



figure(12);
data=textread([dir,'timeenergyspctra.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:max(y));
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
xlabel('Time (ps)'),ylabel('rwx'),zlabel('Pspectrum');
title('Spectrum');
print(gcf,'-djpeg',[dir,'Spectrum.jpeg']);


figure(13);
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
print(gcf,'-djpeg',[dir,'vgr_rad.jpeg']);

figure(15);
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
print(gcf,'-djpeg',[dir,'exc_rad.jpeg']);




figure(17);
data=textread([dir,'ion_rad.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
%plot3(x_17,y_17,z_17);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ionization State');
print(gcf,'-djpeg',[dir,'ion_rad.jpeg']);

figure(14);
data=textread([dir,'totalraddis.dat']);
x=data(:,1);
y=data(:,2);
z=data(:,3);
[X,Y]=meshgrid(min(x):max(x)/300:max(x),min(y):max(y)/200:radupper);
Z=griddata(x,y,z,X,Y);
contourf(X,Y,Z,100,'LineColor','none')
colorbar
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radiss Distribution of total State');
print(gcf,'-djpeg',[dir,'totalraddis.jpeg']);

figure(24);
subplot(2,2,1);
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

subplot(2,2,2);
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
subplot(2,2,3);
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
subplot(2,2,4);
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
text(1,9.6,'(c)','Color','black');

print(gcf,'-djpeg',[dir,'Wave function of angle-resolved.jpeg']);
 end
    end
end


