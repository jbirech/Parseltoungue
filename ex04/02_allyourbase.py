#def dec_to_bin(x):
#  #  s = int (bin(x)[2:])
 #   print(s)
#print dec_to_bin()

# Function to print binary number for the 
# input decimal using recursion
def decimalToBinary(n):
 
    if n > 1:
         #  divide with integral result 
         # (discard remainder) 
        decimalToBinary(n//2) 
 
    print(n%2, end ='') #for python 3            
 
# Driver code
if __name__ == '__main__':
    decimalToBinary(9455)
    
    #decimalToBinary(18)
    #print
    #decimalToBinary(7)
    #print
