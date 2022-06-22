function generateLPsolver(n, N)
    L=load('L_88194.txt');
    fid = fopen('CND.lpt', 'w');
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

            if L(i, j) ~= 0
                fprintf(fid, 'u%d_%d + v%d + v%d >= 1\n', i, j, i, j);
            end

        end

    end

    for i = 1:N - 1

        for j = i + 1:N

            if L(i, j) == 0

                for k = find(L(i, :) > 0)

                    if L(i, k) ~= 0 && L(k, j) ~= 0
                        fprintf(fid, 'u%d_%d - u%d_%d - u%d_%d - v%d >= -1\n', i, j, i, k, k, j, k); 
                        %Tested without - v[k] and obtained the same result 
                    end

                end

            end

        end

    end

    
    for i = 1:N - 1

        for j = i + 1:N

            if L(i, j) ~= 0
                ij_val = num2str(L(i, j),'%.4f');
                fprintf(fid, 'u%d_%d = %s\n', i, j, ij_val);
            end

        end

    end

    fprintf(fid, '\nbinary\n');

    for i = 1:N
        fprintf(fid, 'v%d ', i);
    end



    fprintf(fid, '\nend');
    fclose(fid);
end
