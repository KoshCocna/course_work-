# курсовая работа по звуковещание"

import math

#Определить размеры помещения (объем V, общую площадь ограничивающих поверхностей S)
a = 25
b = 15
c = 7
volume_room = a*b*c
surface_room = 2*(a*b + b*c + c*a)

#Выбрать оптимальное время реверберации Топт и его частотную характеристику
opt_time_reverb = 0.3 * math.log(volume_room, 10) - 0.05 #при частоте 500Гц
#оптимальное время реверберации при разных f, Гц
T_opt = [0.781, 0.878, 0.976, 0.976, 0.976, 0.976]

#Рассчитать требуемые параметры помещения

alpha_required = [(0.161 * volume_room / surface_room)/ i for i in T_opt]
alpha_average = [1 - math.exp(-j) for j in alpha_required]
absorption_required = [i * surface_room for i in alpha_average]

#Определить основные параметры по имеющимся характеристикам помещения

#основной фонд поглощения

#поглощения стены(Штукатурка алебастровая, гладкая по деревянной обрешетке) при 125,250,500,1000,2000,4000Гц
alpha_wall = [0.02, 0.02, 0.03, 0.04, 0.04, 0.03]
surface_wall = 2*(b*c + c*a) - 2*2.4*2.7 - 4*4*3
absorption_of_wall = [i * surface_wall for i in alpha_wall]

#поглощения дверей (Древесина монолитная лакированная)
alpha_door = [0.03, 0.02, 0.05, 0.04, 0.04, 0.04]
surface_door = 2*2.4*2.7
absorption_of_door = [i * surface_door for i in alpha_door]

#поглощения окон(Оконный переплёт)
alpha_window = [0.03, 0.02, 0.15, 0.10, 0.06, 0.04]
surface_window = 4*4*3
absorption_of_window = [i * surface_window for i in alpha_window]

#поглощения пола(паркетный по асфальту)
alpha_floor = [0.04, 0.04, 0.07, 0.06, 0.06, 0.07]
surface_floor = 25*15
absorption_of_floor = [i * surface_floor for i in alpha_floor]

#поглощения потолка(штукатурка по металлической сетке с воздушной полностью позади)
alpha_ceil = [0.04, 0.05, 0.06, 0.08, 0.04, 0.06]
absorption_of_ceil = [i * surface_floor for i in alpha_ceil]

#общий фонд звукопоглощения
absorption_total_fund = []
for i in [0,1,2,3,4,5]: absorption_total_fund.append(absorption_of_wall[i] + absorption_of_door[i] + absorption_of_window[i] + absorption_of_floor[i] + absorption_of_ceil[i])

#доп фонд поглощения

#поглощения 20 стульев
alpha_chair = []
#поглощения 1 кресла
alpha_sofa = []
#поглощения 2 стола
alpha_table = []
#surface_table =
#поглощения 31 человека
alpha_man = [0.14, 0.22, 0.34, 0.45, 0.43, 0.4]
surface_man = 1.9
absorption_of_man = [i * surface_man for i in alpha_man]

print(absorption_of_man)
