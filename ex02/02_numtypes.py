# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    02_numtypes.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jobirech <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:18:21 by jobirech          #+#    #+#              #
#    Updated: 2018/06/13 12:18:23 by jobirech         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
#import math

num1 = (int)(sys.argv[1])
num2 = (int)(sys.argv[2])

num = num1 / num2
rem = num1 % num2

a = 10
b = 56.99
c = 9.322e-36j

def data_type(x):
    if type(x) == int:
        return "interger"
    elif type(x) == float:
        return "float"
    elif type(x) == complex:
        return "complex"

print("%i divided by %i equals %i remainder %i" % (num1, num2, num, rem))
print("Variable a contains : %i  which is of type: %s" % (a, data_type(a))) 
print("Variable b contains :", b, "which is of type:", data_type(b)) 
print("Variable c contains :", complex(c), "which is of type:", data_type(c))