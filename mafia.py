import time
import random
from playsound import playsound

sound_1="1.wav"
sound_2="2.wav"
sound_3="3.wav"
sound_4="4.wav"
sound_5="5.wav"
sound_6="6.wav"
sound_7="7.wav"
sound_8="8.wav"
sound_9="9.wav"
sound_10="10.wav"
stand_up_sound="stand up.wav"
player_sound="player.wav"
sleep_sound="sleep.wav"

print(' welcome...')
playsound('welcome.mp3')
print(' 0-play  \n 1- god father \n 2- doctor \n 3- citizen \n 4-dr. Lecter \n 5-mayor \n 6-psychiatrist \n 7-mafia \n 8-sniper \n 9-die hard \n 10-detective \n 1010-show role ')
god_father=True
doctor=True
citizen=True
dr_lecter=True
mayor=True
psychiatrist=True
mafia=True
sniper=True
die_hard=True
detective=True

while True :
   
    chooser=0
    chooser=int(input(''))

    if chooser==0 :
        break
    elif chooser==1 :
        print(' you can not add or remove god father')
    elif chooser==2 :
        doctor=not doctor
        if doctor == True :
            print (" doctor" , "added")
        elif doctor == False :
            print (" doctor" , "removed")
    elif chooser==3 :
        citizen= not citizen
        if citizen == True :
            print (" citizen" , "added")
        elif citizen == False :
            print (" citizen" , "removed")
    elif chooser==4 :
        dr_lecter = not dr_lecter
        if dr_lecter == True :
            print (" dr-lecter" , "added")
        elif dr_lecter == False :
            print (" dr-lecter" , "removed")
    elif chooser==5 :
        mayor = not mayor
        if mayor == True :
            print (" mayor" , "added")
        elif mayor == False :
            print (" mayor" , "removed")
    elif chooser==6 :
        psychiatrist = not psychiatrist
        if psychiatrist == True :
            print (" psychiatrist" , "added")
        elif psychiatrist == False :
            print (" psychiatrist" , "removed")
    elif chooser==7 :
        mafia = not mafia
        if mafia == True :
            print (" mafia" , "added")
        elif mafia == False :
            print (" mafia" , "removed")
    elif chooser==8 :
        sniper = not sniper
        if sniper == True :
            print (" sniper" , "added")
        elif sniper == False :
            print (" sniper" , "removed")
    elif chooser==9 :
        die_hard = not die_hard
        if die_hard == True :
            print (" die hard" , "added")
        elif die_hard == False :
            print (" die hard" , "removed")
    elif chooser==10 :
        detective = not detective
        if detective == True :
            print (" detective" , "added")
        elif detective == False :
            print (" detective" , "removed")
    elif chooser==1010 :
        print(' 1- god father' ,god_father , ' \n 2- doctor',doctor,' \n 3- citizen ',citizen,'\n 4-dr. Lecter',dr_lecter,' \n 5-mayor',mayor,' \n 6-psychiatrist',psychiatrist,' \n 7-mafia',mafia,' \n 8-sniper',sniper,' \n 9-die hard',die_hard,' \n 10-detective',detective)


crew_num=0
maf_num=0
role_list=[]

if god_father==True :
    role_list.append("god_father")
    maf_num+=1

if doctor==True :
    role_list.append("doctor")
    crew_num+=1

if citizen==True :
    role_list.append("citizen")
    crew_num+=1

if dr_lecter==True :
    role_list.append("dr_lecter")
    maf_num+=1

if mayor==True :
    role_list.append("mayor")
    crew_num+=1

if psychiatrist==True :
    role_list.append("psychiatrist")
    crew_num+=1

if mafia==True :
    role_list.append("mafia")
    maf_num+=1

if sniper==True :
    role_list.append("sniper")
    crew_num+=1

if die_hard==True :
    role_list.append("die_hard")
    crew_num+=1

if detective==True :
    role_list.append("detective")
    crew_num+=1


time.sleep(2)
print("\n " , maf_num , " mafia and" , crew_num ,"citizen")
time.sleep(3)
if maf_num>=crew_num :
    print("There are more mafias than citizens")
    quit()

