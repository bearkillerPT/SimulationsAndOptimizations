%if neighbor_type == "def1Neighbors" 
    %a neighbor node is any node that is not in s;
%else 
    %a neighbor node from the set s is chosen.
    function [best_servers, best_ConNP, best_servers_time] = GRASP(n, search_time, neighbor_type)
    t=tic;
    L= load('L_88194.txt');
    G=graph(L);
    [best_servers] = GreedyRandomized(G, n-1, 4);
    [best_servers] = AdaptativeSearch(G, best_servers, neighbor_type);
    best_ConNP = ConnectedNP(G, best_servers);
    while toc(t)<search_time
        [servers] = GreedyRandomized(G, n-1, 4);
        [servers] = AdaptativeSearch(G, servers, neighbor_type);
        conNP = ConnectedNP(G, servers);
        if conNP<best_ConNP
         best_servers=servers;
         best_ConNP=conNP;
        end
    end
end
