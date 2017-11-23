a = linspace(1, 100, 100)
b = linspace(1, 99, 50)
c = linspace(-1.0, 1.0, 201).*pi
d = cat(2, linspace(-1.0, -0.01, 100), linspace(0.01, 1.0, 100)).*pi

e_ = sin(linspace(1, 100, 100));
e = e_ .* (e_ > 0);

A = reshape(a, [10, 10])
dia = linspace(99, 1, 99);
B = diag((1:100)) + diag(dia, -1) + diag(dia, 1)
C = triu(ones(10, 10))

D = cat(1, arrayfun(@(x) (x * (x + 1)) / 2.0, a), factorial(a))

n = 10;
E = ones(n, n);

for i = 1:n
    for j = 1:n
        if mod(j, i) ~= 0
            E(i, j) = 0;
        end
    end
end

E