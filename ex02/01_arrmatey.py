# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    01_arrmatey.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jobirech <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:18:14 by jobirech          #+#    #+#              #
#    Updated: 2018/06/13 12:18:15 by jobirech         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#import sys
def main(args):
    lists = args[1:]
    for index, item in enumerate(lists):
        print(f"Argv of {index} is {item}")
    lists.sort(key=len, reverse=True)
    for item in lists:
        print(item)
main(sys.argv)