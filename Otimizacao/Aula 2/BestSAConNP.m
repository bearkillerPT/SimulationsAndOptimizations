function [best_ConNP,best_servers] = BestSAConNP(temp_slope)
L= load('L2.txt');
G=graph(L);
N = numnodes(G);
n = 10;
time=tic;
servers= randperm(N,n);
best_servers = servers;
min_ConNP = ConnectedNP(G,servers);
best_ConNP = min_ConNP;
start_temp = - min_ConNP / log(0.5);
%end_temp = - min_ConNP / log(0.001)
temp=start_temp;
while (toc(time)<30)
    others_connp= setdiff(1:N,servers);
    servers_connp= [servers(randperm(n,n-1)) others_connp(randperm(N-n,1))];
    ConNP= ConnectedNP(G,servers_connp);
    x=rand; 
    if(ConNP < min_ConNP)
        min_ConNP = ConNP;
        servers= servers_connp;
        if ConNP < best_ConNP
            best_servers =servers;
            best_ConNP= ConNP;
        end
    elseif (x<exp((ConNP-min_ConNP)/temp))
        min_ConNP = ConNP;
        servers= servers_connp;
    end
    temp= temp_slope * temp;
end
end



