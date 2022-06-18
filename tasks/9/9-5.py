import numpy as np

a1 = np.int8(-456)
print(a1)

a = np.int32(2147483610)
b = np.int32(2147483605)

# print(np.finfo(np.float16))
print(np.float16(4.12))
# 4.12
print(np.float16(4.13))

print(np.float16(4.123))

print(np.float16(4.124))

print(np.float16(4.125))

# print(np.sctypeDict)
# print(len(np.sctypeDict))
# print(*sorted(map(str, set(np.sctypeDict.values()))), sep='\n')
# a = np.bool_(a)
# print(type(a))

# a = np.str_(a)
# print(type(a))
 
 