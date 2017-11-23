N = 100;
M = 500;
d = 10;
X = rand(d, N);
Y = rand(d, M);

tic
closest(X, Y, 1, N, d)
toc
tic
closest(X, Y, 50, N, d)
toc

% x, y: d * N
% h: k * samples
function h = closest(X, Y, k, samples, d)
    h = zeros(k, samples);
    for i = 1:samples
        x = X(:, i);
        [~, I] = sort(cellfun(@(y) dist_vec(x, y, d), num2cell(Y, 1)));
        h(:, i) = I(1:k);
    end
end

function d = dist_vec(X, Y, len)
    d = sum(arrayfun(@(ind) (X(ind) - Y(ind)) ^ 2, 1:len));
end