
clear;
dir='D:\DataOfPro\';
file_name=[dir,'LaserField.dat'];
 if (exist(name_file1) ~= 0)
data_1=textread(file_name);
x_1=data_1(:,1);
y_1=data_1(:,2);
y_2=data_1(:,3);
%y_3=data_1(:,4);re'a
figure(101);
plot(x_1,y_1,'k-','linewidth',0.99);
xlabel('Time (ps)');
ylabel('E(t) (a.u.)');
title('The first laser');
print(gcf,'-djpeg',[dir,'laser1.jpeg']);
figure(102);
plot(x_1,y_2,'k-','linewidth',0.99),xlabel('Time (ps)'),ylabel('E(t) (a.u.)');
title('The second laser');
print(gcf,'-djpeg',[dir,'laser2.jpeg']);
%figure(103);
%plot(x_1,y_3,'k-','linewidth',0.66),xlabel('Time (ps)'),ylabel('E(t) (a.u.)');
%title('The third laser');print(gcf,'-djpeg',['F:dataofion1\laser3.jpeg']);
%figure(100);
%plot(x_1,y_2,'k-',x_1,y_3,'r-','linewidth',0.66),xlabel('Time (ps)'),ylabel('E(t) (a.u.)');
%title('The second and third laser');
clear data_1;
clear x_1;
clear y_1;
clear y_2;
figure(105);
data_pott=textread([dir,'cos1.dat']);
x_21=data_pott(:,1);
y_21=data_pott(:,2);
y_22=data_pott(:,3);
y_23=data_pott(:,4);
xlim([-1 1.78]);
set(gca,'linewidth',0.99);
yyaxis left;
plot(x_21,y_21,'k-','linewidth',1);
ylabel('Orientation');
yyaxis right;
plot(x_21,y_22,'r-','linewidth',1);
xlabel('Time (fs)'),ylabel('Alignment');
legend({'Orientation','Alignment'},'FontSize',7,'Location','northeast');
title('Alignment and Orientation');
print(gcf,'-djpeg',[dir,'Ori_Ali.jpeg']);
clear;

figure(2);
data_pott=textread(dir,'pott.dat');
x_21=data_pott(:,1);
y_21=data_pott(:,2);
y_22=data_pott(:,3);
y_23=data_pott(:,4);
plot(x_21,y_21,'k-',x_21,y_22,'r-',x_21,y_23,'g','linewidth',0.66);
xlabel('Radius (a.u.)'),ylabel('Potential Energy (a.u.)');
legend({'Ground state','excited state','ionization state'},'FontSize',7,'Location','northeast');
title('Potential Energy');
print(gcf,'-djpeg',[dir,'Potential_Energy.jpeg']);
clear;

figure(3);
data_absb=textread(dir,'absb.dat');
x_31=data_absb(:,1);
y_31=data_absb(:,2);
plot(x_31,y_31,'k-','linewidth',0.66),xlabel('Radius (a.u.)'),ylabel('Absorbing Potential');
ylim([-0.1 1.1]);
title('Abs');
print(gcf,'-djpeg',[dir,'absb.jpeg']);
clear;

figure(4);
data_lengdre=textread([dir,'lengdre.dat']);
x_4=data_lengdre(:,1);
y_0=data_lengdre(:,2);
y_1=data_lengdre(:,3);
y_2 =data_lengdre(:,4);
y_3 =data_lengdre(:,5);
y_4 =data_lengdre(:,6);
y_5=data_lengdre(:,7);
y_6=data_lengdre(:,8);
y_7=data_lengdre(:,9);
y_8=data_lengdre(:,10);
y_9=data_lengdre(:,11);
plot(x_4,y_1,'k-',x_4,y_2,'r-',x_4,y_3,'g-',x_4,y_4,'b-',x_4,y_5,'c-',x_4,y_6,'b-.',x_4,y_7,'g-.',x_4,y_8,'r-.',x_4,y_9,'c-.','linewidth',0.66);
xlabel('cos\theta '),ylabel('Population');
legend({'p0','p1','p2','p3','p4','p5','p6','p7','p8','p9'},'FontSize',7,'Location','northeast');
%title('Population');
title('Lengdre');
print(gcf,'-djpeg',[dir,'Population_of_lengdre.jpeg']);
clear;

