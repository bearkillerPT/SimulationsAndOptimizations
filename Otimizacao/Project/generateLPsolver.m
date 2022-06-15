function generateLPsolver(n, N)
    [Nodes,Links,L]= generateTopology(88194);
    fid = fopen('CND.lpt', 'wt');
    fprintf(fid, 'min ');

    for i = 1:n - 1

        for j = i:n
            fprintf(fid, '+ u%d_%d ', i, j);
        end

    end

    fprintf(fid, '\nsubject to\n');

    for i = 1:n
        fprintf(fid, '+ v%d ', i);
    end

    fprintf(fid, '= %d\n', n);

    for i = 1:n-1

        for j = 1:n
            fprintf(fid, 'u%d_%d + v%d + v%d >= 1\n', i, j, i, j);

            for k = j:n
                fprintf(fid, 'u%d_%d >= u%d_%d + u%d_%d - 1 + v%d\n', i, j, i, k, k, j, k);
            end

        end

    end

    fprintf(fid, '\nBounds\n');

    for i =1:n
        for j=1:n
            fprintf(fid, 'u%d_%d >= 0\n', i, j);
        end
    end

    fprintf(fid, '\nbinary\n');

    for i = 1:n
        fprintf(fid, 'v%d ', i);
    end

    fprintf(fid, '\nend');
    fclose(fid);
end
