import re

chenn = "badio ap challenge 02 0 12 1  dec 2023"
# re.match("/")
n = re.findall("\d+", chenn)

print(n)

# lisdijit='0,1,2,3,4,5,6,7,8,9'
# chen="idiot il est la 01 kay 07 089"
# rezilta=[]
# j=0
# for i in chen:
#     j+=1
#     if(i=="0"):
#         print(j)
#         if(chen[j] in lisdijit and j-2!=0):
#             rezilta.append(f'{chen[j]}')

# print(rezilta)