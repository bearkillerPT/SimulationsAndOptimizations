function [min_ConNP,min_servers,execution_time] = BestSAHCConNP(neighbor_type)
t=tic;
L= load('L_88194.txt');
G=graph(L);
N = numnodes(G);
n = 10;
servers= randperm (N, n);
min_ConNP = ConnectedNP(G,servers);
improved = true;
while improved
    last_improvement = min_ConNP;
    if neighbor_type == "def1Neighbors"
        others_connp= def1Neighbors(G,servers);
        next_servers = servers(randperm(n,n-1));
    else
        next_servers= servers(randperm(n,n-1));
        others_connp= def2Neighbors(G,servers,setdiff(servers,next_servers));
        
    end
    for other = others_connp
        servers_connp=[next_servers other];
        ConNP= ConnectedNP(G,servers_connp);
        if(ConNP < min_ConNP)
            min_ConNP = ConNP;
            servers= servers_connp;
        end   
    end
    if last_improvement == min_ConNP
        improved = false;
    end
end
min_servers=servers;
execution_time=toc(t);
end

function [neighborhood] = def1Neighbors(G,servers)
N = numnodes(G);
neighborhood = setdiff(1:N,servers);
end
function [neighborhood] = def2Neighbors(G,new_servers, candidate)
neighborhood = setdiff(neighbors(G,candidate).',new_servers);
end

