function [min_servers] = AdaptativeSearch(G, servers, neighbor_type)
    min_ConNP = ConnectedNP(G, servers);
    min_servers = servers;

    if neighbor_type == "def1Neighbors"
        others_connp = def1Neighbors(G, servers);
    else
        others_connp = def2Neighbors(G, servers, setdiff(servers, next_servers));
    end

    for other = others_connp
        servers_connp = [servers other];
        ConNP = ConnectedNP(G, servers_connp);

        if (ConNP < min_ConNP)
            min_ConNP = ConNP;
            min_servers = servers_connp;
        end

    end
end

function [neighborhood] = def1Neighbors(G, servers)
    N = numnodes(G);
    neighborhood = setdiff(1:N, servers);
end

function [neighborhood] = def2Neighbors(G, new_servers, candidate)
    neighborhood = setdiff(neighbors(G, candidate).', new_servers);
end
