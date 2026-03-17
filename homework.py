



import random
destination={
    'city':['Tokyo','Beijing','New Delhi','hakodate','ohio'],
    'beaches':['bali','maldives','cancun'],
    'mountains':['mount fuji','mount everest','himalayas'],
    'islands':['Japan','Easter island','okinawa','taiwan']



}

jokes=["Why don't skeletons ever go skydiving? Because they don't have the guts!","Why should you never trust an atom? Because they make up everything!","What did the calculator say to its friend? You can always count on me!","What do you call a fake noodle? An impasta!"]
food=['fried rice','fried chicken','ramen','naan','noodles']
cars=['nissan GTR r35','huyra roadster pagani','contenental bently gts','mercades amg']


while True:
    cnd=input('enter destination,jokes,food,cars or exit').strip().lower()
    if cnd=='dest':
        o=input('please enter from,beaches,islands,mountains or city').strip().lower()
        print(random.choice(destination.get(o,['wrong choice'])))

    elif cnd=='jokes':
        print(random.choice(jokes))
    elif cnd=='food':
        print(random.choice(food))
    elif cnd=='cars':
        print(random.choice(cars))
    elif cnd=='exit':
        break
    else:
        print('error you got the wrong choice')
