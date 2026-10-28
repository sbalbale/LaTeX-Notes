A = [1 2; -4 -3];
B = [1; 2];
C = [1 1];
D = 0;
[num, den] = ss2tf(A, B, C, D)
G = tf(num, den)
