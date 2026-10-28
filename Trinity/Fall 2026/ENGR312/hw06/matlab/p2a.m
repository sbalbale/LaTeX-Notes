num = [1 3 7];
den = conv([1 1], [1 5 4]);
[A, B, C, D] = tf2ss(num, den)
