
def decToBin(decNum):
   binNum = 0
   power = 0
   while decNum > 0:
       power += 1
       decNum += 10 ** power * (binNum % 2)
       binNum //= 2
   return binNum
print(decToBin(4))
