# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    04_bool.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jobirech <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:18:37 by jobirech          #+#    #+#              #
#    Updated: 2018/06/13 12:18:41 by jobirech         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #



a = ["false",True,True,None,True,None,None,False,False,None,True,False]
b = ["or","or","or","==","!=","==","and","==","!=","and","!=","and"] 
c = [False,False,None,None,True,True,False,True,None,False,True,None]

def operand(x):
    if (b[x] == "or"):
        return a[i] or c[i]
    elif b[x] == "==":
        return a[i] == c[i]
    elif b[x] == "!=":
        return a[i] != c[i]
    elif b[x] == "and":
        return a[i] and c[i]
for i in range(len(a)):
    print(a[i],b[i],c[i], "=>", operand(i))