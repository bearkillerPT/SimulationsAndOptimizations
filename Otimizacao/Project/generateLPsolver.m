function generateLPsolver(n, N)
    [Nodes, Links, L] = generateTopology(88194);
    fid = fopen('CND.lpt', 'wt');
    fprintf(fid, 'min ');

    for i = 1:N - 1

        for j = i + 1:N

            if L (i, j) > 0
                fprintf(fid, '+ u%d_%d ', i, j);
            end

        end

    end

    fprintf(fid, '\nsubject to\n');

    for i = 1:N
        fprintf(fid, '+ v%d ', i);
    end

    fprintf(fid, '= %d\n', n);

    for i = 1:N - 1

        for j = i + 1:N
            fprintf(fid, 'u%d_%d + v%d + v%d >= 1\n', i, j, i, j);

        end

    end

    for i = 1:N - 1

        for j = i + 1:N

            if L(i, j) == 0

                for k = find(L(i, :) > 0)

                    fprintf(fid, 'u%d_%d - u%d_%d - u%d_%d - v%d >= -1\n', i, j, i, k, k, j, k);
                end

            end

        end

    end

    fprintf(fid, '\nBounds\n');

    for i = 1:N - 1

        for j = i + 1:N
            fprintf(fid, 'u%d_%d >= 0\n', i, j);
        end

    end

    fprintf(fid, '\nbinary\n');

    for i = 1:N
        fprintf(fid, 'v%d ', i);
        for j = i + 1:N
            fprintf(fid, 'u%d_%d ', i,j);
    
        end
    end
    fprintf(fid, '\nend');
    fclose(fid);
end
