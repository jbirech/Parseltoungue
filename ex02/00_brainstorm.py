# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    00_brainstorm.py                                   :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: jobirech <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/06/13 12:04:56 by jobirech          #+#    #+#              #
#    Updated: 2018/06/13 12:05:01 by jobirech         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

answer_list = []

lists = ["prime numbers betwee 0 n 20", "kenyan presidents", "love stories", "war games", "app on your phone", "cricket teams", "football teams", "soccer teams", "songs you sang", "books read", "games you play", "projects you\'\ve done"]

display = random.choice(lists)
print("name all...")
print(display)

i = 0
while (i < 2):
  answer = input("answer {}:" .format(i + 1))
  i += 1
  answer_list.append(answer)

for answer in answer_list:
  print("                  ",answer.rstrip("[]"))
  print("\n")

  