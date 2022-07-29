
for i=1:1:200
    h_fig=figure('Visible','off');
    %set(0,'DefaultFigureVisible', 'off')
    set(gcf,'position',[200,200,500,500]);
    name_file=['F:\ion1_wave\t3\wave\wave_at_pos',num2str(i),'_fs.dat'];
    print(name_file);
    if (exist(name_file) ~= 0)
    data_wave2d=textread(name_file);
    x1=data_wave2d(:,1);
    y1=data_wave2d(:,2);
    z_v=data_wave2d(:,3);
    z_e=data_wave2d(:,4);
    z_i=data_wave2d(:,5);
    z_t(:)=z_v(:)+z_e(:)+z_i(:);
    [x,y]=meshgrid(min(x1):0.01:max(x1),min(y1):0.01:max(y1));
    %title('+',num2str(i));
    %image(x_wave2d,y_wave2d,z_wave2d);',num2str(i),'
    subplot(2,2,1)
    %set(gca,'xtick',[],'ytick',[],'xcolor','w','ycolor','w');
    %backColor=[0.0 0.0 250];set(gca,'color',backColor);
    z=griddata(x1,y1,z_v,x,y);
    %figure('visible','off');
    surf(x,y,z,'EdgeColor','none');
    view(0,60);
    axis([-11 11 -11 11 0 inf]);
    axis off;
    
    %,xlabel('Radial variable (a.u.)'),ylabel('Potential energy (a.u.)');
    text(12,-22,num2str(i));
    text(18,-22,'fs');
    text(10,-10,"G");
    subplot(2,2,2)
    z=griddata(x1,y1,z_e,x,y);
    surf(x,y,z,'EdgeColor','none');
    view(0,60);
    axis([-11 11 -11 11 0 inf]);    
    axis off;
    text(-10,-10,"E");
    subplot(2,2,3)
    z=griddata(x1,y1,z_i,x,y);
    surf(x,y,z,'EdgeColor','none');
    view(0,60);
    axis([-11 11 -11 11 0 inf]);
    axis off;
    text(10,10,"I");
    subplot(2,2,4)
    z=griddata(x1,y1,z_t,x,y);
    surf(x,y,z,'EdgeColor','none');
    view(0,60);
    axis([-11 11 -11 11 0 inf]);
    axis off;
    text(-10,10,"T");
    name_file1=['F:\ion1_wave\t3\wave\wave_at_pos',num2str(i),'_fs.jpeg'];
    saveas(h_fig,name_file1);
    close(h_fig);
    end
    clear;
end
% 
for i=1:1:1928
name_file1=['F:\dataofion1\p_exc_vj\p_vj_at_pos',num2str(i),'_fs.jpeg'];
if (exist(name_file1) ~= 0)
A=imread(name_file1);
[I,map]=rgb2ind(A,256);
if(i==1)
    imwrite(I,map,'F:\dataofion1\p_exc_vj\movefig.gif','DelayTime',0.2,'LoopCount',Inf)
else
    imwrite(I,map,'F:\dataofion1\p_exc_vj\movefig.gif','WriteMode','append','DelayTime',0.2)
end
end
end

