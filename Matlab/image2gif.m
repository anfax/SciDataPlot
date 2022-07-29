
for i=1:1:1928
    
name_file1=['F:\dataofion1\wave\wave_at_pos',num2str(i),'_fs.jpeg'];
if (exist(name_file1) ~= 0)
A=imread(name_file1);
[I,map]=rgb2ind(A,256);
if(i==1)
    imwrite(I,map,'F:\dataofion1\wave\movefig.gif','DelayTime',0.2,'LoopCount',Inf)
else
    imwrite(I,map,'F:\dataofion1\wave\movefig.gif','WriteMode','append','DelayTime',0.2)

end
end
end
