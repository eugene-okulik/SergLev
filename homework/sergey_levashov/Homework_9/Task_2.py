temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30, 32,
                30, 28, 24, 23]

heat_wave = list(filter(lambda t: t > 28, temperatures))
print('Максимальная температура:', max(heat_wave))
print('Минимальная температура::', min(heat_wave))
print('Средняя температура:', sum(heat_wave) / len(heat_wave))