figure(5);
data_eig=textread([dir,'eig.dat']);
x_5=data_eig(1:15,1);
y_51=data_eig(1:15,2);
plot(x_5,y_51,'k-','linewidth',0.9);
xlabel('Levels'),ylabel('Energy (cm^-1)');
title('Energy Levels');
print(gcf,'-djpeg',[dir,'Energy_levels.jpeg']);
% figure(6);
% data_weight=textread(dir,'weight.dat');
% x_6=data_weight(:,1);
% y_61=data_weight(:,2);
% bar(x_6,y_61);
% clear;

figure(7);
set(gcf,'position',[300,300,300,300]);
data_wave2d=textread(dir,'wave2d.dat');
x_wave2d=data_wave2d(:,1);
y_wave2d=data_wave2d(:,2);
z_wave2d=data_wave2d(:,3);
%image(x_wave2d,y_wave2d,z_wave2d);
[x,y]=meshgrid(-5:0.01:5,-5:0.01:5);
z=griddata(x_wave2d,y_wave2d,z_wave2d,x,y);
contourf(x,y,z,500,'LineColor','none')
%,xlabel('Radial variable (a.u.)'),ylabel('Potential energy (a.u.)');
title('wavepket');
print(gcf,'-djpeg',[dir,'wave0.jpeg']);
clear;

figure(8);
data_8=textread([dir,'popu.dat']);
x_8=data_8(:,1);
y_81=data_8(:,2);
y_82=data_8(:,3);
y_83=data_8(:,4);
plot(x_8,y_81,'k-',x_8,y_82,'r-',x_8,y_83,'g-','linewidth',0.9),xlabel('Time (ps)'),ylabel('Population');
legend({'Ground state','excited state','ionized state'},'FontSize',7,'Location','northeast');
title('Population of Different State');
print(gcf,'-djpeg',[dir,'Population_of_different_state.jpeg']);
clear;

figure(9);
data_91=textread([dir,'ori_ali_1.dat']);
x_91=data_91(:,1);
y_911=data_91(:,2);
y_912=data_91(:,3);
plot(x_91,y_911,'k-',x_91,y_912,'r-','linewidth',0.66),xlabel('Time (ps)'),ylabel('Orientation and Alignment');
legend({'Orientation','Alignment'});%,'FontSize',7,'Location','northeast');
title('Orientaton and Alignment of Excited State');
print(gcf,'-djpeg',[dir,'ori_exc.jpeg']);
figure(91);
data_91=textread([dir,'ori_ali_2.dat']);
x_91=data_91(:,1);
y_911=data_91(:,2);
y_912=data_91(:,3);
plot(x_91,y_911,'k-',x_91,y_912,'r-','linewidth',0.66),xlabel('Time (ps)'),ylabel('Orientation and Alignment');
legend({'Orientation','Alignment'});%,'FontSize',7,'Location','northeast');
title('Orientation and Alignment of Ionized State');
print(gcf,'-djpeg',[dir,'ori_ion.jpeg']);
clear;

% figure(10);
% data_10=textread([dir,'ang_dis.dat']);
% x_10=data_10(:,1);
% y_10=data_10(:,2);
% z_10=data_10(:,3);
% [x,y]=meshgrid(min(x_10):0.01:max(x_10),min(y_10):0.1:max(y_10));
% z=griddata(x_10,y_10,z_10,x,y);
% contourf(x,y,z,500,'LineColor','none')
% colorbar
% title('Angular Distribution of Ionized');
% %contourf(x_10,y_10,z_10,16);
% %plot3(x_10,y_10,z_10);
% clear;
% 
% 
% figure(11);
% data_11=textread([dir,'T1_POP_V.dat']);
% x_11=data_11(:,1);
% y11_1=data_11(:,2);
% y11_2=data_11(:,3);
% [x,y]=meshgrid(1.79:0.001:max(x_11),min(y11_1):1:max(y11_1));
% z=griddata(x_11,y11_1,y11_2,x,y);
% contourf(x,y,z,21,'LineColor','none')
% colorbar
% print(gcf,'-djpeg',[dir,'Vibration energy level.jpeg']);
% %plot3(x_11,y11_1,y11_2)
% xlabel('Time (ps)'),ylabel('Vibration energy level'),zlabel('Population');
% clear;


figure(12);
data_12=textread([dir,'timeenergyspctra.dat']);

