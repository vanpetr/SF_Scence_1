# Необходимо напечатать словарь, в котором ключи — годы, а значения — показатели температуры. 
# Ключи необходимо отсортировать в порядке убывания соответствующих им температур.
from collections import OrderedDict
temps = [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5),
        ('2004', -8.2), ('2005', -1.6), ('2006', -5.9), ('2007', -2.4),
        ('2008', -1.7), ('2009', -3.5), ('2010', -12.1), ('2011', -5.8),
        ('2012', -4.9), ('2013', -6.1), ('2014', -6.9), ('2015', -2.7),
        ('2016', -11.2), ('2017', -3.9), ('2018', -2.9), ('2019', -6.5),
        ('2020', 1.5)]
temps  = OrderedDict(sorted(temps, key=lambda x: -x[1])) # x: x[] сортировка по возрастанию x: -x[] сортировка по убыванию

print(temps)