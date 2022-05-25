function [min_ConNP,min_servers] = BestRandConNP(search_time,nodes)
L= load('L.txt');
G=graph(L);
t=tic
min_ConNP = 1000000;
min_servers=[];
while toc(t)<search_time
    servers= randperm(100,nodes);
    ConNP= ConnectedNP(G,servers);
    if(ConNP < min_ConNP)
        min_ConNP = ConNP;
        min_servers = servers;
    end
end





