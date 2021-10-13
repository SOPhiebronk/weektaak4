
Sequentie = ('MEDYTKIEKIGEGTYGVVYKGRHKTTGQVVAMKKIRLESEEEGVPSTAIREISLLKELRHPNIVSLQDVLMQDSRLYLIFEFLSMDLKKYLDSIPPGQYMDSSLVKSYLYQILQGIVFCHSRRVLHRDLKPQNLLIDDKGTIKLADFGLARAFGIPIRVYTHEVVTLWYRSPEVLLGSARYSTPVDIWSIGTIFAELATKKPLFHGDSEIDQLFRIFRALGTPNNEVWPEVESLQDYKNTFPKWKPGSLASHVKNLDENGLDLLSKMLIYDPAKRISGKMALNHPYFNDLDNQIKKM')



count_A = Sequentie.count('A')
count_T = Sequentie.count('T')
count_G = Sequentie.count('G')
count_C = Sequentie.count('C')
count_D = Sequentie.count('D')
count_M = Sequentie.count('M')
count_P = Sequentie.count('P')
count_I = Sequentie.count('I')
count_R = Sequentie.count('R')
count_E = Sequentie.count('E')
count_V = Sequentie.count('V')
count_H = Sequentie.count('H')
count_S = Sequentie.count('S')
count_Y = Sequentie.count('Y')
count_L = Sequentie.count('L')
count_N = Sequentie.count('N')
count_F = Sequentie.count('F')
count_K = Sequentie.count('K')
count_Q = Sequentie.count('Q')
count_W = Sequentie.count('W')

massa_A = count_A * 71.078
massa_T = count_T * 101.104
massa_G = count_G * 57.051
massa_C = count_C * 103.143
massa_D = count_D * 115.087
massa_M = count_M * 131.196
massa_P = count_P * 97.115
massa_I = count_I * 113.158
massa_R = count_R * 156.186
massa_E = count_E * 129.114
massa_V = count_V * 99.131
massa_H = count_H * 137.139
massa_S = count_S * 87.077
massa_Y = count_Y * 163.173
massa_L = count_L * 113.158
massa_N = count_N * 114.103
massa_F = count_F * 147.174
massa_K = count_K * 128.172
massa_Q = count_Q * 128.129
massa_W = count_W * 186.210


Massa_gewicht_eiwit = massa_A + massa_T + massa_G + massa_C + massa_D + massa_M + massa_P + massa_I + massa_R + massa_E + massa_V + massa_H + massa_S + massa_Y + massa_L + massa_N + massa_F + massa_K + massa_Q + massa_W

print('Dit is het massa gewicht van dit eiwit: ', Massa_gewicht_eiwit )
