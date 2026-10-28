A = [-1 0 1; 1 -2 0; 0 0 -3];
B = [0; 0; 1];
C = [1 1 0];
D = 0;
[num, den] = ss2tf(A, B, C, D)
G = tf(num, den)
Gmin = minreal(G)
