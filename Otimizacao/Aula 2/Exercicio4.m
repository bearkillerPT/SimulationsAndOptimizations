Nodes= load('Nodes.txt');
Links= load('Links.txt');
L= load('L.txt');
nNodes= size(Nodes,1);
nLinks= size(Links,1);
G=graph(L);
servers= randperm(100,8);
N = numnodes(G); % no. of nodes of graph G
n = 8; % no. of nodes of set S
% Computing the average shortest path length from each
% node to its closest server node:
t=tic
time=30;
best_avsp= [81    50    18    47    17    10    49    82];
best_connp= [83    13     3    31    53    97    50    39];
min_avsp = AverageSP(G,best_avsp);
min_ConNP = ConnectedNP(G,best_connp);
while toc(t)<time
    others_avsp= setdiff(1:N,best_avsp);
    servers_avsp= [best_avsp(randperm(n,n-1)) others_avsp(randperm(N-n,1))];
    others_connp= setdiff(1:N,best_connp);
    servers_connp= [best_connp(randperm(n,n-1)) others_connp(randperm(N-n,1))];
    AvSP= AverageSP(G,servers_avsp);
    ConNP= ConnectedNP(G,servers_connp);
    if(AvSP < min_avsp)
        min_avsp = AvSP
        best_avsp = servers_avsp
    end 
    if(ConNP < min_ConNP)
        min_ConNP = ConNP
        best_connp = servers_connp
    end
end



