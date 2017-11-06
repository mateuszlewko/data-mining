dist = makedist('Uniform', 'lower', -1, 'upper', 1)
%figure
subplot(2, 2, 1)
nums10k = arrayfun(@(x) (x - 0.5) * 2, rand(1, 10000))
h10k = histogram(nums10k, 100)

subplot(2, 2, 2)
nums100k = arrayfun(@(x) (x - 0.5) * 2, rand(1, 100000))
h100k = histogram(nums100k, 100)

subplot(2, 2, [3 4])
x = -1.02:0.02:1.02
pdfu = pdf(dist, x)
plot(x, pdfu, 'Linewidth', 1)