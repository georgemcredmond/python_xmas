"""Python Christmas Tree
Written by George McRedmond
12-2019
"""

try:
    xmasRows = int(input("How many rows of ornaments?")) # specify the tree's height
except:
    xmasRows = 10
print((xmasRows+2)*' '+'Merry Christmas!')
for i in range(xmasRows):
    print((xmasRows-i)*2*' '+'o'+ i*'~x~o')
    print(((xmasRows-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')