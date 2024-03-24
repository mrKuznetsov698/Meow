import math as m
import matplotlib.pyplot as plt


def parse(filename: str):
    U, I = [], []
    with open(filename, 'r') as fl:
        for l in fl.readlines():
            ui, ii = map(float, l.split(' '))
            U.append(ui)
            I.append(ii)
    return U, I


def least_sqaures(x, y, n):
    x_avrg = sum(x) / n
    y_avrg = sum(y) / n
    xy_avrg = sum([x[i] * y[i] for i in range(n)]) / n
    x2_avrg = sum(el * el for el in x) / n
    # y2_avrg = sum(el * el for el in y) / n
    print()
    k = (xy_avrg - x_avrg * y_avrg) / (x2_avrg - x_avrg * x_avrg)
    b = y_avrg - k * x_avrg
    # kx + b
    return k, b, x_avrg


U, I = parse('data.txt')
assert len(U) == len(I)

U_open = -1; open_i = -1
# С этого значения мы будем скармливать МНК
for i in range(len(U)):
    if I[i] > 0:
        U_open = U[i]
        open_i = i
        break


N = len(U)
min_u = min(U); max_u = max(U)

k, b, u_avrg = least_sqaures(U[open_i:], I[open_i:], N - open_i)
real_open_u = -b / k

R = (u_avrg - real_open_u) / (u_avrg * k + b)

print('Напряжение открытия =', real_open_u, 'Вольт')
print('R =', R, 'Ом')
print(f"P(U) = {k} * U^2 {'-' if b < 0 else '+'} {abs(b)} * U")
print('P(20В) =', k * 20 * 20 + b * 20, 'Ватт')

fig, ax = plt.subplots()

ax.plot(U, I)
ax.plot(range(m.floor(U_open), m.ceil(max_u)), [k * i + b for i in range(m.floor(U_open), m.ceil(max_u))])

ax.set_xlabel('U, В')
ax.set_ylabel('I, A')

plt.show()
