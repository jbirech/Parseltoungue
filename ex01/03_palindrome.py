# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    03_palindrome.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jobirech <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:01:34 by jobirech          #+#    #+#              #
#    Updated: 2018/06/13 12:01:36 by jobirech         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#def checkPalindrome(s):
#   r = s[::-1]
#   if s == r:
#       return True
#   else:
#       return False
def reverse_s(s):
    s = s.lower()
    forbidden = (' ', '.', '?', '!', ':', ';', '-', '—', '(', ')', '[', ']', '’', '“', '”', '/', ',', '"')
    for i in forbidden:
        s = s.replace(i, '')
    return s

def reverse(s):
    return s[::-1]

def is_palindrome(s):
    new = reverse_s(s)
    return reverse_s(s) == reverse(reverse_s(s))

something = input('Type something: ')
if (is_palindrome(something)):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")
