import random
s=["rock",'paper',"scissors"]
computer=random.choice(s)
user=input('enter rock paper or scissor')
print('computer has chosen',computer)
if user==computer:
 print('it is a tie')
elif computer=='rock':
  if user=='paper':
    print('you won')
  else:
    print('you lose')
elif computer=='paper':
  if user=='scissors':
   print('you won')
  else:
    print('you lose')
elif computer=='scissor':
  if user=='rock':
    print('you won')
  else:
    print('you lose')