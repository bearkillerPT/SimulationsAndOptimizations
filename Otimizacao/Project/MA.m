function [best_servers, best_ConNP] = MA(n, search_time, neighbor_type, population_size, mutation_prob)
    t = tic;
    L = load('L_88194.txt');
    G = graph(L);
    P = [];

    for i = 1:population_size
        [best_servers] = GreedyRandomized(G, n, 4);
        [best_servers] = LocalSearch(G, best_servers, neighbor_type);
        P(i, :) = best_servers;
    end

    while toc(t) < search_time
        new_P = [];

        for i = 1:population_size
            [children] = crossover(G, P);

            if rand < mutation_prob
                [children] = mutation(G, children);
            end

            [children] = LocalSearch(G, children, neighbor_type);
            new_P(i, :) = children;

        end

        [P] = selection(G, P, new_P)
    end

    [best_servers] = getBestServer(G, P);
    best_ConNP = ConnectedNP(G, best_servers);
end

function [p1, p2] = chooseparents(G, P)
    probs = zeros(1, length(P(:, 1)));

    for i = 1:length(P(:, 1))
        probs(i) = ConnectedNP(G, P(i, :));
    end

    conNP_sum = sum(probs);

    for i = 1:length(P(:, 1))
        probs(i) = probs(i) / conNP_sum;
    end

    cp = [0, cumsum(probs)];
    r = rand;
    idx1 = find(r > cp, 1, 'last');
    p1 = P(idx1, :);
    idx2 = idx1;

    while idx1 == idx2
        r = rand;
        idx2 = find(r > cp, 1, 'last');
    end

    p2 = P(idx2, :);
end

function [children] = crossover(G, P)
    [p1, p2] = chooseparents(G, P);
    children = zeros(1, length(p1));

    for i = 1:length(p1)
        child = 0;
        [child1] = getNewChild(p1, children);
        [child2] = getNewChild(p2, children);

        if child1 == -1
            child = child2
            return
        elseif child2 == -1
            child = child1
            return
        end

        if rand > 0.5
            child = child1;

        else

            child = child2;

        end

        children(i) = child;

    end

end

function [children] = mutation(G, children)
    mutation_idx = randi(length(children));
    current_chosen_value = children(mutation_idx);
    new_value = randi(100);

    while ismember(new_value, children)
        new_value = randi(100);
    end

    children(mutation_idx) = new_value;
end

function [best_P] = selection (G, P, new_P)
    joint_P = [P; new_P];
    R = [];

    for i = 1:length(joint_P(:, 1))
        R = [R; i ConnectedNP(G, joint_P(i, :))];
    end

    R = sortrows(R, 2);
    best_P = [];

    for i = 1:length(P(:, 1))
        best_P(i, :) = joint_P(R(i, 1), :);
    end

    best_P = best_P(1:length(P(:, 1)), :);
end

function [child] = getNewChild(P, children)
    child = -1;

    for i = 1:length(P)

        if ismember(P(i), children)
            continue;
        else
            child = P(i);
        end

    end

end

function [best_server] = getBestServer(G, P)
    R = [];

    for i = 1:length(P(:, 1))
        R = [R; i ConnectedNP(G, P(i, :))];
    end

    R = sortrows(R, 2);
    best_P = [];

    for i = 1:length(P(:, 1))
        best_P(i, :) = P(R(i, 1), :);
    end

    best_server = best_P(1, :);
end

function [neighborhood] = def1Neighbors(G, servers)
    N = numnodes(G);
    neighborhood = setdiff(1:N, servers);
end

function [neighborhood] = def2Neighbors(G, new_servers, candidate)
    neighborhood = setdiff(neighbors(G, candidate).', new_servers);
end
