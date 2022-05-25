function [neighbors] = def1Neighbors(G,servers)
N = numnodes(G);
neighbors = setdiff(1:N,servers);
end
function [neighbors] = def2Neighbors(G,new_servers, candidate)
neighbors = setdiff(neighbors(G,candidate),new_servers);
end
function [min_ConNP,min_servers] = BestSAHCConNP(search_time,current_best_n, neighbor_type)
L= load('L2.txt');
G=graph(L);
N = numnodes(G);
n = length(current_best_n);
t=tic;
servers= current_best_n;
min_ConNP = ConnectedNP(G,current_best_n);
while toc(t)<search_time
    if neighbor_type == "def1Neighbors"
        others_connp= def1Neighbors(G,servers);
        servers_connp=[servers(randperm(n,n-1)) others_connp(randperm(N-n,1))];
    else
        next_servers= servers(randperm(n,n-1))
        others_connp= def2Neighbors(G,servers,setdiff(servers,next_servers));
        servers_connp=[next_servers others_connp]
    end
    ConNP= ConnectedNP(G,servers_connp);
    if(ConNP < min_ConNP)
        min_ConNP = ConNP;
        servers= servers_connp;
    end    
end
min_servers=servers;
end


