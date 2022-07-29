
for i=0:1:15
    for j=0:5:5
name_file=['F:\doc\ion1\deltat\dteq',num2str(i),num2str(j),'fs\laserandwave.jpeg'];
if (exist(name_file) ~= 0)
A=imread(name_file);
[I,map]=rgb2ind(A,256);
if(i==0)
    imwrite(I,map,'F:\doc\ion1\movefig.gif','DelayTime',0.5,'LoopCount',Inf)
else
    imwrite(I,map,'F:\doc\ion1\movefig.gif','WriteMode','append','DelayTime',0.5)
end
end
 end
    end