player_num=maf_num+crew_num

if player_num>=1 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player1=role_picker

if player_num>=2 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player2=role_picker

if player_num>=3 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player3=role_picker

if player_num>=4 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player4=role_picker

if player_num>=5 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player5=role_picker

if player_num>=6 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player6=role_picker

if player_num>=7 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player7=role_picker

if player_num>=8 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player8=role_picker

if player_num>=9 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player9=role_picker

if player_num>=10 : 
    role_picker=random.choice(role_list)
    role_list.remove(role_picker)
    player10=role_picker





def timer() :
    print(' enter timer time :')
    timer_time=int(input())
    def timer_timing() :
        print(' 0-back \n 1-start timer ')
        timer_chooser=int(input())
        if timer_chooser == 0 :
            day()
        elif timer_chooser == 1 :
            print(' start...')
            time.sleep(timer_time)
            print(' end!')
            playsound('timer.wav')
            print(' 1010-exit \n 0-back \n 1-start again  ')
            timer_chooser_2 = int(input())
            
            if timer_chooser_2 == 1010 :
                day()

            elif timer_chooser_2 == 0 :
                timer()

            elif timer_chooser_2 == 1 :
                timer_timing()
    timer_timing()


def vote():
    vote_chooser = -1
    while vote_chooser != 0:
        print("0-next \n 1010-back \n 1,2,...,9,10-add or remove to court")
        vote_chooser = int(input())
        if vote_chooser == 0:
            print("ok!")
            if player_num >= 1:
                print("say player1 vote")
                player1_vote = int(input())
        elif vote_chooser == 1010:
            day()
        elif vote_chooser == 1:
            print("for first use 0 or 1010")
            vote()

			

def show_role() :
    if player_num>=1 :
        print("sleep please!")
        playsound("timer.wav")
        playsound(player_sound)
        playsound(sound_1)
        playsound(stand_up_sound)
        print("your role is " , player1 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_1)
        playsound(sleep_sound)


    if player_num>=2 :
        playsound(player_sound)
        playsound(sound_2)
        playsound(stand_up_sound)
        print("your role is " , player2 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_2)
        playsound(sleep_sound)

    if player_num>=3 :
        playsound(player_sound)
        playsound(sound_3)
        playsound(stand_up_sound)
        print("your role is " , player3 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_3)
        playsound(sleep_sound)

    if player_num>=4 :
        playsound(player_sound)
        playsound(sound_4)
        playsound(stand_up_sound)
        print("your role is " , player4 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_4)
        playsound(sleep_sound)

    if player_num>=5 :
        playsound(player_sound)
        playsound(sound_5)
        playsound(stand_up_sound)
        print("your role is " , player5 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_5)
        playsound(sleep_sound)

    if player_num>=6 :
        playsound(player_sound)
        playsound(sound_6)
        playsound(stand_up_sound)
        print("your role is " , player6 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_6)
        playsound(sleep_sound)

    if player_num>=7 :
        playsound(player_sound)
        playsound(sound_7)
        playsound(stand_up_sound)
        print("your role is " , player7 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_7)
        playsound(sleep_sound)

    if player_num>=8 :
        playsound(player_sound)
        playsound(sound_8)
        playsound(stand_up_sound)
        print("your role is " , player8 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_8)
        playsound(sleep_sound)
    

    if player_num>=9 :
        playsound(player_sound)
        playsound(sound_9)
        playsound(stand_up_sound)
        print("your role is " , player9 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_9)
        playsound(sleep_sound)

    if player_num>=10 :
        playsound(player_sound)
        playsound(sound_10)
        playsound(stand_up_sound)
        print("your role is " , player10 , "\n press enter")
        input()
        playsound(player_sound)
        playsound(sound_10)
        playsound(sleep_sound)



def night() :
    print()

def day() :
    print(' 1-timer \n 2-vote \n 3-show role \n 4-night')
    day_choooser=int(input())
    if day_choooser==1 :
        timer()
    if day_choooser==2 :
        vote()
    if day_choooser==3 :
        show_role()
    if day_choooser==4 :
        night()


day()