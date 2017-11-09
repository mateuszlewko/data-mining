N1 = 10;
M = 100;
d = 100;
X = rand(d, N1);
Y = rand(d, M);

tic
h1 = dist_mat(X, Y, d, N1, M)
toc

N2 = 100;
X = rand(d, N2);
tic
h2 = dist_mat(X, Y, d, N2, M)
toc

function h = dist_mat(X, Y, d, xlen, ylen)
    h = zeros(xlen, ylen);
    for i = 1:xlen
        for j = 1:ylen
            h(i, j) = dist_vec(X(:, i), Y(:, j), d);
        end
    end
end

function d = dist_vec(X, Y, len)
    d = sum(arrayfun(@(ind) (X(ind) - Y(ind)) ^ 2, 1:len));
end