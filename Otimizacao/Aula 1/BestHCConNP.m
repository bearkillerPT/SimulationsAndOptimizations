function [min_ConNP,min_servers] = BestHCConNP(search_time,current_best_n)
L= load('L.txt');
G=graph(L);
N = numnodes(G);
n = length(current_best_n);
t=tic;
servers= current_best_n;
min_ConNP = ConnectedNP(G,current_best_n);
while toc(t)<search_time
    others_connp= setdiff(1:N,servers);
    servers_connp= [servers(randperm(n,n-1)) others_connp(randperm(N-n,1))];
    ConNP= ConnectedNP(G,servers_connp);
    if(ConNP < min_ConNP)
        min_ConNP = ConNP;
        servers= servers_connp;
    end    
end
min_servers=servers;
end



