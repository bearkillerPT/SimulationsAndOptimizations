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
time=60*15;
min_avsp = 1000000;
min_servers=[];
while toc(t)<time
    servers= randperm(100,8);
    AvSP= AverageSP(G,servers);
    if(AvSP < min_avsp)
        min_avsp = AvSP
        min_servers = servers
    end
end




