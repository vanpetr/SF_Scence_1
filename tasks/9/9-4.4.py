# Вначале избавьтесь от излишней вложенности: 
# в каждой переменной (center, south, north) должен храниться объединённый список купленных товаров без разбиения по чекам. 
# определите, в каком магазине было куплено больше всего товаров
from hidden import north, center, south
from collections import Counter
from collections import defaultdict
north_list = [elem for bill in north for elem in bill]
center_list = [elem for bill in center for elem in bill]
south_list = [elem for bill in south for elem in bill]
c = Counter(north_list)
n = Counter(center_list)
s = Counter(south_list)
print(sum(c.values()))
print(sum(n.values()))
print(sum(s.values()))
print(c.su)