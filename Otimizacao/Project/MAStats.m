function [servers, connp, times] = MAStats()
    servers = [];
    connp = [];
    times = [];
    for i = 1:10
        [servers(i,:), connp(i), times(i)] = MA(8, 300, 'def1Neighbors', 50, 0.05)
    end
end