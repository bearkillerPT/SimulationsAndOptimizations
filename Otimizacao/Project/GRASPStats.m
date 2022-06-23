function [servers, connp, times] = GRASPStats()
    servers = [];
    connp = [];
    times = [];
    for i = 1:10
        [servers(i,:), connp(i), times(i)] =  GRASP(8, 300, 'def1Neighbors')
    end
end