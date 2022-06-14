%if neighbor_type == "def1Neighbors" 
    %a neighbor node is any node that is not in s;
%else 
    %a neighbor node from the set s is chosen.
    function [best_servers, best_ConNP] = GRASP(n, search_time, neighbor_type)
    t=tic;
    [Nodes, Links, L] = generateTopology(88194);
    G=graph(L);
    [best_s] = GreedyRandomized(G, n-1);
    [best_servers] = AdaptativeSearch(G, servers, neighbor_type);
    best_ConNP = ConnectedNP(G, servers_connp);
    while toc(t)<search_time
        [s] = GreedyRandomized(G, n-1);
        [servers] = AdaptativeSearch(G, servers, neighbor_type);
        conNP = ConnectedNP(G, servers);
        if conNP<best_ConNP
         best_servers=servers;
         min_ConNP=conNP;
        end
    end
end
