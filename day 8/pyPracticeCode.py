# assert keyword
# --------------
# --> the keyword is used to check the condition
# age = 15 next 22
# assert age>= 18,'not eligible'
# print('eligible')
# output:
# 1.eligible

# 2.    assert age>= 18,'not eligible'
#            ^^^^^^^^
# AssertionError: not eligible
#
#24hour clock into 12hours
# n = tuple(map(int,input("Enter 24h time :").split(':')))
# if n[0] >= 12 and n[0] <= 24:
#     print(f'{n[0] -12}:{n[1]} PM')  
# else:
#     print(f'{n[0]}:{n[1]} AM')
# output:
# Enter 24h time :21:36
# 9:36 PM
# Enter 24h time :11:35
# 11:35 AM