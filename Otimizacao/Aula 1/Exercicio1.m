Nodes= load('Nodes.txt');
Links= load('Links.txt');
L= load('L.txt');
nNodes= size(Nodes,1);
nLinks= size(Links,1);
G=graph(L);
servers= randperm(100,8);
% Computing the average shortest path length from each
% node to its closest server node:
t=tic
time=20
savefile=fopen('Stats.txt','w');
while toc(t)<time
    servers= randperm(100,8);
    fprintf(savefile, '%d, ', servers);
    AvSP= AverageSP(G,servers);
    fprintf(savefile, ':%f\n', AvSP);
end
fclose(savefile);



