function [min_avsp,min_servers]=BestRandAvSP(search_time,nodes)
L= load('L.txt');
G=graph(L);
t=tic
min_avsp = 1000000;
min_servers=[];
while toc(t)<search_time
    servers= randperm(100,nodes);
    AvSP= AverageSP(G,servers);
    if(AvSP < min_avsp)
        min_avsp = AvSP;
        min_servers = servers;
    end
end