x_12=data_12(:,1);
y12_1=data_12(:,2);
y12_2=data_12(:,3);
[x,y]=meshgrid(min(x_12):0.01:max(x_12),min(y12_1):0.01:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
xlabel('Time (ps)'),ylabel('rwx'),zlabel('Pspectrum');
title('Spectrum');
print(gcf,'-djpeg',[dir,'Spectrum.jpeg']);
clear;

figure(121);
%h=figure(121);
%set(h,'name','Population of continuous ionized state','Numbertitle','off')
subplot(1,3,1);

data_12=textread([dir,'ion_t1.dat']);
x_12=data_12(:,2);
y12_1=data_12(:,4);
y12_2=data_12(:,5);
[x,y]=meshgrid(min(x_12):0.01:max(x_12),min(y12_1):0.1:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
ylabel('ionized state levels');
text(1,-1,'(a)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');

subplot(1,3,2);
data_12=textread([dir,'ion_t2.dat']);
x_12=data_12(:,2);
y12_1=data_12(:,4);
y12_2=data_12(:,5);
[x,y]=meshgrid(min(x_12):0.01:max(x_12),min(y12_1):0.01:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
text(1,9.6,'(b)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');

subplot(1,3,3);
data_12=textread(dir,'ion_t3.dat');
x_12=data_12(:,2);
y12_1=data_12(:,4);
y12_2=data_12(:,5);
[x,y]=meshgrid(min(x_12):0.01:max(x_12),min(y12_1):0.01:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
text(1,9.6,'(c)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');


%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');
%title('Population of continuous ionized state');
text(-4.5,10.5,'Population of continuous ionized state');
text(-3,-0.7,'\theta (\pi)');
print(gcf,'-djpeg',[dir,'ion_all.jpeg']);
clear;


figure(13);
data_13=textread([dir,'vgr_rad.dat']);
x_13=data_13(:,1);
y_13=data_13(:,2);
z_13=data_13(:,3);
[x,y]=meshgrid(min(x_13):0.01:max(x_13),min(y_13):0.1:max(y_13));
z=griddata(x_13,y_13,z_13,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ground State');
print(gcf,'-djpeg',[dir,'vgr_rad.jpeg']);
clear;
figure(14);
data_14=textread([dir,'vgr_ang.dat']);
x_14=data_14(:,1);
y_14=data_14(:,2);
z_14=data_14(:,3);
[x,y]=meshgrid(1.78:0.01:max(x_14),min(y_14):0.1:max(y_14));
z=griddata(x_14,y_14,z_14,x,y);
contourf(x,y,z,100,'LineColor','none')
colorbar
%plot3(x_14,y_14,z_14);
xlabel('Time (ps)'),ylabel('Angle ({\circ})');
title('Angular Distribution of Ground State');
print(gcf,'-djpeg',[dir,'vgr_ang.jpeg']);
clear;


figure(141);
data_14=textread([dir,'totalraddis.dat']);
x_14=data_14(:,1);
y_14=data_14(:,2);
z_14=data_14(:,3);
[x,y]=meshgrid(1.78:0.01:max(x_14),min(y_14):0.1:max(y_14));
z=griddata(x_14,y_14,z_14,x,y);
contourf(x,y,z,100,'LineColor','none')
colorbar
%plot3(x_14,y_14,z_14);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radiss Distribution of total State');
print(gcf,'-djpeg',[dir,'totalraddis.jpeg']);
clear;


figure(15);
data_15=textread([dir,'exc_rad.dat']);
x_15=data_15(:,1);
y_15=data_15(:,2);
z_15=data_15(:,3);
[x,y]=meshgrid(min(x_15):0.01:max(x_15),min(y_15):0.1:max(y_15));
z=griddata(x_15,y_15,z_15,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Excited State');
print(gcf,'-djpeg',[dir,'exc_rad.jpeg']);
clear;



figure(16);
data_16=textread([dir,'exc_ang.dat']);
x_16=data_16(:,1);
y_16=data_16(:,2);
z_16=data_16(:,3);
[x,y]=meshgrid(min(x_16):0.01:max(x_16),min(y_16):0.1:max(y_16));
z=griddata(x_16,y_16,z_16,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_14,y_14,z_14);
xlabel('Time (ps)'),ylabel('Angle ({\circ})');
title('Angle Distribution of Excited State');
print(gcf,'-djpeg',[dir,'exc_ang.jpeg']);
clear;


figure(17);
data_17=textread([dir,'ion_rad.dat']);
x_17=data_17(:,1);
y_17=data_17(:,2);
z_17=data_17(:,3);
%plot3(x_17,y_17,z_17);
[x,y]=meshgrid(min(x_17):0.01:max(x_17),min(y_17):0.1:max(y_17));
z=griddata(x_17,y_17,z_17,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_13,y_13,z_13);
xlabel('Time (ps)'),ylabel('Radius (a.u.)');
title('Radial Distribution of Ionization State');
print(gcf,'-djpeg',[dir,'ion_rad.jpeg']);
clear;


figure(18);
data_18=textread([dir,'ion_ang.dat']);
x_18=data_18(:,1);
y_18=data_18(:,2);
z_18=data_18(:,3);
[x,y]=meshgrid(min(x_18):0.01:max(x_18),min(y_18):0.1:max(y_18));
z=griddata(x_18,y_18,z_18,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_14,y_14,z_14);
xlabel('Time (ps)'),ylabel('Angle ({\circ})');

title('Angular Distribution of Ionized State');
print(gcf,'-djpeg',[dir,'ion_ang.jpeg']);
clear;

figure(19);
data_19=textread([dir,'ion_t1.dat']);
x_19=data_19(:,1);
y19_1=data_19(:,2);
y19_2=data_19(:,3);
y19_3=data_19(:,4);
y19_4=data_19(:,5);
[x,y]=meshgrid(min(y19_2):0.1:max(y19_2),min(y19_3):0.1:max(y19_3));
z=griddata(y19_2,y19_3,y19_4,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar;
xlabel('Anlge (\alpha)'),ylabel('Energy (eV)');
print(gcf,'-djpeg',[dir,'Angle-Photoelectron_spectra1.jpeg']);
figure(21);
plot(y19_3,y19_4);
print(gcf,'-djpeg',[dir,'Photoelectron_spectra1.jpeg']);
clear;


figure(20);
data_20=textread([dir,'ion_t2.dat']);
x_20=data_20(:,1);
y20_1=data_20(:,2);
y20_2=data_20(:,3);
y20_3=data_20(:,4);
y20_4=data_20(:,5);

[x,y]=meshgrid(min(y20_2):0.1:max(y20_2),min(y20_3):0.1:max(y20_3));
z=griddata(y20_2,y20_3,y20_4,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar;
xlabel('Anlge (\alpha)'),ylabel('Energy (eV)');
print(gcf,'-djpeg',[dir,'Angle-Photoelectron_spectra2.jpeg']);
figure(22);
plot(y20_3,y20_4);
print(gcf,'-djpeg',[dir,'Photoelectron_spectra2.jpeg']);
clear;


figure(23);
data_18=textread([dir,'totalangdis.dat']);
x_18=data_18(:,1);
y_18=data_18(:,2);
z_18=data_18(:,3);
[x,y]=meshgrid(min(x_18):0.01:max(x_18),min(y_18):0.1:max(y_18));
z=griddata(x_18,y_18,z_18,x,y);
contourf(x,y,z,500,'LineColor','none')
colorbar
%plot3(x_14,y_14,z_14);
xlabel('Time (ps)'),ylabel('Angle ({\circ})');

title('Angular Distribution of Total');
print(gcf,'-djpeg',[dir,'totalang.jpeg']);
clear;

figure(24);
%h=figure(121);
%set(h,'name','Population of continuous ionized state','Numbertitle','off')
subplot(1,3,1);

data_12=textread([dir,'vgr_ang.dat']);
x_12=data_12(:,1);
y12_1=data_12(:,2);
y12_2=data_12(:,2);
[x,y]=meshgrid(1.78:0.01:max(x_12),min(y12_1):0.1:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
caxis([0,2]);
ylabel('Angle (degree)');
text(1,-1,'(a)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');

subplot(1,3,2);
data_12=textread([dir,'exc_ang.dat']);
x_12=data_12(:,1);
y12_1=data_12(:,2);
y12_2=data_12(:,3);
[x,y]=meshgrid(1.78:0.01:max(x_12),min(y12_1):0.01:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
caxis([0,2]);
text(1,9.6,'(b)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');

subplot(1,3,3);
data_12=textread([dir,'ion_ang.dat']);
x_12=data_12(:,1);
y12_1=data_12(:,2);
y12_2=data_12(:,3);
[x,y]=meshgrid(1.78:0.01:max(x_12),min(y12_1):0.01:max(y12_1));
z=griddata(x_12,y12_1,y12_2,x,y);
contourf(x,y,z,500,'LineColor','none')
caxis([0,2]);
text(1,9.6,'(c)','Color','black');
%colorbar
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');
%xlabel('Time (ps)'),ylabel('ionized state levels'),zlabel('Population');
%title('Population of continuous ionized state');
text(-4.5,10.5,'Wave function of angle-resolved');
text(-3,-0.7,'\theta ');
print(gcf,'-djpeg',[dir,'Wave function of angle-resolved.jpeg']);
clear;


