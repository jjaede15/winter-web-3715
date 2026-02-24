import random

print('welcome to my game')
print("you are on the beach and you see rolling waves and crabs")
print('you see: an umbrella, a bath towel, and a shark swimming in the water')
print('would you like to: 1)grab the umbrella, 2)lay on the bath towel, 3) go fight the shark')
choice=input('what is your choice ')
if choice== '1':
    print('you grab the umbrella but it falls over and hits you on the head. OUCH')
    print('you are quickly taken to the hospital and now you are in the waiting room')
    print('you see:')
    print('1) a nurse 2) a water fountain 3) some beds')
    hospital_choice=input('which would you like to approach')
    if hospital_choice=='1':
        print('you approach the nurse and she tells you they are ready to take you back')
        print('the nurse asks if you are alergic anistehia')
        nurse_choice=input('1) no 2) yes')
    elif nurse_choice== '1':
        print('you do the procedure and it turns out you are algic so you die')
    elif hospital_choice=='2':
        print('you get poisned from the water')   
    elif hospital_choice=='3':
        print(' you try to lay down because you think there is no one laying there but its a really frail dead person')
        print('a nurse kicks you outs and you die on the sidewalk')                  
elif choice=='2':
    print('there was a crab on the bath towel it pinches you and you start bleeding!')
    print('would you like to apply a bandage')
elif choice=='3':
    print('you wade in the water to fight the shark')
    result=random.randint(1,6)
    if result==1:
        print('theshark bites your arm off and you bleed to death')
    elif result==2 or result==2:
        print('the shark eats you')
    elif result==4:
        print('you punch the shark in the nose and he waddles away')        
    else:
        print('you kill the shark and now you have extra shark meat')