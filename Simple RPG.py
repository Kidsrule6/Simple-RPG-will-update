#Hello, this is a simple RPG. Enjoy!


#Note to self -5/13/2025. In balancing stuff since I put nums in, I've realized that the elf is weak bc it was supposed to get racial spells. The drow and the high will both get extra spells, but the others will be normal subraces.
#Note to self -7/28/2025. Thank you for asking about myself! I'm currently driving in our RV, writing this note! I don't have any internet, so this is the best that I can do. Anyway, if you ever add a buff, copper dragonling's breath has a chance to give any random effect, so put it there if you've made one recently.


#For other_coders/future_self: Whenever an effect from a monster or yourself is set to "non", instead of "none", that's because the longer the effect is, the lower chance that the monster trip/debuffs you.
    #The above only applies if the stat is above 3 characters.

import sys
import random
import time
from datetime import datetime
import uuid


p_max_health=random.randint(40, 60)
p_max_mana=random.randint(0, 1)
p_energy=0
p_classes=[]
p_AB=random.randint(0, 3) #it stands for Attack Bonus
p_race="NA"
p_race_charges=0
p_max_race_charges=0
p_max_armor=random.randint(1, 4)
p_DR=random.choice([0, 0, 0, 0, 0, 0, 5, 6, 7]) #it stands for Damage Reduction
p_speed=0
p_max_speed=random.randint(-1, 2)
p_lv=0
input_var=0
save_code=0
save_list=[]
mon1_effect='non'
p_effect='non'
mon1_race="Human"
mon1_dmg=0
mon1_perma_effect='non'
mon1_max_hp=0
did_p_use_ml="non"
mon1_hp=0
quest="non"
num_of_quests=0
p_coins=0
turns_lasted=0
p_loot=0
p_insurance=0
mon1_hp_last_turn=0
g=0 #this is a var for the shaman in "def mon1_turn()"

def scramble_code(t):
    global scrambled
    machine_id=uuid.getnode()
    scrambled=""
    r=len(str(machine_id))
    r-=1
    while r>0:
        input_var=str(int(str(machine_id)[r])+t)
        scrambled=scrambled+input_var
        r-=1

def rest():
    global p_max_health, p_max_speed, p_speed, p_health, p_mana, p_max_mana, p_energy, p_AB, p_AB_temp, p_effect, mon1_perma_effect, mon1_effect, p_max_race_charges, p_race_charges, p_race, did_p_use_ml, mon1_race, p_armor, p_max_armor
    p_health=p_max_health
    p_mana=p_max_mana
    p_energy=0
    p_AB_temp=p_AB
    p_speed=p_max_speed
    p_armor=p_max_armor
    if p_race=="Copper Dragonling":
        p_max_race_charges==random.randint(2, 4)*random.randint(1, 3)
        if p_max_race_charges==2:
            p_max_race_charges+=1
        p_max_race_charges+=random.randint(-1, 1)
        if random.randint(1, 3)==1:
            p_max_race_charges+=1
    elif p_race=="Mind Flayer":
        did_p_use_ml="non"
    p_race_charges=p_max_race_charges
    p_max_health=int(p_max_health)

def settings(w):
    global sleep_setting, input_var, difficulty
    if w=="First":
        while True:
            input_var=input("What difficulty would you like to do? Inputs are 'easy', 'normal' and 'hard'.\n>>>")
            input_var=input_var.lower()
            if input_var=="easy" or input_var=="e":
                difficulty="e"
                break
            elif input_var=="normal" or input_var=="n":
                difficulty="n"
                break
            elif input_var=="hard" or input_var=="h":
                difficulty="h"
                break
            else:
                print("The only acceptable inputs are 'easy', 'normal' and 'hard'.")
    while True:
        input_var=input("Do you want there to be pause before selecting races/classes/points? (This is used to not make mistakes while spamming.)\n>>>")
        input_var=input_var.lower()
        if input_var=="yes" or input_var=="y":
            sleep_setting="y"
            break
        elif input_var=="no" or input_var=="n":
            sleep_setting="n"
            break
        else:
            print("The only acceptable inputs are 'yes' and 'no'.")
    while True:
        input_var=input("Do you want there to be pause during combat? (This is used to make the combat more realistic.)\n>>>")
        input_var=input_var.lower()
        if input_var=="yes" or input_var=="y":
            sleep_setting+="y"
            break
        elif input_var=="no" or input_var=="n":
            sleep_setting+="n"
            break
        else:
            print("The only acceptable inputs are 'yes' and 'no'.")

def enter_town():
    global num_of_quests, quest, p_coins
    num_of_quests=int(random.uniform(1+p_lv/6, 2+p_lv/4))
    if quest[0]=="-":
        input_var=quest[1:]
        quest=input_var
    if quest[0]=="0":
        if "point" in quest:
            input_var=0
            x=0
            while quest[input_var]!=">":
                input_var+=1
            input_var+=2
            if quest[input_var+1]==" ":
                x+=int(quest[input_var])
            else:
                x+=int(quest[input_var])*10
                x+=int(quest[input_var+1])
            while x>0:
                points("quest")
                x-=1
            quest="non"
        elif "coin" in quest:
            input_var=0
            while quest[input_var]!=">":
                input_var+=1
            input_var+=2
            if quest[input_var+1]!=" ":
                p_coins+=int(quest[input_var])
            elif quest[input_var+2]!=" ":
                p_coins+=int(quest[input_var])
                p_coins+=int(quest[input_var-1])*10
            elif quest[input_var+3]!=" ":
                p_coins+=int(quest[input_var])
                p_coins+=int(quest[input_var-1])*10
                p_coins+=int(quest[input_var-2])*100
            else:
                p_coins+=int(quest[input_var])
                p_coins+=int(quest[input_var-1])*10
                p_coins+=int(quest[input_var-2])*100
                p_coins+=int(quest[input_var-3])*1000
            quest="non"
        else:
            print("Somehow, you don't have coin/point as a reward? Ending simulation.")
            sys.exit()
    if num_of_quests==1:
        print("You enter a town. They have 1 shop. Each shop, you can visit once.")
    else:
        print(f"You enter a town. They have {num_of_quests} shops in town. Each shop, you can visit once.")
    town()

def town():
    global num_of_quests, p_coins, p_lv, p_max_speed, p_max_armor, p_AB, p_max_mana, p_max_health, p_loot, p_insurance
    input_var="You're still at a town. What do you want go do? Inputs are 'examine', 'settings', "
    if num_of_quests>0:
        input_var+="'quests', "
    input_var+="'shop', and 'leave'.\n>>>"
    input_var=input(input_var)
    input_var=input_var.lower()
    if input_var=="settings" or input_var=="setting" or input_var=="se":
        settings("later")
    elif input_var=="quests" or input_var=="quest" or input_var=="q":
        if num_of_quests>0:
            talk_to_villager()
        else:
            print("You've visited all the shops in the town.")
    elif input_var=="shop" or input_var=="sh":
        shop()
    elif input_var=="examine" or input_var=="e":
        print(f"Your stats are, {p_max_health} hp, {p_max_mana} mana, {p_AB}AB, {p_max_armor} armor, {p_max_speed} speed, {p_DR} DR, {p_loot} loot.\nYour extra stats are {p_lv} level, ${p_coins}, {num_of_quests} shop(s), Quest: {quest}, Insurance: {p_insurance}.")
        input_var=""
        if p_classes.count("Berserker")>0:
            input_var+=(f'Lv{p_classes.count("Berserker")} Berserker ')
        if p_classes.count("Fighter")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Fighter")} Fighter ')
        if p_classes.count("Tank")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Tank")} Tank ')
        if p_classes.count("Mage")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Mage")} Mage ')
        if p_classes.count("Cleric")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Cleric")} Cleric ')
        if p_classes.count("Monk")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Monk")} Monk ')
        if p_classes.count("Shaman")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Shaman")} Shaman ')
        if p_classes.count("Hunter")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Hunter")} Hunter ')
        if p_classes.count("Spellsword")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Spellsword")} Spellsword ')
        if p_classes.count("Alchemist")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Alchemist")} Alchemist ')
        if p_classes.count("Pyromancer")>0:
            if input_var!="":
                input_var=input_var[:-1]
                input_var+=", "
            input_var+=(f'Lv{p_classes.count("Pyromancer")} Pyromancer ')
        input_var=input_var[:-1]
        print(input_var)
    elif input_var=="leave" or input_var=="l":
        return
    else:
        print("You didn't enter a correct answer. You're still in the town.")
    town()

def shop():
    global p_coins, p_lv, p_insurance
    input_var=6*p_lv+42
    insurance_cost=12+p_lv*6
    premium_insurance_cost=59+p_lv*21
    input_var=input(f"Hello! What would you like to buy?\nPoints: ${input_var}\nInsurance: ${insurance_cost} or ${premium_insurance_cost}\nYou have ${p_coins}\n>>>")
    input_var=input_var.lower()
    if input_var=="points" or input_var=="p":
        if p_coins>=6*p_lv+42:
            p_coins-=6*p_lv+42
            points("shop")
            shop()
        else:
            print("You don't have enough coins.")
    elif input_var=="insurance" or input_var=="i":
        input_var=input(f"Which Insurance level would you like to buy? You have {p_insurance} insurance(s). (P.S. Insurance doesn't stack.)\nPremium Insurance: ${premium_insurance_cost}\nInsurance: ${insurance_cost}\nYou have ${p_coins}.\n>>>")
        input_var=input_var.lower()
        if input_var=="insurance" or input_var=="i":
            if p_coins>=insurance_cost:
                p_coins-=insurance_cost
                p_insurance=2
            else:
                print("You don't have enough coins.")
        elif input_var=="premium insurance" or input_var=="premium" or input_var=="pi" or input_var=="p":
            if p_coins>=premium_insurance_cost:
                p_coins-=premium_insurance_cost
                p_insurance=3
            else:
                print("You don't have enough coins.")
        else:
            print("That's not an insurance level!")
    elif input_var=="shop":
        print("Haha, lol. I do have a shop for sale, but trust me, you'd rather use your combat skills than be in my position. Have fun with your easter egg!")
    else:
        print("We don't have whatever you put... sorry.")

def talk_to_villager():
    global quest, num_of_quests, num_of_quests, p_coins
    input_var=input("Hi! I do not have a name, as I recognize myself as a NPC in your quest. Speaking of quests, would you like to take this quest? Inputs are 'yes', 'no' and 'work'.  If you select work, you get some money from me, but I won't give you a quest.\n(Mistyping will cause you to lose your quest.)\n>>>")
    input_var=input_var.lower()
    if input_var=="yes" or input_var=="y":
        num_of_quests-=1
        x=""
        c=""
        input_var="My quest is for you to "
        q=random.randint(1, 9)
        if q==1:
            c+="Kill "
            x=random.randint(3, 5)
            c+=str(x)
            c+=" humans."
            x=str(x)
            x+="Human"
        elif q==2:
            c+="Kill "
            x=random.randint(2, 4)
            c+=str(x)
            c+=" orcs."
            x=str(x)
            x+="Orc"
        elif q==3:
            c+="Kill "
            x=random.randint(1, 3)
            c+=str(x)
            c+=" minotaur."
            x=str(x)
            x+="Minotaur"
        elif q==4:
            c+="Kill "
            x=random.randint(3, 4)
            c+=str(x)
            c+=" elf."
            x=str(x)
            x+="Elf"
        elif q==5:
            c+="Kill "
            x=random.randint(2, 3)
            c+=str(x)
            c+=" fairy."
            x=str(x)
            x+="Fairy"
        elif q==6:
            c+="Kill "
            x=random.randint(1, 2)
            c+=str(x)
            c+=" troll."
            x=str(x)
            x+="Troll"
        elif q>6 and q<10:
            c+="Kill "
            x=random.randint(11, 14)
            c+=str(x)
            c+=" monsters."
            x=str(x)
            x+="Monsters"
        c+=" Your reward is "
        q=random.randint(1, 2)
        if q==1:
            z=random.randint(1, 2+p_lv//8)
            c+=str(z)
            c+=" point!"
            z=str(z)
            z+="point"
        elif q==2:
            z=random.randint(25+p_lv*14, 50+p_lv*25) #Don't question why these are weird numbers
            c+=str(z)
            c+=" coins!"
            z=str(z)
            z+="coins"
        print(c)
        input_var=input(f"Do you accept this quest? The inputs are 'yes' and 'no'.\nYour current quest is {quest}.\n>>>")
        input_var=input_var.lower()
        if input_var=="yes" or input_var=="y":
            quest=""
            if "Kill" in c:
                input_var=0
                while x[input_var]=="1" or x[input_var]=="2" or x[input_var]=="3" or x[input_var]=="4" or x[input_var]=="5" or x[input_var]=="6" or x[input_var]=="7" or x[input_var]=="8" or x[input_var]=="9" or x[input_var]=="0":
                    quest+=x[input_var]
                    input_var+=1
                if "human" in c:
                    quest+=" Human"
                elif "orc" in c:
                    quest+=" Orc"
                elif "elf" in c:
                    quest+=" Elf"
                elif "fairy" in c:
                    quest+=" Fairy"
                elif "troll" in c:
                    quest+=" Troll"
                elif "minotaur" in c:
                    quest+=" Minotaur"
                elif "monsters" in c:
                    quest+=" Monster"
            quest+=" -> "
            input_var=0
            while z[input_var]=="1" or z[input_var]=="2" or z[input_var]=="3" or z[input_var]=="4" or z[input_var]=="5" or z[input_var]=="6" or z[input_var]=="7" or z[input_var]=="8" or z[input_var]=="9" or z[input_var]=="0":
                quest+=z[input_var]
                input_var+=1
            if "point" in c:
                quest+=" point(s)"
            elif "coin" in c:
                quest+=" coins"
            print(f"Thank you for doing this! Your new quest is {quest}.")
    elif input_var=="work" or input_var=="w":
        input_var=12+p_lv*2
        x=30+p_lv*5
        input_var=input(f"I give you minimum {input_var} and at most, {x}. However, this costs a quest. Would you like to proceed?\n>>>")
        if input_var=="yes" or input_var=="y":
            input_var=random.randint(12+p_lv*2, 30+p_lv*5)
            p_coins+=input_var
            num_of_quests-=1
            input_var=random.randint(1, 7)
            if input_var==1:
                input_var="sweeping my house!"
            elif input_var==2:
                input_var="getting some water!"
            elif input_var==3:
                input_var="helping on the farm!"
            elif input_var==4:
                input_var="taking the garbage out!"
            elif input_var==5:
                input_var="making dinner!"
            elif input_var==6:
                input_var="defending me!"
            elif input_var==7:
                input_var="sharing your tales!"
            print(f"Thanks for {input_var}")
    print("Ok, goodbye!")

def tutorial():
    while True:
        input_var=input("Ok, first thing. Instead of putting 'yes', you can put the first letter of the response, and it'll work. For example, put 'o' for 'ok' to go to the next one.\n>>>")
        input_var=input_var.lower()
        if input_var=="o":
            break
        else:
            print("You need to put the first letter of 'ok' as the input.")
    print("It doesn't matter if you use caps or not. Most inputs don't care.")
    while True:
        input_var=input("There are a couple of stats you need to memorize. AB stands for attack bonus. Mana is only useful for spellcasters. DR stands for damage reduction.\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    print("There's many more stats that usually don't need explaining. There's also loot that increases the money you get per kill.")
    while True:
        input_var=input("If you attack, the game takes your AB stat, adds 2 or 3 randomly, then compares it to the monster's armor stat. If yours is higher, you hit!\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    print("The attacking rule also applies to the monster.")
    while True:
        input_var=input("Your other attack move is Trip. It takes your AB stat, and SUBTRACTS 1 or 2 randomly. But if you hit, it knocks them prone, skipping most of their turns.\nPut 'trip' into this to learn more.\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        elif input_var=="t" or input_var=="trip":
            print("In order to get up if you're tripped, the game takes your speed stat, and adds numbers to it or smth. TLDR, the higher speed you have, the less you stay tripped.\nElves are a monster race that specializes in speed. This means if you trip them, they'll get up faster.")
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    print("Speed is useful for 1 other thing. If you have more speed than your opponent, you start!")
    while True:
        input_var=input("DR, or damage reduction, doesn't actually reduce damage to 0. Infact, it'll never reduce it to 0. This is because of a recent nerf to DR builds.\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    while True:
        input_var=input("The examine stat only displays the stats previously mentioned. It'll also give you your turn back.\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    while True:
        input_var=input("The last usable action for every build is Charge. It gives you a buff called chrg. Don't ask why it's so short. It gives you +5 AB on your next attack.\nBut it goes away after your next attack. If you use it again, you get +1 AB until the end of the fight!\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Most of these tutorial information require 'ok' to move on, unless specified.")
    while True:
        input_var=input("Last thing; if you'd like a more indepth tutorial, visit my YouTube channel with a much better explanation on builds, spellcasting, and more!\nVisit https://www.youtube.com/@KORNKingdome for more info!\n>>>")
        input_var=input_var.lower()
        if input_var=="o" or input_var=="ok":
            break
        else:
            print("Pls sub <3")

def points(w):
    global input_var, p_max_health, p_max_mana, p_AB, p_max_speed, p_max_armor, p_DR, sleep_setting, mon1_hp, p_loot, difficulty, p_coins
    if w=="combat":
        if sleep_setting[:1]=="y":
            time.sleep(1.1)
        input_var=input(f"\nYou've defeated the {mon1_race}, and are able to choose a stat to put points into.\nHealth: {p_max_health}\nMana: {p_max_mana}\nAB: {p_AB}\nArmor: {p_max_armor}\nSpeed: {p_max_speed}\nDR: {p_DR}\nLoot: {p_loot}\nEnter your desired stat upgrade here:\n>>>")
    elif w=="Alc Pot":
        input_var=input(f"You got some points in the middle of the battle!!! Choose a stat.\nHealth: {p_max_health}\nMana: {p_max_mana}\nAB: {p_AB}\nArmor: {p_max_armor}\nSpeed: {p_max_speed}\nDR: {p_DR}\nLoot: {p_loot}\nEnter your desired stat upgrade here:\n>>>")
    elif w=="shop":
        input_var=input(f"You purchased some points! Choose a stat.\nHealth: {p_max_health}\nMana: {p_max_mana}\nAB: {p_AB}\nArmor: {p_max_armor}\nSpeed: {p_max_speed}\nDR: {p_DR}\nLoot: {p_loot}\nEnter your desired stat upgrade here:\n>>>")
    elif w=="quest":
        input_var=input(f"You completed your quest!! Choose a stat.\nHealth: {p_max_health}\nMana: {p_max_mana}\nAB: {p_AB}\nArmor: {p_max_armor}\nSpeed: {p_max_speed}\nDR: {p_DR}\nLoot: {p_loot}\nEnter your desired stat upgrade here:\n>>>")
    elif w=="difficulty":
        input_var=input(f"Your difficulty gave you another point! Choose a stat.\nHealth: {p_max_health}\nMana: {p_max_mana}\nAB: {p_AB}\nArmor: {p_max_armor}\nSpeed: {p_max_speed}\nDR: {p_DR}\nLoot: {p_loot}\nEnter your desired stat upgrade here:\n>>>")
    input_var=input_var.lower()
    p_max_health+=random.randint(0, 2)
    if input_var=="health" or input_var=="h" or input_var=="hp":
        p_max_health+=random.uniform(11+p_lv/1.6, 18+p_lv*1.16)
        p_max_health=int(p_max_health)
        print("You put your points into health!")
    elif input_var=="mana" or input_var=="m":
        p_max_mana+=random.randint(5, 7)
        print("You put your points into mana!")
    elif input_var=="ab":
        p_AB+=1
        print("You put your points into AB!")
    elif input_var=="armor" or input_var=="ar":
        p_max_armor+=random.randint(1, 2+p_lv//9)
        print("You put your points into armor!")
    elif input_var=="dr":
        p_DR+=random.uniform(2+p_lv/3.7, 6+p_lv*1.05)
        p_DR=int(p_DR)
        print("You put your points into DR!")
    elif input_var=="speed" or input_var=="spd" or input_var=="s":
        p_max_speed+=random.randint(1, 3)
        print("You put your points into speed!")
    elif input_var=="loot" or input_var=="l":
        p_loot+=random.randint(2, 7)
        print("You put your points into Loot!")
    else:
        if w=="shop":
            print("Rebooting back to shop...")
            p_coins+=6*p_lv+42
        else:
            print("Please re-enter your answer.")
            points(w)
        return
    if difficulty=="e" and random.randint(1, 4)==1 and w!="difficulty":
        points("difficulty")
    if difficulty=="n" and random.randint(1, 9)==1 and w!="difficulty":
        points("difficulty")

def choose_a_race():
    global p_max_health, p_max_mana, input_var, p_classes, p_AB, p_max_armor, p_DR, p_race, p_speed, p_lv, p_max_speed, p_max_race_charges, sleep_setting
    input_var=input("Which race do you want to become? The options are Human, Orc, Elf, Dwarf, Halfling, Gnome.\n>>>")
    input_var=input_var.lower()
    if input_var=="premium":
        input_var=input("Which race do you want to become? The options are Human (Devotee), Orc, Elf, Dwarf, Halfling, Gnome, Mind Flayer, War Bot, Dragonling, Aasimar.\n>>>")
    if input_var=="human" or input_var=="h" or input_var=="human; devotee" or input_var=="human devotee" or input_var=="hd":
        p_race="Human"
        p_max_speed+=random.randint(2, 5)
        p_DR+=random.randint(5, 8)
        p_max_health+=random.randint(30, 40)
        p_max_armor+=random.randint(1, 2)
        p_max_mana+=random.randint(0, 3)
        if input_var=="human; devotee" or input_var=="human devotee" or input_var=="hd":
            p_race="Human Devotee"
            p_max_speed+=random.randint(1, 3)
            p_AB+=1
            p_max_armor-=random.randint(2, 3)
            p_max_mana+=random.randint(0, 1)
        else:
            p_AB+=random.randint(0, 1)
    elif input_var=="orc" or input_var=="o":
        p_max_speed-=random.randint(2, 4)
        p_race="Orc"
        p_max_health+=random.randint(20, 62)
        p_AB+=random.randint(1, 2)
        p_max_mana-=random.randint(2, 3)
    elif input_var=="elf" or input_var=="e":
        p_race="Elf"
        input_var=input("Do you want to be a Forest elf, a High elf, a Stone elf, a Drow elf or a River elf?\n-Forest grants speed and hp.\n-High grants a lot of mana at the cost of a little armor.\n-Stone grants AC and mana.\n-Drow grants mana and damage at the cost of a little hp & armor.\n-River grants a random amount of every stat.\n>>>")
        input_var=input_var.lower()
        if input_var=="forest" or input_var=="f":
            input_var="Forest"
            p_max_health+=random.randint(20, 40)
            p_max_speed+=random.randint(3, 6)
            p_max_mana+=random.randint(0, 4)
        elif input_var=="high" or input_var=="h":
            input_var="High"
            p_max_mana+=random.randint(4, 8)
            p_max_armor-=random.randint(0, 2)
            p_max_speed+=random.randint(1, 4)
        elif input_var=="stone" or input_var=="s":
            input_var="Stone"
            p_max_armor+=random.randint(1, 3)
            p_max_health+=random.randint(20, 40)
            p_max_mana+=random.randint(2, 3)
            p_DR+=random.randint(4, 9)
        elif input_var=="drow" or input_var=="d":
            input_var="Drow"
            p_max_mana+=random.randint(3, 6)
            p_AB+=1
            p_max_health-=random.randint(6, 26)
            p_max_armor-=random.randint(0, 2)
        elif input_var=="river" or input_var=="r":
            input_var="River"
            p_max_armor+=random.randint(-3, 4)
            if random.randint(1, 4)==1:
                p_max_speed+=random.randint(3, 7)
            else:
                p_max_speed+=random.randint(-1, 6)
            p_max_health+=random.randint(-10, 22)*random.randint(4, 6)
            if random.randint(0, 4)>1:
                p_max_mana+=random.randint(4, 6)
            else:
                p_max_mana-=random.randint(2, 6)
            if random.randint(1, 3)==1:
                p_AB+=1
            else:
                if random.randint(1, 2)==1:
                    p_AB-=1
            if random.randint(0, 1)==0:
                p_DR+=random.randint(3, 12)
            else:
                p_DR-=random.randint(2, 9)
        else:
            print(f"There is no {input_var} elf available. Rebooting now...")
            choose_a_race()
            return
        p_race=str(input_var)+" Elf"
    elif input_var=="dwarf" or input_var=="d":
        p_max_speed-=random.randint(2, 4)
        p_max_mana-=random.randint(1, 2)
        input_var=input("Do you want to be a part of the Forge, Mountain or Valley heritage?\n-Forge grants DR.\n-Mountain grants hp, but at the cost of speed.\n-Valley grants speed, damage and a little health at the cost of armor.\n>>>")
        input_var=input_var.lower()
        if input_var=="mountain" or input_var=="m":
            input_var="Mountain"
            p_max_health+=random.randint(60, 90)
            p_max_speed-=random.randint(1, 2)
        elif input_var=="forge" or input_var=="f":
            input_var="Forge"
            p_DR+=random.randint(12, 17)
            p_max_speed-=random.randint(2, 3)
            p_max_mana-=random.randint(3, 6)
        elif input_var=="valley" or input_var=="v":
            input_var="Valley"
            p_max_health+=random.randint(20, 30)
            p_AB+=1
            p_max_speed+=random.randint(4, 6)
            p_max_armor-=random.randint(1, 2)
        else:
            print(f"There is no {input_var} dwarf available. Rebooting now...")
            choose_a_race()
            return
        p_race=str(input_var)+" Dwarf"
    elif input_var=="halfling" or input_var=="ha":
        p_race="Halfling"
        p_max_health+=random.randint(0, 15)
        p_max_armor+=random.randint(3, 4)
        p_max_speed+=random.randint(4, 6)
        p_max_mana+=random.randint(0, 1)
    elif input_var=="gnome" or input_var=="gn":
        p_race="Gnome"
        p_max_speed+=random.randint(-1, 2)
        p_max_mana+=random.randint(6, 9)
        p_max_health-=random.randint(20, 30)
        p_AB-=1
        p_max_armor+=random.randint(1, 2)
    elif input_var=="mind flayer" or input_var=="mf" or input_var=="mindflayer": #Premium
        input_var=input("Enter the Mind Flayer code:\n>>>")
        input_var=input_var.lower()
        scramble_code(1)
        if input_var==scrambled:
            p_race="Mind Flayer"
            print("Be warned, Mind Flayers get very hungry when not consuming brains. Thus, they take damage EVERY TURN.")
            p_max_speed-=random.randint(0, 3)
            p_max_mana+=random.randint(4, 8)
            p_max_health+=random.randint(40, 70)
            p_max_armor-=random.randint(0, 2)
            p_AB-=random.randint(0, 2)
            p_max_race_charges+=random.choice([4, 5, 5, 6, 6, 7])
        else:
            print("Not the code.")
            choose_a_race()
            return
    elif input_var=="war bot" or input_var=="wb" or input_var=="warbot": #Premium
        input_var=input("Enter the War Bot code:\n>>>")
        input_var=input_var.lower()
        scramble_code(2)
        if input_var==scrambled:
            p_race="War bot"
            p_max_speed-=random.randint(2, 5)
            p_max_health+=random.randint(20, 40)
            p_max_armor+=random.randint(1, 2)
            input_var=input("Do you want to be made as an Adamantine Plate, with a Steel Plate, or with a Mithril Plate?\n-Adamantine grants DR at the cost of mana and some speed.\n-Steel grants hp and a little speed at the cost of AB and mana.\n-Mithril only gives more armor.\n(btw), when entering your answer, just do the name, don't use 'plate'.)\n>>>")
            input_var=input_var.lower()
            if input_var=="adamantine" or input_var=="a":
                input_var="Adamantine"
                p_DR+=random.randint(10, 14)
                p_max_speed-=random.randint(0, 1)
                p_max_mana-=random.randint(1, 3)
            elif input_var=="steel" or input_var=="s":
                input_var="Steel"
                p_max_health+=random.randint(30, 40)
                p_max_speed+=random.randint(0, 2)
                p_AB-=1
                p_max_mana-=random.randint(0, 4)
            elif input_var=="mithril" or input_var=="m":
                input_var="Mithril"
                p_max_armor+=random.randint(1, 2)
                p_max_speed-=random.randint(1, 2)
                p_max_health-=10
            else:
                print("You entered a wrong answer. Rebooting now...")
                choose_a_race()
                return
            p_race=str(input_var)+" War Bot"
        else:
            print("Not the code.")
            choose_a_race()
            return
    elif input_var=="dr" or input_var=="dragonling" or input_var=="dl": #Premium
        input_var=input("Enter the Dragonling code:\n>>>")
        input_var=input_var.lower()
        scramble_code(3)
        if input_var==scrambled:
            input_var=input("What color of dragonling?\n-Red does more damage.\n-Blue gets mana each time you hit.\n-Green does DOT.\n-Black does percentage damage.\n-White reduces speed.\n-Brass gives a buff heals over time.\n-Bronze has a chance to trip.\n-Copper gives a random effect.\n-Gold heals instead of damage.\n-Silver has a chance to give you another turn.\n     (This is NOT like other inputs where you can enter the first letter.)\n>>>")
            input_var=input_var.lower()
            if input_var=="red":
                p_max_armor-=random.randint(1, 2)
                p_DR-=random.randint(4, 15)
                p_AB+=random.randint(1, 2)
                p_max_race_charges+=random.randint(3, 4)
                p_race="Red"
            elif input_var=="blue":
                p_DR+=random.randint(1, 5)
                p_max_speed-=random.randint(2, 4)
                p_max_race_charges+=random.randint(5, 6)
                p_max_health-=random.randint(10, 20)
                p_race="Blue"
            elif input_var=="green":
                p_max_health-=random.randint(35, 46)
                p_DR+=random.randint(12, 23)
                p_max_race_charges+=random.randint(1, 2)
                p_race="Green"
            elif input_var=="black":
                p_DR-=random.randint(2, 12)
                p_max_health+=random.randint(0, 30)
                p_max_race_charges+=random.randint(2, 3)
                p_race="Black"
            elif input_var=="white":
                p_max_armor+=random.randint(-1, 5)
                p_max_health+=random.randint(0, 20)
                p_max_race_charges+=random.randint(4, 5)
                p_race="White"
            elif input_var=="brass":
                p_race="Brass"
                p_max_health+=random.randint(20, 50)
                p_max_race_charges+=random.randint(1, 2)
                p_max_armor+=2
                p_DR+=random.randint(2, 6)
            elif input_var=="bronze":
                p_race="Bronze"
                p_max_race_charges+=random.randint(3, 6)
                p_max_race_charges*=2
                p_max_speed+=random.randint(0, 3)
                p_max_armor+=random.randint(-1, 2)
                p_DR+=random.randint(4, 9)
            elif input_var=="copper":#rando
                p_race="Copper"
                p_max_health+=random.randint(0, 40)
                p_max_armor+=random.randint(-2, 1)
                p_DR+=random.randint(0, 17)
                p_max_speed-=random.randint(-1, 2)
                p_max_race_charges+=random.randint(2, 4)*random.randint(1, 3)
                if p_max_race_charges==2:
                    p_max_race_charges+=1
            elif input_var=="gold":
                p_race="Gold"
                p_max_health+=random.randint(10, 60)
                p_max_speed-=random.randint(1, 4)
                p_max_race_charges=random.randint(4, 6)
            elif input_var=="silver":#extra turn
                p_race="Silver"
                p_max_armor-=random.randint(2, 3)
                p_max_speed+=random.randint(-1, 1)*3
                p_DR+=random.randint(1, 4)*random.randint(2, 3)
                p_max_race_charges=random.randint(2, 5)
            else:
                print("Type the whole thing out.")
                choose_a_race()
                return
            p_race+=" Dragonling"
            p_max_health+=random.randint(20, 40)
            p_max_armor-=random.randint(1, 4)
            p_DR+=random.randint(5, 11)
            p_max_speed-=random.randint(0, 1)
            p_max_race_charges+=random.randint(-1, 1)
            if random.randint(1, 3)==1:
                p_max_race_charges+=1
            if p_max_race_charges<1:
                p_max_race_charges=1
        else:
            print("Not the code.")
            choose_a_race()
            return
#Red: Embodiment of destruction and power.
#Blue: Masters of the desert, known for their cunning.
#Green: Deceivers of the forest, skilled in manipulation.
#Black: Shadows of the swamp, often associated with evil.
#White: Frozen terror, typically found in cold regions. 
#Brass: Talkative and friendly, often found in warm climates.
#Bronze: Known for their love of justice and order.
#Copper: Playful and mischievous, often engaging in tricks.
#Gold: Noble and wise, often acting as guardians.
#Silver: Compassionate and helpful, often aiding adventurers.
    elif input_var=="aasimar" or input_var=="aa": #Premium
        input_var=input("Enter the Aasimar code:\n>>>")
        input_var=input_var.lower()
        scramble_code(4)
        if input_var==scrambled:
            p_race="Aasimar"
            p_max_health+=random.randint(15, 25)
            p_max_mana+=random.randint(1, 3)
            p_max_race_charges+=random.randint(7, 10)
            p_max_speed+=random.randint(0, 1)
            p_max_armor-=random.randint(0, 1)
        else:
            print("Not the code.")
            choose_a_race()
            return
    else:
        print("You entered a wrong answer. Rebooting now...")
        choose_a_race()
        return
    if sleep_setting[:1]=="y":
        time.sleep(0.3)
    print(f"These are the stats that you have been given; {p_race}: Max health: {p_max_health}, Max mana: {p_max_mana}, Attack Bonus: {p_AB}, Armor: {p_max_armor}, Damage Reduction: {p_DR}, Speed: {p_max_speed}.")

def level_up():
    global p_max_health, p_mana, p_max_mana, p_energy, input_var, p_classes, p_AB, p_max_armor, p_DR, p_race, p_lv, j, p_max_speed, sleep_setting, p_max_race_charges, p_loot
    if sleep_setting[:1]=="y":
        time.sleep(0.8)
    while True:
        input_var=input("Which class would you like to level up? The options are Berserker, Fighter, Cleric, Tank, Monk, Mage.\n>>>")
        input_var=input_var.lower()
        if input_var=="premium":
            input_var=input("Which class would you like to level up? The options are Berserker, Fighter, Cleric, Tank, Monk, Mage, Shaman, Hunter, Spellsword, Alchemist, Pyromancer.\n>>>")
            input_var=input_var.lower()
        if input_var=="berserker" or input_var=="b":
            input_var="Berserker"
            p_max_health+=random.randint(20, 67)
            p_max_armor+=random.randint(-1, 2)
            p_AB+=random.randint(3, 5)
            p_max_speed+=random.randint(0, 2)
            p_loot+=random.randint(0, 2)
            break
        elif input_var=="fighter" or input_var=="f":
            input_var="Fighter"
            p_lv+=1 #If you're confused by this, don't be. At the end of fighter's upgrades, it reduces their level by 1.
            p_max_health+=random.randint(8, 31)
            p_DR+=random.randint(4+p_lv*random.randint(1, 2), 9+p_lv*random.randint(3, 5))
            p_max_armor+=random.randint(1, 2)
            p_AB+=random.randint(1, 2)
            p_max_speed-=random.randint(0, 2)
            p_loot+=random.randint(-1, 3)
            p_lv-=1 #If you're confused by this, read the hashtagged above.
            break
        elif input_var=="tank" or input_var=="ta":
            input_var="Tank"
            p_max_health+=random.randint(90, 130)
            p_DR+=random.randint(2, 5)
            p_max_armor+=random.randint(0, 1)
            p_loot+=random.randint(1, 4)
            break
        elif input_var=="mage" or input_var=="ma":
            input_var="Mage"
            p_max_speed+=random.randint(0, 1)
            p_max_mana+=random.randint(13, 17)
            p_max_health+=random.randint(17, 38)
            p_loot+=random.randint(1, 3)
            break
        elif input_var=="cleric" or input_var=="cl":
            input_var="Cleric"
            p_max_speed+=random.randint(0, 1)
            p_max_mana+=random.randint(11, 14)
            p_max_health+=random.randint(40, 55)
            p_max_armor+=random.randint(1, 2)
            p_AB+=random.randint(1, 2)
            p_DR+=random.randint(2, 4)
            p_loot+=random.randint(0, 4)
            break
        elif input_var=="monk" or input_var=="mo":
            input_var="Monk" #gets energy
            p_max_speed+=random.randint(3, 5)
            p_max_health+=random.randint(29, 47)
            p_max_armor-=1
            p_AB+=random.randint(1, 2)
            p_loot+=random.randint(3, 4)
            break
        elif input_var=="shaman" or input_var=="sh": #Premium
            if p_classes.count("Shaman")==0:
                input_var=input("Put your Shaman code here:\n>>>")
                input_var=input_var.lower()
                scramble_code(5)
                if input_var==scrambled:
                    input_var="Shaman" #gets energy
                    p_max_speed+=random.randint(3, 4)
                    p_max_mana+=random.randint(6, 8)
                    p_max_health+=random.randint(13, 27)
                    p_AB+=1
                    p_loot+=random.randint(2, 4)
                    break
                else:
                    print("Not the code.")
                    level_up()
                    return
            else:
                input_var="Shaman" #gets energy
                p_max_speed+=random.randint(3, 4)
                p_max_mana+=random.randint(6, 8)
                p_max_health+=random.randint(13, 27)
                p_AB+=1
                p_loot+=random.randint(2, 4)
                break
        elif input_var=="hunter" or input_var=="hu": #Premium
            if p_classes.count("Hunter")==0:
                input_var=input("Put your Hunter code here:\n>>>")
                input_var=input_var.lower()
                scramble_code(6)
                if input_var==scrambled:
                    input_var="Hunter"
                    p_max_speed+=random.randint(6, 12)
                    p_max_health+=random.randint(27, 54)
                    p_max_armor+=random.randint(0, 2)
                    p_AB+=2
                    p_loot+=random.randint(1, 4)
                    break
                else:
                    print("Not the code.")
                    level_up()
                    return
            else:
                input_var="Hunter"
                p_max_speed+=random.randint(6, 12)
                p_max_health+=random.randint(27, 54)
                p_max_armor+=random.randint(0, 2)
                p_AB+=2
                p_loot+=random.randint(1, 4)
                break
        elif input_var=="spellsword" or input_var=="ss": #Premium
            if p_classes.count("Spellsword")==0:
                input_var=input("Put your Spellsword code here:\n>>>")
                input_var=input_var.lower()
                scramble_code(7)
                if input_var==scrambled:
                    input_var="Spellsword"
                    p_max_health+=random.randint(20, 50)
                    p_max_mana+=random.randint(8, 11)
                    p_max_speed+=random.randint(1, 2)
                    p_max_armor+=random.randint(0, 1)
                    p_AB+=random.randint(2, 4+p_lv//4)
                    p_loot+=random.randint(1, 3)
                    break
                else:
                    print("Not the code.")
                    level_up()
                    return
            else:
                input_var="Spellsword"
                p_max_health+=random.randint(20, 50)
                p_max_mana+=random.randint(8, 11)
                p_max_speed+=random.randint(1, 2)
                p_max_armor+=random.randint(0, 1)
                p_AB+=random.randint(2, 4+p_lv//4)
                p_loot+=random.randint(1, 3)
                break
        elif input_var=="alchemist" or input_var=="al": #Premium
            if p_classes.count("Alchemist")==0:
                input_var=input("Put your Alchemist code here:\n>>>")
                input_var=input_var.lower()
                scramble_code(8)
                if input_var==scrambled:
                    input_var="Alchemist"
                    p_max_health+=random.randint(15, 35)
                    p_AB+=random.randint(0, 3)
                    p_max_speed+=random.randint(1, 3)
                    p_DR+=random.randint(2, 3)
                    p_max_armor+=random.randint(-1, 4)
                    p_loot+=random.randint(2, 3)
                    break
                else:
                    print("Not the code.")
                    level_up()
                    return
            else:
                input_var="Alchemist"
                p_max_health+=random.randint(15, 35)
                p_AB+=random.randint(0, 3)
                p_max_speed+=random.randint(1, 3)
                p_DR+=random.randint(2, 3)
                p_max_armor+=random.randint(-1, 4)
                p_loot+=random.randint(2, 3)
                break
        elif input_var=="pyromancer" or input_var=="py": #Premium
            if p_classes.count("Pyromancer")==0:
                input_var=input("Put your Pyromancer code here:\n>>>")
                input_var=input_var.lower()
                scramble_code(9)
                if input_var==scrambled:
                    input_var="Pyromancer"
                    p_max_health+=random.randint(22, 29)
                    p_AB+=random.randint(1, 2)
                    p_max_speed+=random.randint(2, 4)
                    p_max_mana+=random.randint(11, 15)
                    p_DR+=random.randint(2, 4)
                    p_max_armor+=random.randint(-1, 1)
                    p_loot+=1#random.randint(2, 3)
                    break
                else:
                    print("Not the code.")
                    choose_a_race()
                    return
            else:
                input_var="Pyromancer"
                p_max_health+=random.randint(15, 25)
                p_AB+=random.randint(0, 2)
                p_max_speed+=random.randint(0, 2)
                p_max_mana+=random.randint(10, 15)
                p_DR+=random.randint(0, 1)
                p_max_armor+=random.randint(-1, 1)
                p_loot+=1
                break
        else:
            print("You did not select a class. Rebooting now...")
    p_classes.append(input_var)
    input_var=""
    if p_classes.count("Berserker")>0:
        input_var+=(f'Lv{p_classes.count("Berserker")} Berserker ')
    if p_classes.count("Fighter")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Fighter")} Fighter ')
    if p_classes.count("Tank")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Tank")} Tank ')
    if p_classes.count("Mage")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Mage")} Mage ')
    if p_classes.count("Cleric")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Cleric")} Cleric ')
    if p_classes.count("Monk")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Monk")} Monk ')
    if p_classes.count("Shaman")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Shaman")} Shaman ')
    if p_classes.count("Hunter")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Hunter")} Hunter ')
    if p_classes.count("Spellsword")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Spellsword")} Spellsword ')
    if p_classes.count("Alchemist")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Alchemist")} Alchemist ')
    if p_classes.count("Pyromancer")>0:
        if input_var!="":
            input_var=input_var[:-1]
            input_var+=", "
        input_var+=(f'Lv{p_classes.count("Pyromancer")} Pyromancer ')
    input_var=input_var[:-1]
    input_var+=(f": Max health: {p_max_health}, Max mana: {p_max_mana}, Attack Bonus: {p_AB}, Armor: {p_max_armor}, Damage Reduction: {p_DR}, Speed: {p_max_speed}.")
    print(input_var)
    p_lv+=1
    p_loot+=random.randint(0, 2)
    if p_lv>=random.randint(6, 10) and "War Bot" in p_race and p_max_race_charges==0:
        p_max_race_charges+=random.randint(2, 3)
        print("You have now unlocked your rocket boost ability.")
    rest()

def create_monster():
    global p_lv, mon1_hp, mon1_spd, mon1_armor, mon1_AB, j, mon1_race, mon1_max_hp, difficulty
    p_room=1
    mon1_max_hp=0
    j=p_lv*random.randint(6, 13)
    while j>0:
        j-=1
        mon1_max_hp+=random.randint(1, 3)
    mon1_spd=p_lv+1
    mon1_armor=random.randint(0+p_lv//2, 2+p_lv*2)
    mon1_AB=random.randint(2, 3)
    mon_var_list=0
    m_difficulty=1
    if p_lv==2:
        m_difficulty+=1
    if p_lv==1:
        m_difficulty=3
    j=(2+p_lv//2)
    while j>0:
        j-=1
        m_difficulty+=random.uniform(3 + p_lv//2, 4 + p_lv*1.2)**random.choice([1, 1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.2, 1.2, 1.2, 1.2, 1.2, 1.2, 1.22, 1.3, 1.3, 1.4])
        if difficulty!="hard":
            m_difficulty-=p_lv
        elif difficulty=="easy":
            m_difficulty-=p_lv
    mon_stats=-1
    while m_difficulty>0:
        m_difficulty-=1
        mon_stats=random.randint(0, 5)
        if mon_stats==0:
            mon1_max_hp+=random.randint(15, 20)
        elif mon_stats==1:
            if mon1_spd<2+p_lv*1.9:
                mon1_spd+=random.choice([0, 0, 0, 1+p_lv/9])
            else:
                m_difficulty+=1
        elif mon_stats==5:
            mon1_armor+=random.choice([0, 0, 1+p_lv/14])
        elif mon_stats>1 and mon_stats<5:
            if mon1_AB<2*p_lv+2:
                mon1_AB+=random.choice([0, 0, 1+p_lv/12])
            else:
                m_difficulty+=1
        else: m_difficulty+=1
    #decides race
    input_var=random.randint(1, 16) #hello mr dev. If you're reading this, consider adding a giant. I'm not doing it rn because it'll take WAY too long considering quests and all.
    if input_var<=4:
        mon1_race="Human"
        mon1_AB=mon1_AB*random.randint(95, 120)/100
        mon1_max_hp=mon1_max_hp*random.randint(90, 120)/100
        mon1_spd=mon1_spd*random.randint(90, 130)/100
        mon1_armor=mon1_armor*random.randint(90, 115)/100
    elif input_var<=7:
        mon1_race="Orc"
        mon1_AB=mon1_AB*random.randint(160, 195)/100
        mon1_armor=mon1_armor*random.randint(40, 70)/100
        mon1_max_hp=mon1_max_hp*random.randint(120, 130)/100
        mon1_spd=mon1_spd*random.randint(80, 95)/100
    elif input_var<=10:
        mon1_race="Elf"
        mon1_AB=mon1_AB*random.randint(70, 120)/100
        mon1_max_hp=mon1_max_hp*random.randint(80, 90)/100
        mon1_spd=mon1_spd*random.randint(150, 180)/100
        mon1_armor=mon1_armor*random.randint(70, 90)/100
    elif input_var<=12:
        mon1_race="Minotaur"
        mon1_AB=mon1_AB*random.randint(130, 160)/100
        mon1_armor=mon1_armor*random.randint(35, 45)/100
        mon1_max_hp=mon1_max_hp*random.randint(105, 120)/100
        mon1_spd=mon1_spd*random.randint(60, 85)/100
    elif input_var<=13:
        mon1_race="Troll"
        mon1_AB=mon1_AB*random.randint(110, 125)/100
        mon1_armor=mon1_armor*random.randint(55, 70)/100
        mon1_max_hp=mon1_max_hp*random.randint(135, 160)/100
        mon1_spd=mon1_spd*random.randint(60, 85)/100
    elif input_var<=16:
        mon1_race="Fairy"
        mon1_AB=mon1_AB*random.randint(105, 125)/100
        mon1_armor=mon1_armor*random.randint(70, 105)/100
        mon1_max_hp=mon1_max_hp*random.randint(45, 70)/100
        mon1_spd=mon1_spd*random.randint(285, 305)/100
    else:
        print("Creation failed. Recreating the monster...")
        create_monster()
        time.sleep(0.15)
        return
    if p_lv%12==0:
        mon1_max_hp=mon1_max_hp*1.2
        mon1_spd=mon1_spd*1.05
        input_var=random.randint(1, 4)
        if input_var==1:
            mon1_race+=" Witch"
            mon1_AB=mon1_AB*random.randint(105, 130)/100
            mon1_armor=mon1_armor*random.randint(95, 105)/100
            mon1_max_hp=mon1_max_hp*random.randint(50, 60)/100
            mon1_spd=mon1_spd*random.randint(100, 115)/100
            print(f"The {mon1_race} approaches, summoning undead you kill with ease.")
            #witch #gets to revive itself. When it does, it causes a HUGE explosion dealing lots of damage. Also ignores armor after revive. Player gets like 3 or so turns after it dies to attack it more.
        elif input_var==2:
            mon1_race+=" Jugernaut"
            mon1_AB=mon1_AB*random.randint(130, 145)/100
            mon1_armor=mon1_armor*random.randint(115, 130)/100
            mon1_max_hp=mon1_max_hp*random.randint(130, 155)/100
            mon1_spd=mon1_spd*random.randint(75, 90)/100
            print(f"You hear the {mon1_race} aproaching from a mile away. With his giant sword and all his armor, he's not hard to track.")
        elif input_var==3:
            mon1_race+=" Assassin"
            mon1_AB=mon1_AB*random.randint(130, 160)/100
            mon1_armor=mon1_armor*random.randint(90, 115)/100
            mon1_max_hp=mon1_max_hp*random.randint(120, 140)/100
            mon1_spd=mon1_spd*random.randint(170, 265)/100
            print(f"{mon1_race} ambushes you and inflicts poison.")
        elif input_var==4:
            mon1_race+=" Shaman"
            mon1_AB=mon1_AB*random.randint(125, 145)/100
            mon1_armor=mon1_armor*random.randint(85, 105)/100
            mon1_max_hp=mon1_max_hp*random.randint(135, 145)/100
            mon1_spd=mon1_spd*random.randint(140, 170)/100
            print(f"The {mon1_race} is said to never have been defeated in the brawl arena. Someone must've hired it.")
            #shaman #if it isn't damaged for 1 turn, if it isn't damaged for the next turn, it heals to full and becomes untripped, if so. This ability works while tripped. If at above half health, gains hp equal to 1/4 of its max hp after full healing
    mon1_max_hp=mon1_max_hp//1
    mon1_armor=mon1_armor//1
    mon1_armor=int(mon1_armor)
    mon1_spd=mon1_spd//1
    mon1_spd=int(mon1_spd)
    mon1_hp=mon1_max_hp
    mon1_AB=int(mon1_AB)

def fight():
    global p_health, p_speed, mon1_hp, mon1_spd, mon1_armor, mon1_AB, mon1_effect, mon1_trip_bonus, p_trip_bonus, p_effect, mon1_race, sleep_setting, p_DR, mon1_perma_effect, turns_lasted, p_lv, p_loot, p_coins, quest, p_insurance, mon1_max_hp
    mon1_AB=mon1_AB//1
    mon1_AB=int(mon1_AB)
    mon1_trip_bonus=0
    turns_lasted=0
    p_trip_bonus=0
    p_effect="non"
    mon1_perma_effect="non"
    mon1_effect="non"
    if mon1_spd+random.randint(0, 4)<p_speed+random.randint(0, 4):
        print("You start. And because you start, you get a surprise attack!")
        p_effect="chrg"
        if sleep_setting[:2]=="yes":
            time.sleep(0.5)
        p_turn("non")
    elif mon1_spd+random.randint(0, 4)==p_speed+random.randint(0, 4):
        if random.randint(0, 1)>0:
            print("You start. And because you start, you get a surprise attack!")
            p_effect="chrg"
            if sleep_setting[:2]=="yes":
                time.sleep(0.5)
            p_turn("non")
        else:
            p_effect="non"
            print(f"The {mon1_race} starts.")
    else:
        p_effect="non"
        print(f"The {mon1_race} starts.")
    if "Witch" in mon1_race:
        while p_health>0 and mon1_hp>0:
            mon1_turn()
            if p_health>0 and mon1_hp>0:
                p_turn("non")
                turns_lasted+=1
                if turns_lasted>random.randint(90, 150): #Used to be 80-150, but then I remembered that tank builds need to charge alot.
                    print("This fight has lasted too long! What we are going to do is destroy the monster, then increase the dificulty. By far too much. Do not take this much time again.")
                    mon1_hp=0
                    p_lv+=random.randint(4, 7)
                    turns_lasted=0
        if mon1_hp<=0:
            print("The witch's body falls to the ground.")
            revival_cooldown=(random.randint(3, 6)-1)-p_lv/14
            if revival_cooldown<random.randint(0, 1): #should this be random, or just 1 always?
                revival_cooldown=1
            while revival_cooldown>0:
                revival_cooldown-=1
                print(revival_cooldown)
                if revival_cooldown<=1:
                    print('The "corpse" appears to be moving.')
                else:
                    print("The witch's corpse lies on the ground.")
                print(revival_cooldown)
                p_turn("non")
            print("The witch rises from the ground, eyes glowing purple, as an explosion blasts you away.")
            mon1_max_hp=mon1_max_hp*2
            mon1_hp+=mon1_max_hp
            input_var=p_lv
            revival_cooldown=0
            if mon1_hp<=0:
                print("The explosion didn't work because you overkilled it!")
                input_var=0
            while input_var>0:
                input_var-=1
                revival_cooldown-=random.randint(21, 26)
            revival_cooldown=abs(revival_cooldown)
            p_health-=revival_cooldown-p_DR
            mon1_AB+=random.randint(8*p_lv, 12*p_lv)
            mon1_spd+=random.randint(7*p_lv, 9*p_lv)
            while p_health>0 and mon1_hp>0:
                mon1_turn()
                if p_health>0 and mon1_hp>0:
                    p_turn("non")
                    turns_lasted+=1
                    if turns_lasted>random.randint(90, 150): #Used to be 80-150, but then I remembered that tank builds need to charge alot.
                        print("This fight has lasted too long! What we are going to do is destroy the monster, then increase the dificulty. By far too much. Do not take this much time again.")
                        mon1_hp=0
                        p_lv+=random.randint(4, 7)
                        turns_lasted=0
    else:
        while p_health>0 and mon1_hp>0:
            mon1_turn()
            if p_health>0 and mon1_hp>0:
                p_turn("non")
                turns_lasted+=1
                if turns_lasted>random.randint(90, 150): #Used to be 80-150, but then I remembered that tank builds need to charge alot.
                    print("This fight has lasted too long! What we are going to do is destroy the monster, then increase the dificulty. By far too much. Do not take this much time again.")
                    mon1_hp=0
                    p_lv+=random.randint(4, 7)
                    turns_lasted=0
    if mon1_hp<=0:
        turns_lasted=0
        input_var="You killed the "
        input_var+=mon1_race
        input_var+="!"
        if mon1_hp<p_lv*-1:
            input_var+=" And here's how much overkill you got: "
            mon1_hp=int(mon1_hp)
            input_var+=str(abs(mon1_hp))
            input_var+="!"
        print(input_var)
        if p_lv>=random.randint(5, 15) and p_lv<10:
            while True:
                input_var=input("You've reached the level when you can reset your build to unlock a premium race/class. If you do so, your build gets reset. Would you like to continue playing, or unlock a random premium race/class? Inputs are 'yes' and 'no'.\n>>>")
                input_var=input_var.lower()
                if input_var=="yes" or input_var=="y":
                    input_var=random.randint(1, 9)
                    machine_id=uuid.getnode()
                    if input_var==1: #Mind Flayer
                        scramble_code(input_var)
                        print(f"Here is your code for mind flayer: {scrambled}")
                    elif input_var==2: #War Bot
                        scramble_code(input_var)
                        print(f"Here is your code for war bot: {scrambled}")
                    elif input_var==3: #Dragonling
                        scramble_code(input_var)
                        print(f"Here is your code for Dragonling: {scrambled}")
                    elif input_var==4: #Aasimar
                        scramble_code(input_var)
                        print(f"Here is your code for Aasimar: {scrambled}")
                    elif input_var==5: #Shaman
                        scramble_code(input_var)
                        print(f"Here is your code for Shaman: {scrambled}")
                    elif input_var==6: #Hunter
                        scramble_code(input_var)
                        print(f"Here is your code for Hunter: {scrambled}")
                    elif input_var==7: #Spellsword
                        scramble_code(input_var)
                        print(f"Here is your code for Spellsword: {scrambled}")
                    elif input_var==8: #Alchemist
                        scramble_code(input_var)
                        print(f"Here is your code for Alchemist: {scrambled}")
                    elif input_var==9: #Pyromancer
                        scramble_code(input_var)
                        print(f"Here is your code for Pyromancer: {scrambled}")
                    sys.exit()
                elif input_var=="no" or input_var=="n":
                    break
        if mon1_hp<mon1_max_hp*-1.4:
            mon1_hp=mon1_max_hp*-1.4
        p_coins+=(random.randint(2, 1+p_lv*2)+p_loot+abs(mon1_hp)//random.randint(p_lv*20, p_lv*35))
        mon1_perma_effect="non"
        if p_effect=="trip":
            p_effect='non'
            p_DR+=4*p_lv+4
        p_effect="non"
        mon1_effect="non"
        if quest!="non":
            if quest[0]!="0":
                if "Human" in quest and "Human" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Orc" in quest and "Orc" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Elf" in quest and "Elf" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Fairy" in quest and "Fairy" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Troll" in quest and "Troll" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Minotaur" in quest and "Minotaur" in mon1_race:
                    t=quest[0]
                    t=int(t)
                    t=t-1
                    y=quest[1:]
                    quest=str(t)+str(y)
                elif "Monster" in quest:
                    if quest[1]==" ":
                        t=quest[0]
                        t=int(t)
                        t=t-1
                        y=quest[1:]
                        quest=str(t)+str(y)
                    else:
                        if quest[1]==0:
                            t=quest[1]
                            t=int(t)
                            t=t-1
                            t=quest[0]+str(t)
                            y=quest[2:]
                            quest=str(t)+str(y)
                        else:
                            quest=quest[1:]
                            t=quest[0]
                            t=int(t)
                            t=9
                            t=str(t)
                            quest=t+quest[1:]
                if quest[0]=="0":
                    print("Quest completed! Return to a village to claim your prize!")
            else:
                print("Quest completed! Return to a village to claim your prize!")
        points("combat")
        input_var=random.randint(1, 100)
        if quest[0]=="0": #if quest is done
            input_var+=4
        if input_var<=23:
            enter_town()
            rest()
    if p_health<=0:
        if p_insurance<1:
            print(f"You died. And here's how much hp he was at: {mon1_hp} hp. You reached level {p_lv} before dying.")
            sys.exit()
        else:
            p_insurance-=1
            print("Your insurance saved you!")
    else:
        if p_insurance>0 and random.randint(1, 4)<4:
            p_insurance-=1
            print("Your insurance is gone.")
    if p_health>0 and mon1_hp>0:
        print("Something broke. Please restart.")
        sys.exit()

def mon1_turn():
    global p_health, p_energy, p_classes, p_race, p_armor, p_DR, p_lv, mon1_hp, mon1_spd, mon1_armor, mon1_AB, mon1_effect, mon1_trip_bonus, p_effect, mon1_dmg, mon1_perma_effect, sleep_setting, mon1_max_hp, p_mana, mon1_hp_last_turn, g
    mon1_dmg=0
    if sleep_setting[:2]=="yes":
        time.sleep(1.1)
    if mon1_hp_last_turn==mon1_hp and "Shaman" in mon1_race:
        if g==1:
            if mon1_effect=="trip":
                mon1_effect="non"
                print(f"The {mon1_race}'s ability untripped it.")
            if mon1_hp>=mon1_max_hp//2:
                mon1_hp=mon1_max_hp*1.25
                print(f"The {mon1_race}'s ability healed it past full health.")
            else:
                mon1_hp=mon1_max_hp
                print(f"The {mon1_race}'s ability healed it to full health.")
            mon1_hp=int(mon1_hp)
        else:
            g=1
    else:
        g=0
    mon1_hp_last_turn=mon1_hp
    if mon1_race[:8]=="Minotaur" and mon1_max_hp*random.randint(2, 6)/10>mon1_hp:
        if "Rage" in mon1_effect:
            mon1_effect+="q"
        else:
            if mon1_effect=="trip":
                print("The monster is so full of Rage that they got up.")
            elif mon1_effect=="non" or mon1_effect[:3]=="Rag":
                print("The monster is enraged.")
            else:
                print("The monster is so full of Rage that they replaced their effect with Rage.")
            mon1_effect="Rage_q"
        if random.randint(1, 4)==1:
            mon1_perma_effect="non"
    if mon1_effect=='trip':
        if mon1_spd<=0:
            input_var=mon1_spd
            mon1_spd=0.001
        if mon1_spd**(random.randint(9, 12)*0.1)+mon1_trip_bonus+(mon1_trip_bonus//3)>=p_lv*random.randint(2, 3)-random.randint(0, 2):
            mon1_effect='non'
            print(f"The {mon1_race} got up.")
            mon1_trip_bonus=0
            mon1_armor+=2
            if mon1_spd>=p_lv*random.randint(random.choice([1, 2, 2, 2, 3, 3]), 7):
                print("...and has enough speed to try and attack you without penalty.")
            else:
                mon1_effect='-5 AB'
                print("...and has enough speed to try and attack you with a -5 penalty.")
                mon1_AB-=5
        else:
            mon1_trip_bonus+=1
            print(f"The {mon1_race} is tripped.")
        if mon1_spd==0.001:
            mon1_spd=input_var
    input_var="ignore_this_coders"
    if mon1_effect!='trip' and mon1_hp>0:
        if p_effect[:3]=="Ma3":
            p_armor+=p_classes.count("Mage")*2
        elif p_effect=="Ss5":
            p_DR+=p_classes.count("Spellsword")*5+p_lv*3
        elif p_effect[:3]=="Py5":
            p_DR+=p_classes.count("Pyromancer")*8
        if mon1_effect=="Cl5" and random.randint(1, 3)>1:
            mon1_spd-=random.randint(1, 2)
            print("Their speed has been reduced!")
        elif mon1_effect=="-5 AB":
            if random.randint(1, 5)==1:
                input_var="The monster missed"
                p_armor+=10000000000
        else:
            if random.randint(1, 12)==1:
                input_var="the monster missed"
                p_armor+=10000000000
        if mon1_AB+random.randint(-5, 7)>=p_armor:
            mon1_dmg=random.choice([0.5, 0.6, 0.7, 0.7, 0.9, 0.9, 1, 1, 1, 1, 1, 1, 1.1, 1.2, 1.7, 2])
            if p_effect=="HD1":
                mon1_dmg=random.choice([0.5, 0.6, 0.7, 0.7, 0.9, 0.9, 1, 1, 1, 1, 1, 1, 1, 1.1, 1.2, 1.3, 1.7, 2, 2.1, 2.4]) #the difference between this and the one above is that this one has a 2.4, 2.1, 1.3, and one more 1 than the list above
            if "Rage" in mon1_effect:
                mon1_dmg+=(len(mon1_effect)-6)*random.choice([0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09])
            if (random.randint(1, (len(p_effect)-2)//2 + 1)==1 or p_effect[:3]!="Ma7"): #Bro while coding this, I was stuck for like 5min bc of all the negatives.
                if mon1_dmg<0.9:
                    mon1_dmg=mon1_dmg*p_lv*random.randint(7, 12)-p_DR
                    if mon1_race[:5]=="Fairy":
                        mon1_dmg=mon1_dmg/2
                    if "Jugernaut" in mon1_race:
                        mon1_dmg*=3
                    if mon1_dmg<=1:
                        mon1_dmg=p_lv*1.5
                        mon1_dmg=mon1_dmg//1
                    if "Jugernaut" in mon1_race and random.randint(0, 1)==1:
                        mon1_dmg=0
                        print("The Jugernaut's attack was too slow for you.")
                    else:
                        if mon1_dmg>0:
                            p_health-=mon1_dmg
                        p_health=p_health//1
                        print(f"The {mon1_race} hit you (weakly)! You're now down to {p_health}hp.")
                elif mon1_dmg>1.5:
                    mon1_dmg=mon1_dmg*p_lv*random.randint(7, 12)-p_DR
                    if mon1_race[:5]=="Fairy":
                        mon1_dmg=mon1_dmg/2
                    if "Jugernaut" in mon1_race:
                        mon1_dmg*=3
                    if mon1_dmg<=1:
                        mon1_dmg=p_lv*random.randint(6, 8)
                    if "Jugernaut" in mon1_race and random.randint(0, 1)==1:
                        mon1_dmg=0
                        print("The Jugernaut's attack was too slow for you.")
                    else:
                        if mon1_dmg>0:
                            p_health-=mon1_dmg
                        p_health=p_health//1
                        print(f"The {mon1_race} CRIT! You're down to {p_health}hp.")
                else:
                    mon1_dmg=mon1_dmg*p_lv*random.randint(7, 12)-p_DR
                    if mon1_race[:5]=="Fairy":
                        mon1_dmg=mon1_dmg/2
                    if "Jugernaut" in mon1_race:
                        mon1_dmg*=3
                    if mon1_dmg<=1:
                        mon1_dmg=p_lv*random.randint(2, 7)
                    if "Jugernaut" in mon1_race and random.randint(0, 1)==1:
                        mon1_dmg=0
                        print("The Jugernaut's attack was too slow for you.")
                    else:
                        if mon1_dmg>0:
                            p_health-=mon1_dmg
                        p_health=p_health//1
                        print(f"The {mon1_race} hit you! You're down to {p_health}hp.")
                p_health=p_health//1
                chance_to_trip=random.randint(1, 13+len(p_effect)-3*2)
                if "Assassin" in mon1_race:
                    chance_to_trip-=3
                if chance_to_trip<=1 and p_effect!="Cl6":
                    if p_effect=="non" or p_effect=="trip":
                        if p_effect!="trip":
                            p_armor-=2
                            p_DR-=p_lv*4+4
                        p_effect="trip"
                        print("You have been tripped!")
                    else:
                        if p_effect=="Ss5":
                            p_DR-=p_classes.count("Spellsword")*5+p_lv*3
                        if p_effect[:3]=="Ma3":
                            p_armor-=p_classes.count("Mage")*2
                        p_effect="non"
                        print(f"The {mon1_race} debuffed you instead of tripping you.")
                if (p_classes.count("Shaman")>0 or p_classes.count("Monk")>0 or p_race=="Human Devotee") and p_energy>0:
                    if p_energy>=4+p_lv*2:
                        p_energy-=random.choice([1, 1, 1, 1, 1, 1, 2, 2, 3])
                        print(f"The {mon1_race} hit you well, making you lose concentration and energy, because you were at too high energy.")
                    elif random.randint(p_energy, 4+p_lv*2)==4+p_lv*2:
                        p_energy-=random.choice([1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3])
                        print(f"The {mon1_race} hit you well, making you lose concentration and energy.")
                    if p_energy<0:
                        p_energy=0
                if mon1_race[:5]=="Fairy" and p_mana>0 and ("Shaman" in p_classes or "Mage" in p_classes or "Cleric" in p_classes or "Spellsword" in p_classes or "Pyromancer" in p_classes):
                    p_mana-=random.uniform(p_lv*0.6, p_lv*1.8)
                    p_mana=int(p_mana)
                    print(f"The Fairy stole your mana. You're down to {p_mana} mana.")
                    if p_mana<0:
                        p_mana=0
            else:
                print(f"The {mon1_race} hit a clone, deleting it.")
                if p_effect=="Ma7q":
                    p_effect="non"
                elif len(p_effect)//2==1:
                    print(f"Somehow the p_effect became an odd num? Here's the str: {p_effect}. Here's a unique code to Ctrl + F this: o3m1bs8d.")
                else:
                    p_effect=p_effect[:-2]
            if sleep_setting[:2]=="yes":
                time.sleep(0.3)
            if p_effect[:3]=="Ma3" and len(p_effect)>3:
                w=len(p_effect)-3
                while w>0:
                    w-=1
                    mon1_hp-=random.randint(11, 17)+p_classes.count("Mage")
                print("Your thorns from Ma3 worked!")
            elif p_effect[:3]=="Py5" and len(p_effect)>3:
                input_var=len(p_effect)-3
                while input_var>0:
                    input_var-=1
                    if "Fire" in mon1_perma_effect:
                        mon1_perma_effect+="f"
                    else:
                        mon1_perma_effect="Firef"
                input_var=len(mon1_perma_effect)-4
                print(f"The monster took some fire damage. It's up to {input_var} fire!")
            if p_effect=="HD1":
                mon1_dmg=mon1_dmg*1.75
                mon1_hp-=mon1_dmg
                mon1_hp//1
                mon1_dmg=mon1_dmg//1
                p_effect="non"
                print(f"Using your stat, you dealt {mon1_dmg}hp. It's down to {mon1_hp}hp.")
        else:
            if input_var=="ignore_this_coders":
                print("The monster missed.")
            else:
                print(input_var)
        if p_effect[:3]=="Ma3":
            p_armor-=p_classes.count("Mage")*2
        elif p_effect=="Ss5":
            p_DR-=p_classes.count("Spellsword")*5+p_lv*3
        elif p_effect[:3]=="Py5":
            p_DR-=p_classes.count("Pyromancer")*8
    if p_armor>=9999999989:
        p_armor-=10000000000
    if mon1_perma_effect=="Ma9":
        mon1_hp-=random.randint(3*p_lv, 6*p_lv)
        if mon1_hp>0:
            print(f"Your Acid Splash spell dealt damage! It's now down to {mon1_hp} hp!")
        else:
            print(f"Your Acid Splash spell dealt damage!")
    elif mon1_perma_effect=="Green Breath":
        mon1_hp-=random.randint(1*p_lv, 5*p_lv)
        print(f"Your Breath Attack dealt damage! It's now down to {mon1_hp} hp!")
    elif mon1_perma_effect[:3]=="Ss4":
        if random.randint(0, len(mon1_perma_effect)+3)>4:
            mon1_spd-=random.randint(1, p_classes.count("Spellsword")//2+(len(mon1_perma_effect)-2)//2)
            print("Ss4 debuffed their speed.")
        if random.randint(0, len(mon1_perma_effect)+3)>4:
            mon1_armor-=random.randint(0, p_classes.count("Spellsword")//2+(len(mon1_perma_effect)-2)//2)
            print("Ss4 debuffed their armor.")
        if random.randint(0, len(mon1_perma_effect)+3)>4:
            mon1_AB-=random.randint(0, 1+p_classes.count("Spellsword")//random.randint(2, 4)+(len(mon1_perma_effect)-2)//3)
            print("Ss4 debuffed their AB.")
    if mon1_race[:5]=="Troll" and not mon1_hp<0:
        mon1_hp+=mon1_max_hp*random.uniform(0.020, 0.028)
        mon1_hp=int(mon1_hp)
        print(f"The {mon1_race} healed. It's up to {mon1_hp}.")
        if mon1_hp>mon1_max_hp:
            mon1_hp=mon1_max_hp
    p_health=p_health//1
    if mon1_effect=='-5 AB':
        mon1_AB+=5
        mon1_effect='non'

def p_turn(w):
    global p_health, p_mana, p_max_mana, p_energy, input_var, p_classes, p_AB, p_AB_temp, p_armor, p_DR, p_race, p_speed, p_lv, mon1_hp, mon1_spd, mon1_armor, mon1_AB, mon1_effect, p_effect, p_trip_bonus, mon1_dmg, did_p_use_ml
    p_DR=p_DR//1
    if p_race=="Mind Flayer" and did_p_use_ml!="Mind Leech":
        p_health-=random.randint(1*p_lv, 3*p_lv)+random.randint(10, 14)
    else:
        did_p_use_ml="non"
    if p_effect=="trip":
        if p_speed+p_trip_bonus+(p_trip_bonus//3)>=p_lv*random.randint(2, 3):
            p_effect='non'
            print("You got up!")
            p_armor+=2
            p_DR+=p_lv*4+4
            if p_speed>=p_lv*random.randint(2, 5):
                print("...and you have enough speed to try and attack without penalty.")
            else:
                p_effect='-5 AB'
                print("...and you while you did get up, you can't attack without a -5 penalty.")
        else:
            p_trip_bonus+=random.choice([0, 1, 1, 1, 1, 1, 1, 2, 2, 3,])
            print("You stay tripped.")
    elif p_effect=="Cl6":
        if p_mana>=1+p_lv//3+p_lv//2:
            if random.randint(1, 3)>1:
                p_mana-=1+p_lv//3+p_lv//2
            if random.randint(1, 5+p_classes.count("Cleric"))>=5:
                if mon1_effect=="trip":
                    mon1_armor+=2
                mon1_effect="trip"
                mon1_armor-=2
                print(f"With your celestial form, you knocked the {mon1_race} down.")
        else:
            print("You're out of mana, you leave your celestial self.")
            p_effect="non"
    elif p_effect[:3]=="Ma7":
        input_var=(len(p_effect)-2)//2
        while input_var>0:
            input_var-=1
            if random.randint(1, 3)!=1: #mon1_armor<=random.randint(-3, 5) + p_AB_temp:         #<--- That's hashtagged out because it's technically a spell and it shouldn't rely on AB. Plus, Mage doesn't get AB from leveling, so it's really iritating to code this, then the copies just miss every day because you don't have AB. Does that make sense?
                mon1_hp-=(random.randint(6*p_lv, 10*p_lv))
                print("The clone hit!")
            else:
                print("The clone missed.")
    elif p_effect=="Cl4":
        p_health+=random.randint(4*p_classes.count("Cleric"), 7*p_classes.count("Cleric"))#+p_classes.count("Cleric")*2
        print(f"The power of regeneration has healed you! You're up to {p_health} health.")
        if p_health>p_max_health:
            p_health=p_max_health
    elif p_effect=="Cl5" and random.randint(1, 4)==1:
        if mon1_effect!="Cl5":
            mon1_effect="Cl5"
            print(f"Your Cl5 buff debuffed the {mon1_race}!")
        else:
            print("The monster already has cl5, so you get to reduce their speed!")
            mon1_spd-=random.randint(0, 3)
    elif p_effect=="Ss5":
        input_var=p_lv
        while input_var>0:
            input_var-=1
            p_health-=random.randint(2, 7)
        print("You've lost health because of Ss5.")
    elif p_effect=="Ss1":
        p_speed+=random.randint(0, 2)
        print(f"You've gained speed because your effect! You're up to {p_speed} speed.")
    elif p_effect=="HD4":
        p_AB_temp-=1
        print(f"Your AB got reduced because of your buff. You now have {p_AB_temp}AB.")
    elif p_effect=="B&B":
        p_health+=random.randint(4+p_lv//3, 7+p_lv)
        print(f"You Brass Breath healed you! You're up to {p_health} health!")
        if p_health>p_max_health:
            p_health=p_max_health
    if "Assassin" in mon1_race:
        input_var=random.randint(1, 3)
        while input_var>0:
            input_var-=1
            p_health-=p_lv
        print("The Assassin poison damages you!")
    if p_effect!="trip" and p_health>0.001 and w!="NoXtrTurn":
        if "Shaman" in p_classes or "Monk" in p_classes or p_race=="Human Devotee":
            print(f"You have {p_energy} energy.")
        if "Shaman" in p_classes or "Mage" in p_classes or "Cleric" in p_classes or "Spellsword" in p_classes or "Pyromancer" in p_classes:
            print(f"You have {p_mana} mana/{p_max_mana} mana.")
        p_turn_pt2()

def p_turn_pt2():
    global p_max_health, p_health, p_mana, p_max_mana, p_energy, input_var, p_classes, p_AB, p_AB_temp, p_armor, p_DR, p_race, p_speed, p_lv, mon1_hp, mon1_spd, mon1_armor, mon1_AB, mon1_effect, p_effect, p_trip_bonus, mon1_dmg, mon1_perma_effect, mon1_race, p_max_race_charges, p_race_charges, mon1_max_hp, did_p_use_ml, p_max_speed, turns_lasted, p_loot, p_max_armor
    if p_effect[:3]=="Ma4":
        input_var=(f"\nThe {mon1_race}'s stats are {mon1_hp}hp/{mon1_max_hp}max hp, {mon1_AB}AB, {mon1_armor} armor, {mon1_spd} speed.\n")
        if mon1_effect=="non":
            input_var+=("And it doesn't have an effect.\n")
        else:
            input_var+=(f"And it's stat is {mon1_effect}.\n")
        if mon1_perma_effect!="non":
            input_var+=(f"And it's perma stat is {mon1_perma_effect}.\n")
        input_var+=(f"\nYour stats are {p_health}hp/{p_max_health}max hp, {p_AB_temp}AB, {p_armor} armor, {p_speed} speed")
        if p_DR!=0:
            input_var+=(f", {p_DR}DR")
            if p_DR<0:
                input_var+=(" (you have negative DR, so they get increased dmg)")
        if p_classes.count("Shaman")>0 or p_classes.count("Monk") or p_race=="Human Devotee":
            input_var+=(f", {p_energy} energy")
        input_var+=(f", {p_mana} mana/{p_max_mana} max mana")
        input_var+=(f".\nAnd your stat is {p_effect}.\n")
        print(input_var)
        input_var=input("Do you want to charge your Lightning Bolt, or release it?\n>>>")
        input_var=input_var.lower()
        if input_var=="charge" or input_var=="c":
            if p_mana>=p_classes.count("Mage"):
                p_mana-=p_classes.count("Mage")
                p_effect+="q"
                print("You charged your bolt.")
                return
            else:
                print("Because you don't have enough mana to charge up the Lightning Bolt, you're forced to fire it.")
                input_var="r"
        if input_var=="release" or input_var=="r":
            mon1_hp-=random.randint(5, 7)**((len(p_effect)-2)/2.3)*p_lv*random.choice([1, 1.1, 1.1, 1.2, 1.2, 1.2, 1.2, 1.3, 1.3, 1.3, 1.3, 1.4, 1.4, 1.5])+p_lv*4
            p_effect="non"
            mon1_hp=mon1_hp//1
            print("You released the Bolt.")
            return
        else:
            print("You entered a wrong answer. Rebooting now...")
            p_turn_pt2()
            return
    if p_effect!="trip":
        input_var="Actions: Attack, Trip, Examine, Charge"
        if p_classes.count("Shaman")>0 or p_classes.count("Monk") or p_race=="Human Devotee":
            input_var+=", Energy"
        if p_classes.count("Shaman")>0 or p_classes.count("Mage")>0 or p_classes.count("Spellsword")>0 or p_classes.count("Cleric")>0 or p_classes.count("Pyromancer")>0:
            input_var+=", Spellbook"
        if p_classes.count("Alchemist"):
            input_var+=", Bottle"
        if "Dragonling" in p_race and p_race_charges>0:
            input_var+=", Breath Attack"
        elif p_race=="Mind Flayer" and mon1_effect=="trip" and p_race_charges>0:
            input_var+=", Mind Leech"
        elif "War Bot" in p_race and p_race_charges>0:
            input_var+=", Rocket Blast"
        elif p_race=="Aasimar" and p_race_charges>0:
            input_var+=", Divine Healing"
        input_var+="\n>>>"
        input_var=input(input_var)
        input_var=input_var.lower()
        if (input_var=="breath attack" or input_var=="ba") and 'Dragonling' in p_race:
            #Red does more damage. Blue doesn't get any extra effect, but they do get MUCH more mana. Green does DOT. Black does percentage damage. White reduces speed.\nBrass gives a buff that heals over time. Bronze has a chance to trip. Copper gives a random effect. Gold heals instead of deals damage. Silver has a chance to give you another turn.
            if "Red" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(12*p_lv, 19*p_lv+18))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(10*p_lv, 14*p_lv+13))
                        print("You hit!")
                else:
                    print("You don't have enough charges for your Red Breath Attack.")
                    p_turn_pt2()
                return
            elif "Blue" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    p_mana+=random.randint(p_lv, p_lv*4)
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(9*p_lv, 13*p_lv))
                        p_mana+=random.randint(p_lv, p_lv*random.randint(2, 3))
                        print("You CRIT, dealing more damage and gaining more mana!")
                    else:
                        mon1_hp-=(random.randint(7*p_lv, 11*p_lv))
                        print("You hit!")
                    if p_mana>p_max_mana:
                        p_mana=p_max_mana
                else:
                    print("You don't have enough charges for your Blue Breath Attack.")
                    p_turn_pt2()
                return
            elif "Green" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(10*p_lv, 11*p_lv))
                        print("You CRIT, dealing more damage and inflicting DOT!")
                    else:
                        mon1_hp-=(random.randint(5*p_lv, 7*p_lv))
                        print("You hit, inflicting DOT!")
                    mon1_perma_effect="Green Breath"
                else:
                    print("You don't have enough charges for your Green Breath Attack.")
                    p_turn_pt2()
                return
            elif "Black" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=mon1_max_hp*random.randint(5, 8)/17
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=mon1_max_hp*random.randint(3, 5)/20
                        print("You hit!")
                    mon1_hp=int(mon1_hp)
                else:
                    print("You don't have enough charges for your Black Breath Attack.")
                    p_turn_pt2()
                return
            elif "White" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(8*p_lv, 15*p_lv))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(7*p_lv, 10*p_lv))
                        print("You hit!")
                    mon1_spd-=random.uniform(1+p_lv/6, 3+p_lv/4)
                    mon1_spd=int(mon1_spd)
                    print(f"You reduced its speed! It's down to {mon1_spd} speed!")
                else:
                    print("You don't have enough charges for your White Breath Attack.")
                    p_turn_pt2()
                return
            elif "Brass" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(10*p_lv, 13*p_lv))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(8*p_lv, 9*p_lv))
                        print("You hit!")
                    p_effect="B&B"
                else:
                    print("You don't have enough charges for your Brass Breath Attack.")
                    p_turn_pt2()
                return
            elif "Bronze" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(10*p_lv, 15*p_lv))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(8*p_lv, 13*p_lv))
                        print("You hit!")
                    if random.randint(1, 4+p_lv//2)>3:
                        mon1_effect="trip"
                        print("You tripped it!")
                        mon1_armor-=2
                else:
                    print("You don't have enough charges for your Bronze Breath Attack.")
                    p_turn_pt2()
                return
            elif "Copper" in p_race: #rando effect
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(9*p_lv, 15*p_lv))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(7*p_lv, 12*p_lv))
                        print("You hit!")
                    q=random.randint(1, 9)
                    if (p_classes.count("Shaman")+p_classes.count("Mage")+p_classes.count("Spellsword")+p_classes.count("Cleric")+p_classes.count("Pyromancer")<1) and q==1:
                        q=random.randint(2, 9)
                    if q==1:
                        p_mana+=2+p_max_mana//13
                        print("You gained mana!")
                    elif q==2:
                        mon1_spd-=random.randint(0, 1)
                        mon1_armor-=random.randint(0, 2)
                        mon1_AB-=random.randint(0, 3)
                        print("You cursed it!")
                    elif q==3:
                        input_var=mon1_hp/mon1_max_hp
                        q=mon1_effect
                        create_monster()
                        mon1_hp=input_var*mon1_max_hp
                        mon1_hp=int(mon1_hp)
                        mon1_effect=q
                        print("You randomized the monster!! Have fun with the new one!")
                    elif q==4:
                        mon1_hp-=p_health
                        p_health=p_health//2
                        print("You dealt damage equal to your health, then halved your health.")
                    elif q==5:
                        p_health+=(p_max_health*random.randint(1, 4))//11
                        print("You've healed a percentage of your health.")
                    elif q==6:
                        p_race_charges+=1
                        print("You got another Breath Attack charge!")
                    else:
                        print("You got a random effect!!")
                        input_var=random.randint(1, 18)
                        if input_var==1:
                            p_effect="Ma3"
                            q=random.randint(1, 3)
                            while q>0:
                                q-=1
                                p_effect+="q"
                        elif input_var==2:
                            p_effect="Ma7q"
                            q=random.randint(1, 4)
                            if q==1:
                                p_effect+="qq"
                        elif input_var==3:
                            p_effect="Cl4"
                        elif input_var==4:
                            p_effect="Cl5"
                        elif input_var==5:
                            p_effect="Cl6"
                        elif input_var==6:
                            p_effect="Ss1"
                        elif input_var==7:
                            p_effect="Ss3"
                        elif input_var==8:
                            p_effect="Ss5"
                        elif input_var==9:
                            p_effect="HD1"
                        elif input_var==10:
                            p_effect="HD4"
                        elif input_var==11:
                            p_effect="Rage_"
                            input_var=random.randint(2, 7)
                            while input_var>0:
                                input_var-=1
                                p_effect+="q"
                        elif input_var==12:
                            p_effect="B&B"
                        elif input_var==13:
                            p_effect="-5 AB"
                        elif input_var==14:
                            p_effect="chrg"
                        elif input_var==15:
                            p_effect="brew"
                            input_var=random.randint(0, 3)
                            while input_var>0:
                                input_var-=1
                                p_effect+="q"
                            print("This effect doesn't do anything unless you're a specific class.")
                        elif input_var==16:
                            p_effect="Dmg"
                            q=random.randint(2, 5)
                            while q>0:
                                q-=1
                                if random.randint(1, 7)==1:
                                    p_effect+="g"
                                elif random.randint(1, 4)==1:
                                    p_effect+="f"
                                else:
                                    p_effect+="s"
                                if random.randint(1, 4)==1:
                                    p_effect+="a"
                        elif input_var==17:
                            p_effect="PPot"
                        elif input_var==18:
                            p_effect="Py3"
                        elif input_var==18:
                            if p_effect=="Py5":
                                q=random.randint(1, 3)
                                while q>0:
                                    q-=1
                                    p_effect+="q"
                            else:
                                p_effect="Py5"
                        else:
                            p_effect="trip"
                        print(f"Your effect is now {p_effect}!")
                        if p_effect=="non": #debugging tests only
                            print(f"Hi there. This is the debugging commitee! Sorry for the interference, but for some reason, you didn't get an effect... If the developer is playing; {input_var}. That number should've determined what effect you got, but it decided to not work. If you could take a screenshot of this and the number specifically, then contact me with this screenshot, that would be appreciated! Thank you, and good luck on your simulation!")
                else:
                    print("You don't have enough charges for your Copper Breath Attack.")
                    p_turn_pt2()
                return
            elif "Gold" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        p_health-=(random.randint(14*p_lv, 18*p_lv))
                        print("You CRIT, dealing healing more!")
                    else:
                        p_health-=(random.randint(10*p_lv, 13*p_lv))
                        print("You hit!")
                    if p_health>p_max_health:
                        p_health=p_max_health
                else:
                    print("You don't have enough charges for your Gold Breath Attack.")
                    p_turn_pt2()
                return
            elif "Silver" in p_race:
                if p_race_charges>0:
                    p_race_charges-=1
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(12*p_lv, 16*p_lv))
                        print("You CRIT, dealing more damage!")
                    else:
                        mon1_hp-=(random.randint(10*p_lv, 13*p_lv))
                        print("You hit!")
                    if random.randint(1, 4+p_lv//3)>2:
                        print("You go again!")
                        p_turn_pt2()
                        return
                else:
                    print("You don't have enough charges for your Silver Breath Attack.")
                    p_turn_pt2()
                return
            else:
                print("What type of dragonling are you?!??")
                p_turn_pt2()
                return
        else:
            if input_var=="breath attack" or input_var=="ba":
                print("You aren't a dragonling!")
                p_turn_pt2()
                return
        if input_var=="examine" or input_var=="ex" or input_var=="e":
            if p_effect=="chrg":
                p_AB_temp+=5
            elif p_effect=="-5 AB":
                p_AB_temp-=5
            elif p_effect[:3]=="Ma3":
                p_armor+=p_classes.count("Mage")*2
            elif p_effect[:3]=="Py5":
                p_DR+=p_classes.count("Pyromancer")*8
            p_DR=p_DR//1
            q=(f"The {mon1_race}'s stats are {mon1_hp}hp/{mon1_max_hp}max, {mon1_AB}AB, {mon1_armor}")
            if mon1_effect=="trip":
                q+="*"
            q+=(f" armor, {mon1_spd} speed.\n")
            if mon1_effect=="non":
                q+=("And it doesn't have an effect.\n")
            else:
                q+=(f"And it's stat is {mon1_effect}.\n")
            if mon1_perma_effect!="non":
                q+=(f"And it's perma stat is {mon1_perma_effect}.\n")
            q+=(f"\nYour stats are {p_health}hp/{p_max_health}max hp, ")
            q+=str(p_AB_temp)
            if p_effect=="chrg" or p_effect=="-5 AB":
                q+="*"
            q+=(f"AB, {p_armor}")
            if p_effect[:3]=="Ma3":
                q+=("*")
            q+=(f" armor, {p_speed} speed")
            if p_DR!=0:
                q+=(f", {p_DR}")
                if p_effect[:3]=="Py5":
                    q+="*"
                q+=("DR")
                if p_DR<0:
                    q+=(" (you have negative DR, so they get increased dmg)")
            if p_classes.count("Shaman")>0 or p_classes.count("Monk") or p_race=="Human Devotee":
                q+=(f", {p_energy} energy")
            if p_classes.count("Shaman")>0 or p_classes.count("Mage")>0 or p_classes.count("Spellsword")>0 or p_classes.count("Cleric")>0 or p_classes.count("Pyromancer")>0:
                q+=(f", {p_mana} mana/{p_max_mana} max mana")
            if p_max_race_charges>0:
                q+=(f", {p_race_charges} charges/{p_max_race_charges} max charges")
            q+=(".\n")
            if p_effect=="non":
                q+=("And you don't have an effect.")
            else:
                q+=(f"And your stat is {p_effect}.")
            print(q)
            if p_effect=="chrg":
                p_AB_temp-=5
            elif p_effect=="-5 AB":
                p_AB_temp+=5
            elif p_effect[:3]=="Ma3":
                p_armor-=p_classes.count("Mage")*2
            elif p_effect[:3]=="Py5":
                p_DR-=p_classes.count("Pyromancer")*8
            p_turn_pt2()
            return
        elif input_var=="turns_lasted": #Debugging only
            print(f"Debug Message: It is {turns_lasted} turns.")
            p_turn_pt2()
            return
        elif input_var=="hdecn": #Debugging only
            mon1_hp=0
            print("Congrats on the one-shot kill. You now have a 1/4th chance that you die.")
            if random.randint(1, 4)==1:
                print("Lol, it rolled the 1. You die now. (And if you don't your max hp is at -300. DONT CHEAT.)")
                p_max_health=-300
        elif (input_var=="mind leech" or input_var=="ml") and mon1_effect=="trip" and p_race_charges>0 and p_race=="Mind Flayer":
            print("Automatic hit! You drained speed, AB, and you gained some health and mana.")
            did_p_use_ml="Mind Leech"
            p_race_charges-=1
            mon1_spd-=random.randint(0, 3)
            mon1_AB-=random.randint(2, 3)
            p_mana+=p_lv*random.uniform(2.2, 4.7)
            if p_mana>p_max_mana:
                p_mana=p_max_mana
            if p_health<=p_max_health:
                p_health+=p_lv*random.randint(6, 11)+random.randint(18, 35)
                if p_health>p_max_health:
                    p_health=p_max_health
            p_health=p_health//1
            p_mana=p_mana//1
        elif (input_var=="rocket blast" or input_var=="rb") and p_race_charges>0 and "War Bot" in p_race:
            p_race_charges-=1
            mon1_hp-=(random.randint(18*p_lv, 24*p_lv))
            input_var="Your Rocket Blast dealt a lot of damage"
            if random.randint(1, 5)>2:
                if p_effect!="trip":
                    p_armor-=2
                    p_DR-=p_lv*4+4
                p_effect="trip"
                input_var+=", but it also knocked you down due to recoil"
            if random.randint(1, 3)>2:
                mon1_spd-=random.randint(2, 4)
                input_var+=" and it reduced their speed"
            if random.randint(1, 3)==1:
                if mon1_effect!="trip":
                    mon1_armor-=2
                mon1_effect="trip"
                input_var+=" and tripped them"
            input_var+=". Then reduced it's armor by 1."
            mon1_armor-=1
            print(input_var)
        elif (input_var=="divine healing" or input_var=="dh") and p_race_charges>0 and p_race=="Aasimar":
            p_race_charges-=1
            p_health+=random.randint(8*p_lv, 12*p_lv)+16
            print(f"You healed using Divine Healing! You're up to {p_health}hp!")
            if p_health>p_max_health:
                p_health=p_max_health
        elif (input_var=="bottle" or input_var=="b") and p_classes.count("Alchemist")>0:
            input_var=input("Do you want to throw the bottle or use it yourself? Inputs are 'throw' and 'drink' and 'brew'.\n>>>")
            input_var=input_var.lower()
            if input_var=="throw" or input_var=="t":
                input_var="throw"
            elif input_var=="drink" or input_var=="d":
                input_var="drink"
            elif input_var=="brew" or input_var=="b":
                input_var="brew"
                if p_effect[:4]=="brew":
                    p_effect+="q"
                else:
                    p_effect="brew"
                input_var=len(p_effect)-3
                print(f"You've brewed your next potion {input_var} times! (And you healed a little.)")
                p_health+=(random.randint(2*p_classes.count("Alchemist"), 5*p_classes.count("Alchemist")))
                return
            else:
                print("You didn't answer a correct answer. Rebooting now...")
                p_turn_pt2()
                return
            q=0
            #For another neutral one, you could half the target's health, then deal damage to the other equal to the hp of the target.
            #If the dev adds a new effect for potions, change the lines with this:   #\-/
            while q>18 or q<1: #\-/
                q=random.randint(0, 19) #\-/
                if input_var=="drink":
                    q+=random.randint(-3, 4)
                    if p_effect[:4]=="brew":
                        input_var=len(p_effect)
                        while input_var>0:
                            input_var-=random.randint(1, 2)
                            if q<random.randint(13, 17): #\-/
                                q+=random.randint(0, 3)
                        input_var="drink"
                    elif p_effect=="PPot":
                        p_health+=(random.randint(5*p_classes.count("Alchemist"), 7*p_classes.count("Alchemist")))
                    if mon1_effect=="MonPot":
                        p_health-=(random.randint(5*p_classes.count("Alchemist"), 7*p_classes.count("Alchemist")))
                elif input_var=="throw":
                    q-=random.randint(-3, 4)
                    if p_effect[:4]=="brew":
                        input_var=len(p_effect)
                        while input_var>0:
                            input_var-=random.randint(1, 2)
                            if q>random.randint(1, 5): #\-/
                                q-=random.randint(0, 3)
                        input_var="throw"
                    elif p_effect=="PPot":
                        mon1_hp-=(random.randint(5*p_classes.count("Alchemist"), 7*p_classes.count("Alchemist")))
                    if mon1_effect=="MonPot":
                        mon1_hp+=(random.randint(5*p_classes.count("Alchemist"), 7*p_classes.count("Alchemist")))
            if p_effect[:4]=="brew" and input_var=="brew":
                q=0
            else:
                if p_effect[:4]=="brew":
                    p_effect="non"
                    print("Brew used.")
            if q==1: #Very Bad #\-/
                print("Very Bad: The potion was instant poison! The target is down to 1hp!")
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if mon1_hp>0:
                        mon1_hp=1
                elif input_var=="drink":
                    p_health=1
                    print("Because you're at 1hp, you get another turn.")
                    p_turn("non")
                    return
            elif q==2: #Bad #\-/
                if input_var=="throw":
                    input_var="drink" #yes, this is supposed to be like this
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                elif input_var=="drink":
                    input_var="throw" #yes, this is supposed to be like this
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                q=random.randint(11, 17) #\-/
                print("Bad: The potion gave the other target a good effect.")
            elif q==3: #Bad #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    mon1_hp-=random.uniform(10, 45)/100*mon1_max_hp
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    p_health-=random.uniform(10, 45)/100*p_max_health
                p_health=p_health//1
                mon1_hp=mon1_hp//1
                print("Bad: The potion dealt percentage damage.")
            elif q==4: #Bad #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 12*p_classes.count("Alchemist")))
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 12*p_classes.count("Alchemist")))
                elif input_var=="drink":
                    p_health-=(random.randint(7*p_classes.count("Alchemist"), 12*p_classes.count("Alchemist")))
                    mon1_hp+=(random.randint(7*p_classes.count("Alchemist"), 12*p_classes.count("Alchemist")))
                print("Bad: The potion was a life-drain potion!")
            elif q==5: #Bad #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if mon1_effect=="trip":
                        q=p_classes.count("Alchemist")
                        while q>0:
                            q-=1
                            mon1_spd-=random.randint(0, 3)
                    if mon1_effect!="trip":
                        mon1_armor-=2
                    mon1_effect="trip"
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if p_effect!="trip":
                        p_armor-=2
                        p_DR-=p_lv*4+4
                    p_effect="trip"
                print("Bad: It was a tripping potion!")
            elif q==6: #Bad #\-/
                if input_var=="throw":
                    mon1_armor-=random.randint(2+p_classes.count("Alchemist")//3, 2+p_classes.count("Alchemist")//2)
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                elif input_var=="drink":
                    p_armor-=random.randint(2+p_classes.count("Alchemist")//3, 2+p_classes.count("Alchemist")//2)
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                print("Bad: The potion reduced the armor of the target!")
            elif q==7: #Neutral #\-/
                print("Neutral: The potion was a randomize potion!")
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    input_var=mon1_hp/mon1_max_hp
                    q=mon1_effect
                    create_monster()
                    mon1_hp=input_var*mon1_max_hp
                    mon1_hp=int(mon1_hp)
                    mon1_effect=q
                    input_var="throw"
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    #
                    q=random.randint(-18*p_classes.count("Alchemist"), 18*p_classes.count("Alchemist"))
                    p_max_health+=q
                    p_health+=q
                    input_var="Max Hp "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    #
                    q=random.randint(-5*p_classes.count("Alchemist"), 5*p_classes.count("Alchemist"))
                    p_speed+=q
                    p_max_speed+=q
                    input_var+=", Max Spd "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    #
                    q=random.randint(-3*p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                    p_AB_temp+=q
                    p_AB+=q
                    input_var+=", Max AB "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    #
                    q=random.randint(-2*p_classes.count("Alchemist"), 2*p_classes.count("Alchemist"))
                    input_var+=", Max Armor "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    p_max_armor+=q
                    p_armor+=q
                    #
                    q=random.randint(-5*p_classes.count("Alchemist"), 5*p_classes.count("Alchemist"))
                    input_var+=", Max Mana "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    p_mana+=q
                    p_max_mana+=q
                    #
                    q=random.randint(-3*p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                    input_var+=", Loot "
                    if q<0:
                        input_var+="- "
                    else:
                        input_var+="+ "
                    input_var+=str(abs(q))
                    p_loot+=q
                    #
                    if p_max_race_charges!=0:
                        q=random.randint(-1, 1)
                        input_var+=", Max Race Charges "
                        input_var+="+ "
                        input_var+=str(q)
                        p_race_charges+=q
                        p_max_race_charges+=q
                    #
                    q=random.randint(-7*p_classes.count("Alchemist"), 7*p_classes.count("Alchemist"))
                    input_var+=", DR "
                    input_var+="+ "
                    input_var+=str(abs(q))
                    p_DR+=q
                    #
                    if p_classes.count("Shaman")>0 or p_classes.count("Monk") or p_race=="Human Devotee":
                        q=random.randint(-4*p_classes.count("Alchemist"), 4*p_classes.count("Alchemist"))
                        input_var+=", Energy "
                        if q<0:
                            input_var+="- "
                        else:
                            input_var+="+ "
                        input_var+=str(abs(q))
                        p_energy+=q
                    input_var+="."
                    print(input_var)
                    input_var="drink"
                q=6 #\-/
            elif q==8: #Neutral #\-/
                print("Neutral: If the target has an odd amount of the stat, they lose some of that stat, otherwise, they gain some of that stat.")
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if random.randint(1, 3)>=1: #hp
                        input_var=random.randint(10*p_classes.count("Alchemist"), 15*p_classes.count("Alchemist"))
                        if mon1_max_hp%2==1:
                            mon1_max_hp-=input_var
                            mon1_hp-=input_var
                            print(f"Neutral: The {mon1_race} lost max hp.")
                        else:
                            mon1_max_hp+=input_var
                            mon1_hp+=input_var
                            print(f"Neutral: The {mon1_race} gained max hp.")
                    if random.randint(1, 2)==1: #spd
                        if mon1_spd%2==1:
                            mon1_spd-=random.randint(p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                            print(f"Neutral: The {mon1_race} lost speed.")
                        else:
                            mon1_spd+=random.randint(p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                            print(f"Neutral: The {mon1_race} gained speed.")
                    if random.randint(1, 3)>=1: #armor
                        if int(mon1_armor)%2==1:
                            mon1_armor-=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist"))
                            print(f"Neutral: The {mon1_race} lost armor.")
                        else:
                            mon1_armor+=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist"))
                            print(f"Neutral: The {mon1_race} gained armor.")
                    if random.randint(1, 3)>=1: #ab
                        if int(mon1_AB)%2==1:
                            mon1_AB-=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist")+p_classes.count("Alchemist")//4)
                            print(f"Neutral: The {mon1_race} lost AB.")
                        else:
                            mon1_AB+=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist")+p_classes.count("Alchemist")//4)
                            print(f"Neutral: The {mon1_race} gained AB.")
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if random.randint(1, 3)>=1: #hp
                        if p_health%2==1:
                            p_health-=random.randint(10*p_classes.count("Alchemist"), 15*p_classes.count("Alchemist"))
                            print(f"Neutral: You lost hp.")
                        else:
                            p_health+=random.randint(10*p_classes.count("Alchemist"), 15*p_classes.count("Alchemist"))
                            print(f"Neutral: You gained hp.")
                    if random.randint(1, 2)==1: #spd
                        if p_speed%2==1:
                            p_speed-=random.randint(p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                            print(f"Neutral: You lost speed.")
                        else:
                            p_speed+=random.randint(p_classes.count("Alchemist"), 3*p_classes.count("Alchemist"))
                            print(f"Neutral: You gained speed.")
                    if random.randint(1, 3)>=1: #armor
                        if p_armor%2==1:
                            p_armor-=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist"))
                            print(f"Neutral: You lost armor.")
                        else:
                            p_armor+=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist"))
                            print(f"Neutral: You gained armor.")
                    if random.randint(1, 3)>=1: #ab
                        if p_AB_temp%2==1:
                            p_AB_temp-=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist")+p_classes.count("Alchemist")//4)
                            print(f"Neutral: You lost AB.")
                        else:
                            p_AB_temp+=random.randint(1+p_classes.count("Alchemist")//3, p_classes.count("Alchemist")+p_classes.count("Alchemist")//4)
                            print(f"Neutral: You gained AB.")
            elif q==9: #Neutral #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    mon1_AB+=random.randint(2+p_classes.count("Alchemist")//4, 7+p_classes.count("Alchemist")//2)
                    mon1_hp-=random.randint(5*mon1_AB, 6*mon1_AB)
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    p_AB_temp+=random.randint(2+p_classes.count("Alchemist")//4, 7+p_classes.count("Alchemist")//2)
                    p_health-=random.randint(5*p_AB_temp, 6*p_AB_temp)
                print("Neutral: The potion gave lots of AB, but dealt damage scaling with the AB the target has.")
            elif q==10: #Neutral #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if mon1_effect=="trip":
                        mon1_armor+=2
                    input_var=mon1_AB
                    mon1_AB=mon1_armor
                    mon1_armor=input_var
                    if mon1_effect=="trip":
                        mon1_armor-=2
                    input_var="throw"
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    input_var=p_armor
                    p_armor=p_AB_temp
                    p_AB_temp=input_var
                    input_var="drink"
                print("Neutral: The potion switched the AB and armor of the target.")
            if q==11: #Neutral #\-/ #Yes, this should be an 'if' not an elif because of q==2
                print("Neutral: Whoever had the most speed had their speed reduced. Then whoever had the most speed after that got some extra turns.")
                if mon1_spd>=p_speed:
                    mon1_spd-=random.randint(p_classes.count("Alchemist")//3, 2+p_classes.count("Alchemist"))
                else:
                    p_speed-=random.randint(p_classes.count("Alchemist")//3, 2+p_classes.count("Alchemist"))
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                if mon1_spd+random.randint(0, p_lv*2)>p_speed+random.randint(0, p_lv*2):
                    input_var=random.randint(1, 3)
                    if input_var==1:
                        print("The monster got 1 turn!")
                        mon1_turn()
                    elif input_var==2:
                        print("The monster got 2 turns!")
                        mon1_turn()
                        mon1_turn()
                    elif input_var==3:
                        print("The monster got 3 turns!")
                        mon1_turn()
                        mon1_turn()
                        mon1_turn()
                else:
                    input_var=random.randint(1, 3)
                    if input_var==1:
                        print("You got 1 turn!")
                        p_turn("non")
                    elif input_var==2:
                        print("You got 2 turns!")
                        p_turn("non")
                        p_turn("non")
                    elif input_var==3:
                        print("You got 3 turns!")
                        p_turn("non")
                        p_turn("non")
                        p_turn("non")
            elif q==12: #Neutral #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    mon1_spd-=(mon1_max_hp-mon1_hp)//random.randint(15, 20)
                    mon1_hp=mon1_max_hp
                    mon1_spd-=1
                elif input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    p_speed-=(p_max_health-p_health)//random.randint(15, 20)
                    p_health=p_max_health
                    p_speed-=1
                print("Neutral: The potion was a full-healing, speed reduction potion!")
            elif q==13: #Good #\-/
                print("Good: The potion was a time potion, giving them an extra turn!")
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    mon1_turn()
                elif input_var=="drink":
                    p_health=p_health+(random.randint(7, 10)*p_classes.count("Alchemist"))
                    p_turn("non")
            elif q==14: #Good #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    mon1_spd+=random.randint(1+p_classes.count("Alchemist"), p_classes.count("Alchemist")*3)
                elif input_var=="drink":
                    p_speed+=random.randint(1+p_classes.count("Alchemist"), p_classes.count("Alchemist")*3)
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                print("Good: The potion increased their speed!")
            elif q==15: #Good #\-/
                if input_var=="throw":
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if mon1_effect=="non":
                        mon1_effect="Rage_"
                        q=random.randint(2, 5)
                        while q>0:
                            q-=1
                            mon1_effect+="q"
                    else:
                        if mon1_effect[:5]!="Rage_":
                            mon1_effect="Rage_"
                        q=random.randint(1, 3)
                        while q>0:
                            q-=1
                            mon1_effect+="q"
                if input_var=="drink":
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                    if p_effect=="non":
                        p_effect="Dmg"
                        q=random.randint(2, 5)
                        while q>0:
                            q-=1
                            if random.randint(1, 4)==1:
                                p_effect+="g"
                            elif random.randint(1, 3)==1:
                                p_effect+="f"
                            else:
                                p_effect+="d"
                            if random.randint(1, 6)==1:
                                p_effect+="a"
                    elif p_effect[:3]=="Dmg":
                        q=random.randint(2, 5)
                        while q>0:
                            q-=1
                            if random.randint(1, 6)==1:
                                p_effect+="g"
                            elif random.randint(1, 6)==1:
                                p_effect+="f"
                            else:
                                p_effect+="s"
                            if random.randint(1, 5)==1:
                                p_effect+="a"
                    else:
                        p_effect="Dmg"
                        q=random.randint(4, 7)
                        while q>0:
                            q-=1
                            if random.randint(1, 4)==1:
                                p_effect+="g"
                            elif random.randint(1, 3)==1:
                                p_effect+="f"
                            else:
                                p_effect+="d"
                            if random.randint(1, 6)==1:
                                p_effect+="a"
                q=13
                print("Good: The potion was a Rage potion!")
            elif q==16: #Good #\-/
                if input_var=="throw":
                    mon1_effect="MonPot"
                    mon1_hp-=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                elif input_var=="drink":
                    p_effect="PPot"
                    p_health+=(random.randint(7*p_classes.count("Alchemist"), 10*p_classes.count("Alchemist")))
                print("Good: The potion gave a buff that increases the damage/healing that future potions cause.")
            elif q==17: #Good #\-/
                if input_var=="throw":
                    mon1_hp+=(random.randint(7, 10)*p_classes.count("Alchemist"))
                elif input_var=="drink":
                    p_health+=(random.randint(21*p_classes.count("Alchemist"), 30*p_classes.count("Alchemist")))
                print("Good: The potion was a healing potion!")
            elif q==18: #Very Good #\-/
                if input_var=="throw":
                    if not " " in mon1_race or random.randint(1, 4)==1:
                        print(f"Very Good: The potion transformed the {mon1_race} into a Minotaur, and it full healed it.")
                        mon1_race="Minotaur"
                    else:
                        print(f"Very Good: The potion full healed it.")
                    mon1_hp=mon1_max_hp
                elif input_var=="drink":
                    print("Very Good: The potion gave you points and completely rested you!")
                    if random.randint(1, 7)>5 and p_classes.count("Alchemist")>p_lv*4/7:
                        print("VERY GOOD!: And you got some extra points for being lucky!")
                        points("Alc Pot")
                    if p_classes.count("Alchemist")>p_lv/2:
                        points("Alc Pot")
                    else:
                        print("Unfortunatally, you're unable to get xtr points because Alchemist is not your main stat. Make your Alc level your highest level, then you get xtr points.")
                    rest()
        elif input_var=="attack" or input_var=="a":
            if p_effect=="chrg":
                p_AB_temp+=5
            if p_effect=="-5 AB":
                p_AB_temp-=5
            if random.randint(1, 18)==1:
                mon1_hp-=(random.randint(12*p_lv, 16*p_lv))
                if p_effect[:5]=="Rage_":
                    mon1_hp-=random.randint(5*p_lv, 9*p_lv)
                if p_effect=="chrg":
                    mon1_hp-=p_lv*random.randint(3, 8)
                if p_effect[:5]!="Rage_":
                    if p_race=="Human Devotee":
                        p_energy+=1
                    p_energy+=p_classes.count("Monk")+p_classes.count("Shaman")
                if p_effect=="Ss3":
                    p_mana+=random.randint(3, p_classes.count("Spellsword")*3)
                    print(f"You gained mana! You're up to {p_mana} mana!")
                    if p_mana>p_max_mana:
                        p_mana=p_max_mana
                print("You CRIT! Not only did you automatically hit, but you also dealt much more damage.")
                if p_effect=="Cl6" or p_effect=="Ss5":
                    mon1_hp-=(random.randint(7*p_lv, 12*p_lv))
                    print("You dealt extra damage with your buff!")
                elif p_effect[:3]=="Dmg":
                        q=len(p_effect)
                        q-=1
                        input_var=0
                        while q>3:
                            if p_effect[q]=="a":
                                input_var+=1
                            elif p_effect[q]=="s":
                                input_var+=2
                            elif p_effect[q]=="d":
                                input_var+=3
                            elif p_effect[q]=="f":
                                input_var+=4
                            elif p_effect[q]=="g":
                                input_var+=5
                            elif p_effect[q]=="h":
                                input_var+=6
                            q-=1
                        while input_var>0:
                            input_var-=1
                            mon1_hp-=random.randint(0, 3*p_lv)
            else:
                if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                    mon1_hp-=(random.randint(10*p_lv, 13*p_lv))
                    if p_effect[:5]=="Rage_":
                        mon1_hp-=random.randint(5*p_lv, 9*p_lv)
                    if p_effect[:5]!="Rage_":
                        if p_race=="Human Devotee":
                            p_energy+=1
                        p_energy+=p_classes.count("Monk")+p_classes.count("Shaman")
                    if p_effect=="Ss3":
                        p_mana+=random.randint(p_classes.count("Spellsword"), 4*p_classes.count("Spellsword"))
                        print(f"You gained mana! You're up to {p_mana} mana!")
                        if p_mana>p_max_mana:
                            p_mana=p_max_mana
                    print("You hit!")
                    if p_effect=="Cl6" or p_effect=="Ss5":
                        mon1_hp-=(random.randint(4*p_lv, 9*p_lv))
                        print("You dealt extra damage with your buff!")
                    elif p_effect=="Py3":
                        if "f" in mon1_perma_effect:
                            input_var=random.randint(1, 2)
                            while input_var>0:
                                input_var-=1
                                mon1_perma_effect+="f"
                        else:
                            mon1_perma_effect="Fireff"
                        input_var=len(mon1_perma_effect)-4
                        print(f"It caught on fire from your attacks! It's up to {input_var} fire counters!")
                    elif p_effect[:3]=="Dmg":
                        q=len(p_effect)
                        q-=1
                        input_var=0
                        while q>3:
                            if p_effect[q]=="a":
                                input_var+=1
                            elif p_effect[q]=="s":
                                input_var+=2
                            elif p_effect[q]=="d":
                                input_var+=3
                            elif p_effect[q]=="f":
                                input_var+=4
                            elif p_effect[q]=="g":
                                input_var+=5
                            elif p_effect[q]=="h":
                                input_var+=6
                            q-=1
                        while input_var>0:
                            input_var-=1
                            mon1_hp-=random.randint(0, 2*p_lv)
                else:
                    print("You missed.")
            if p_effect=="chrg":
                print("Charge used.")
                p_AB_temp-=5
                p_effect="non"
            if p_effect=="-5 AB":
                p_AB_temp+=5
        elif input_var=="trip" or input_var=="t":
            if p_effect=="chrg":
                p_AB_temp+=5
            if p_effect=="-5 AB":
                p_AB_temp-=5
            if mon1_armor<=random.randint(-3, 0) + p_AB_temp:
                mon1_hp-=random.randint(2*p_lv, 5*p_lv)
                if p_effect[:5]!="Rage_":
                    if p_race=="Human Devotee":
                        p_energy+=1
                    p_energy+=p_classes.count("Monk")+p_classes.count("Shaman")
                if p_effect=="Ss3":
                    p_mana+=random.randint(p_classes.count("Spellsword"), 2*p_classes.count("Spellsword"))
                    print(f"You gained mana! You're up to {p_mana} mana!")
                    if p_mana>p_max_mana:
                        p_mana=p_max_mana
                trip_chance=random.randint(1, 5)
                if p_effect=="chrg":
                    trip_chance=5
                if trip_chance!=1:
                    if mon1_effect!="trip":
                        mon1_armor-=2
                    mon1_effect='trip'
                    print("You hit, and tripped them successfully!")
                else:
                    print("You hit, but didn't trip successfully.")
                if p_effect[:3]=="Dmg":
                    q=len(p_effect)
                    q-=1
                    input_var=0
                    while q>3:
                        if p_effect[q]=="a":
                            input_var+=1
                        elif p_effect[q]=="s":
                            input_var+=2
                        elif p_effect[q]=="d":
                            input_var+=3
                        elif p_effect[q]=="f":
                            input_var+=4
                        elif p_effect[q]=="g":
                            input_var+=5
                        elif p_effect[q]=="h":
                            input_var+=6
                        q-=1
                    while input_var>0:
                        input_var-=1
                        mon1_hp-=random.randint(0, 1*p_lv)
                elif p_effect=="Py3":
                    if "f" in mon1_perma_effect:
                        input_var=random.randint(0, 1)
                        while input_var>0:
                            input_var-=1
                            mon1_perma_effect+="f"
                    else:
                        mon1_perma_effect="Firef"
            else:
                print("You missed.")
            if p_effect=="chrg":
                print("Charge used.")
                p_AB_temp-=5
                p_effect="non"
            if p_effect=="-5 AB":
                p_AB_temp+=5
        elif input_var=="charge" or input_var=="c":
            if p_effect=="non" or p_effect=="-5 AB":
                p_effect="chrg"
                print("You charged.")
            elif p_effect=="HD4":
                print("You can't remove the HD4 debuff with charging, only with energy-empowered buffs or other divine buffs. Your enemy can also remove it.")
                p_turn_pt2()
                return
            elif p_effect=="chrg":
                print("You already have charge, so you get +1 AB until the round is over.")
                p_AB_temp+=1
                if random.randint(1, 4)==1:
                    print("Unfortunatally, because you double charged, your next turn gets skipped.")
                    mon1_turn()
                    p_turn("NoXtrTurn")
            else:
                print(f"You debuffed instead of charging. Your previous buff was {p_effect}.")
                p_effect='non'
        elif input_var=="energy" or input_var=="en":
            if 'Shaman' in p_classes or 'Monk' in p_classes or p_race=="Human Devotee":
                q='Your energy actions are these:'
                if p_race=="Human Devotee":
                    q+="\n-HD1: Costing 4 energy: End your turn, and when you take damage this turn, deal that much damage back with a multiplier with 1.75, automatical hit.\n-HD2: Costing 0 energy: End your turn to gain a lot of energy based on the amount of energy-related classes you have.\n-HD3: Costing 3 energy: Gain mana equal to your max mana * 0.3.\n-HD4: Costing 4 energy: Become empowered gaining 5 AB, -1 AB end of your turn.\n-HD5: Costing 2 energy: Attack right now, but it heals yourself the amount that you dealt rather than dealing damage. (FYI, you have to hit them.)"
                if 'Shaman' in p_classes:
                    q+="\n-Sh1: Costing "
                    q+=str(3 + int(p_classes.count("Shaman")) + int(p_classes.count("Monk")))
                    q+=" energy: Heal yourself, the amount scaling per shaman level.\n-Sh2: Costing "
                    q+=str(p_lv+int(p_classes.count("Shaman")+3))
                    q+=" energy: You drive yourself into a rage. It doesn't last forever, but while it's active, you deal extra damage and don't get energy on hit.\n-Sh3: Costing "
                    q+=str(3 + p_lv * 2)
                    q+=" energy: Deals normal damage times 2 or 3, randomly."
                if 'Monk' in p_classes:
                    q+="\n-Mo1: Costing 2 energy: Attack right now with +5AB.\n-Mo2: Costing "
                    q+=str(3 + p_lv - int(p_classes.count("Shaman")) - int(p_classes.count("Monk")))
                    q+=" energy: Deal damage, scaling with AB.\n-Mo3: Costing "
                    q+=str(3 + p_lv + p_lv - int(p_classes.count("Shaman")) - int(p_classes.count("Monk")))
                    q+=" energy: Permanentally gives your target -2 to -4 speed, randomly. (FYI, you have to hit them.)\n-Mo4: Costing "
                    q+=str(p_lv * 2 + 1)
                    q+=" energy: Deals damage, scaling with speed."
                q+=(f"\nTo select an ability, type mo3 for Monk's 3rd ability, etc.\nYou have {p_energy} energy.\n>>>")
                q=input(q)
                q=q.lower()
                if q=="hd1" and p_energy>=4 and p_race=="Human Devotee":
                    p_energy-=4
                    p_effect="HD1"
                    print("You used HD1!")
                elif q=="hd2" and p_race=="Human Devotee":
                    p_energy+=1+p_classes.count("Monk")+p_classes.count("Shaman")
                    if p_race=="Human Devotee":
                        p_energy+=2
                    print(f"Your energy is now at {p_energy}!")
                elif q=="hd3" and p_race=="Human Devotee" and p_energy>=3:
                    p_energy-=3
                    p_mana+=p_max_mana*0.3
                    p_mana=int(p_mana)
                    print(f"You gained mana! You're up to {p_mana} mana!")
                elif q=="hd4" and p_energy>=4 and p_race=="Human Devotee":
                    p_energy-=4
                    p_AB_temp+=5
                    p_effect="HD4"
                    print(f"You empowered yourself with energy. You now have {p_AB_temp}AB.")
                elif q=="hd5" and p_energy>=2 and p_race=="Human Devotee":
                    p_energy-=2
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if random.randint(1, 18)==1:
                        p_health+=(random.randint(20*p_lv, 23*p_lv))
                        if p_effect=="chrg":
                            p_health +=p_lv*random.randint(7, 11)
                        print("You CRIT! Not only did you automatically hit, but you also healed much more.")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            p_health+=(random.randint(16, 21))
                            print("You healed extra with your buff!")
                    else:
                        if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                            p_health+=(random.randint(14*p_lv, 19*p_lv))
                            print("You hit!")
                            if p_effect=="Cl6" or p_effect=="Ss5":
                                p_health+=(random.randint(10*p_lv, 16*p_lv))
                                print("You healed extra with your buff!")
                        else:
                            print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                elif q=="mo1" and p_energy>=2 and p_classes.count("Monk")>0:
                    p_energy-=2
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if mon1_armor<=random.randint(3, 10) + p_AB_temp:
                        mon1_hp-=random.randint(9*p_lv, 12*p_lv)
                        print("You hit!")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=(random.randint(7*p_lv, 12*p_lv))
                            print("You dealt extra damage with your buff!")
                    else:
                        print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                elif q=="mo2" and p_energy>=3 + p_lv - int(p_classes.count("Shaman")) - int(p_classes.count("Monk")) and p_classes.count("Monk")>0:
                    p_energy-=3 + p_lv - int(p_classes.count("Shaman")) - int(p_classes.count("Monk"))
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                        mon1_hp-=p_AB_temp*random.randint(28, 39)//4
                        print("You hit!")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=(random.randint(7*p_lv, 12*p_lv))
                            print("You dealt extra damage with your buff!")
                    else:
                        print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                elif q=="mo3" and p_energy>=3+p_lv+p_lv-p_classes.count("Monk")-p_classes.count("Shaman") and p_classes.count("Monk")>0:
                    p_energy-=3+p_lv+p_lv-p_classes.count("Monk")-p_classes.count("Shaman")
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                        mon1_hp-=random.randint(9*p_lv, 14*p_lv)
                        mon1_spd-=random.randint(2, 4)
                        print(f"You hit! Their speed is now {mon1_spd}!")
                    else:
                        print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                elif q=="mo4" and p_energy>=2*p_lv+1 and p_classes.count("Monk")>0:
                    p_energy-=2*p_lv+1
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                        mon1_hp-=((p_speed*random.choice([1.6, 1.6, 1.8, 1.9, 1.9, 1.9, 2, 2, 2, 2, 2, 2.1, 2.1, 2.1, 2.1, 2.2, 2.2, 2.2, 2.3, 2.4])*p_lv+p_lv))
                        mon1_hp=mon1_hp//1
                        print("You hit!")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=(random.randint(7*p_lv, 12*p_lv))
                            print("You dealt extra damage with your buff!")
                    else:
                        print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                elif q=="sh1" and p_energy>=3 + int(p_classes.count("Shaman")) + int(p_classes.count("Monk")) and p_classes.count("Shaman")>0:
                    p_energy-=3 + int(p_classes.count("Shaman")) + int(p_classes.count("Monk"))
                    p_health+=int(p_classes.count("Shaman")*10+random.randint(p_lv*8, p_lv*14))
                    print("You been healed!")
                    if p_health>p_max_health:
                        p_health=p_max_health
                elif q=="sh2" and p_energy>=p_lv+int(p_classes.count("Shaman")+3) and p_classes.count("Shaman")>0:
                    p_energy-=p_lv+int(p_classes.count("Shaman")+3)
                    p_effect="Rage_"
                    input_var=random.randint(3, 5)
                    while input_var>0:
                        input_var-=1
                        p_effect+="q"
                    print("You've becomed enraged!")
                    p_turn("non")
                    return
                elif q=="sh3" and p_energy>=3+p_lv*2 and p_classes.count("Shaman")>0:
                    p_energy-=3+p_lv*2
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                        mon1_hp-=random.randint(24*p_lv, 30*p_lv)
                        print("You hit!")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=random.randint(7*p_lv, 12*p_lv)
                            print("You dealt extra damage with your buff!")
                    else:
                        print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                else:
                    print("You entered a wrong answer. Rebooting now...")
                    p_turn_pt2()
                    return
            else:
                print("You can not access energy-empowered abililties, because you don't have the Monk class. Rebooting now...")
                p_turn_pt2()
                return
        elif (input_var=="spellbook" or input_var=="sb" or input_var=="s") and p_classes.count("Mage")+p_classes.count("Spellsword")+p_classes.count("Shaman")+p_classes.count("Cleric")+p_classes.count("Pyromancer")>0:
            q="Your spells are these:"
            if 'Mage' in p_classes:
                q+="\nMagic Missile (Ma1): Costing "
                q+=str(p_classes.count("Mage"))
                q+=" mana: Deal a basic amount of damage, scaling with your mage level.\nGust (Ma2): Costing "
                q+=str(p_lv*2)
                q+=" mana: Automatically trips them, and if it hits, deals a small amount of damage and reduces their speed.\nShield (Ma3): Costing "
                q+=str(p_classes.count("Mage")+(p_lv-p_classes.count("Mage"))//3)
                q+=" mana: Gives you some armor, and if you cast it again, it gains more and more thorns, until you get debuffed.\nLightning Bolt (Ma4): Costing "
                q+=str(p_classes.count("Mage")*3)
                q+=" mana: Next turn, you can either attack, or charge. It takes mana to charge, and it increases in damage if you do.\nNecrotic Blast (Ma5): Costing "
                q+=str(p_classes.count("Mage")*7)
                q+=" mana: Use an unholy amount of mana to deal an unholy amount of damage.\nAugury (Ma6): Costing "
                q+=str(p_classes.count("Mage")*2+p_lv//2)
                q+=" mana: Get a random effect from a small heal, to basic damage, or useful utility, like reducing a target's stats.\nConjure Clone (Ma7): Costing "
                q+=str(p_classes.count("Mage")*2+p_lv)
                q+=" mana: Half the attacks that attack you instead attack your clone. It has one hp, and it can also attack. This counts as a buff.\nChaos Bolt (Ma8): Costing "
                q+=str(p_classes.count("Mage")*2+2)
                q+=" mana: A lot like Magic Missile, it deals only damage, however, with a far wider range of damage.\nAcid Splash (Ma9): Costing "
                q+=str(p_lv*3+1)
                q+=" mana: This attack is the only DOT you'll ever find. (DOT standing for Damage Over Time.)"
            if 'Shaman' in p_classes:
                q+="\nCure (Sh1): Costing "
                q+=str(p_classes.count("Shaman")*2+1)
                q+=" mana: Heal yourself. There's a similar ability using energy.\nCurse (Sh2): Costing "
                q+=str(p_lv)
                q+=" mana: Curse the target by removing some of their buffs, like armor, AB, and speed.\nLife Drain (Sh3): Costing "
                q+=str(p_classes.count("Shaman")*4)
                q+=" mana: Gain a bunch of energy. This doesn't actually drain the target in any way.\nEnergy Blast (Sh4): Costing "
                q+=str(p_classes.count("Shaman")+3+p_lv//3)
                q+=" mana: Deal spell damage, scaling with your current energy."
            if 'Cleric' in p_classes:
                q+="\nCure Wounds (Cl1): Costing "
                q+=str(p_classes.count("Cleric"))
                q+=" mana: Heal a good amount, scaling with your cleric level.\nEmpower Weapon (Cl2): Costing "
                q+=str(p_classes.count("Cleric")//2+p_lv-1)
                q+=" mana: Gain 1 AB, and a chance to gain 2 instead, maybe even 3.\nDivine Beam (Cl3): Costing "
                q+=str(p_classes.count("Cleric")*3-1)
                q+=" mana: Deal some amount of damage, more than your normal attack would.\nRegeneration (Cl4): Costing "
                q+=str(p_classes.count("Cleric")*3+1)
                q+=" mana: Heals a small amount, over time.\nPrayer (Cl5): Costing "
                q+=str(p_classes.count("Cleric")*4-1)
                q+=" mana: You may give yourself a buff that has a chance to give them the debuff every turn. This debuff gives them minus speed every turn.\n   Also inflicts debuff on cast.\nAngel Wings (Cl6): Costing "
                q+=str(p_lv*4-1-p_classes.count("Cleric")*2)
                q+=" mana: Channels divine power through you. By becoming a celestial being, you have\n -A chance to trip your target at the start of your turn\n -Become immune to trip\n -Your base attack increases damage\n      However, this takes mana every turn to stay in this form."
            if 'Spellsword' in p_classes:
                q+="\nBlur (Ss1): Costing "
                q+=str(p_lv*3-p_classes.count("Spellsword"))
                q+=" mana: Gain a buff that gives you armor as soon as you cast it, and at the start of your turns gives you speed.\nSpectral Attack (Ss2): Costing "
                q+=str(p_lv+p_classes.count("Spellsword")*2+2)
                q+=" mana: Attack as normal, but armor is heavily negated. Also has a high chance to trip.\nImbue: Mana (Ss3): Costing "
                q+=str(p_lv*4-p_classes.count("Spellsword")-1)
                q+=" mana: Gain a buff that gives you mana every time you attack.\nCursed Cut (Ss4): Costing "
                q+=str(p_classes.count("Spellsword")+p_lv)
                q+=" mana: Attack, and if you hit, it debuffs them permanentally, reducing their stats at the start of their turn. This can stack.\nBlade Bond (Ss5): Costing "
                q+=str(p_classes.count("Spellsword")*3+p_lv*3)
                q+=" mana: Gain a lot of DR, and you lose health every turn. You also deal more damage. This counts as a buff."
            if 'Pyromancer' in p_classes:
                q+="\nFire Blast (Py1): Costing "
                q+=str(p_classes.count("Pyromancer"))
                q+=" mana: Increase monster's fire counter by a small amount.\nFlame Strike (Py2): Costing "
                q+=str(p_classes.count("Pyromancer")+p_lv)
                q+=" mana: Deal damage to a monster scaling with their fire counter.\nFlame Coating (Py3): Costing "
                q+=str(p_classes.count("Pyromancer")*2+p_lv-1)
                q+=" mana: Gives you a buff that allows you to increase it's fire counter every time you attack, and less counters if you trip.\nFireball (Py4): Costing "
                q+=str(p_classes.count("Pyromancer")*4+p_lv*2-1)
                q+=" mana: It gives the monster some fire counters, then deals damage scaling with their fire counters.\nFire Shield (Py5): Costing "
                q+=str(p_classes.count("Pyromancer")+p_lv//4)
                q+=" mana: Increases your DR, and you can stack it. If you do, it gives fire counters when you're hit per time you cast it.\nResurgance (Py6): Costing "
                q+=str(p_classes.count("Pyromancer")*2+1)
                q+=" mana: Remove your opponent's fire counters to heal yourself far past your max hp.\nMelt Armor (Py7): Costing "
                q+=str(p_classes.count("Pyromancer"))
                q+=" mana: Reduce it's armor. Also requires 3-4 fire."
            q+="\nTo select an ability, type ma4 for Mage's 4th ability, cl2 for Cleric's 2nd ability, etc.\n>>>"
            q=input(q)
            q=q.lower()
            if q=="ma1" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage"):
                    p_mana-=p_classes.count("Mage")
                    mon1_hp-=(random.randint(10, 15)*p_classes.count("Mage")+p_classes.count("Mage")*2)
                    print("You hit!")
                else:
                    print("You do not have enough mana for Ma1.")
                    p_turn_pt2()
                    return
            elif q=="ma2" and p_classes.count("Mage")>0:
                if p_mana>=p_lv*2:
                    if mon1_effect!="trip:":
                        mon1_armor-=2
                    mon1_effect="trip"
                    p_mana-=p_lv*2
                    mon1_hp-=random.randint(1, 5)*p_classes.count("Mage")
                    mon1_spd-=random.randint(0, 2+p_classes.count("Mage")//3)
                    print("You cast gust!")
                else:
                    print("You do not have enough mana for Ma2.")
                    p_turn_pt2()
                    return
            elif q=="ma3" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")+(p_lv-p_classes.count("Mage"))//3:
                    p_mana-=p_classes.count("Mage")+(p_lv-p_classes.count("Mage"))//3
                    q="You cast Shield!"
                    if p_effect[:3]!="Ma3":
                        p_effect="Ma3"
                    else:
                        p_effect+="q"
                        q+=" Your thorns is up to "
                        q+=str(len(p_effect) -3)
                        q+="."
                    print(f"{q}")
                else:
                    print("You do not have enough mana for Ma3.")
                    p_turn_pt2()
                    return
            elif q=="ma4" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")*3:
                    p_mana-=p_classes.count("Mage")*3
                    p_effect="Ma4"
                    print("You're charging a Lightning Bolt!")
                else:
                    print("You do not have enough mana for Ma4.")
                    p_turn_pt2()
                    return()
            elif q=="ma5" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")*7:
                    p_mana-=p_classes.count("Mage")*7
                    mon1_hp-=(random.randint(38, 54)*p_classes.count("Mage"))
                    print("You dealt an unholy amount of damage!")
                else:
                    print("You do not have enough mana for Ma5.")
                    p_turn_pt2()
                    return
            elif q=="ma6" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")*2+p_lv//2:
                    p_mana-=p_classes.count("Mage")*2+p_lv//2
                    q=random.randint(1, 7)
                    if q==1:
                        mon1_hp-=(random.randint(24, 30)*p_classes.count("Mage")+p_classes.count("Mage")*2)
                        print("You dealt damage!")
                    elif q==2:
                        if p_health//2>=p_max_health:
                            p_health=p_max_health*random.choice([3.1, 3.2, 3.3, 3.5, 3.7, 3.7, 3.7, 3.8, 3.9, 4.1])
                        else:
                            p_health=p_max_health*2
                        if p_effect!="trip":
                            p_armor-=2
                            p_DR-=p_lv*4+4
                        p_effect="trip"
                        p_health=int(p_health)
                        print(f"You healed yourself far past your max hp. This comes at the cost of becoming tripped. You're up to {p_health} hp. And your max health is {p_max_health}.")
                    elif q==3:
                        mon1_spd-=random.randint(1, 3)*p_classes.count("Mage")
                        mon1_armor-=random.randint(2, 4+p_lv//2)
                        mon1_AB-=p_classes.count("Mage")
                        print("You cursed the monster!")
                    elif q==4:
                        p_mana+=p_classes.count("Mage")*3+p_lv+p_lv//2
                        print(f"You gained mana! You're up to {p_mana} mana!")
                    elif q==5:
                        p_effect="HD1"
                        print("You activated a special ability from another class!")
                    elif q==6:
                        p_effect="HD4"
                        p_AB_temp+=random.randint(3+p_lv, 5+p_lv*2)
                        mon1_spd+=random.randint(0, 4+p_classes.count("Mage"))
                        print(f"You got a HUGE bonus to AB, but it will go away soon, and it increased the {mon1_race}'s speed.")
                else:
                    print("You do not have enough mana for Ma6.")
                    p_turn_pt2()
                    return
            elif q=="ma7" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")*2+p_lv:
                    p_mana-=p_classes.count("Mage")*2+p_lv
                    if p_effect[:3]!="Ma7":
                        p_effect="Ma7q"
                    else:
                        p_effect+="qq"
                    print("You created a clone!")
                else:
                    print("You do not have enough mana for Ma7.")
                    p_turn_pt2()
                    return
            elif q=="ma8" and p_classes.count("Mage")>0:
                if p_mana>=p_classes.count("Mage")*2+1:
                    p_mana-=p_classes.count("Mage")*2+1
                    if random.randint(1, 3)==1:
                        mon1_hp-=(random.randint(22*p_lv, 41*p_lv)+p_lv*4)
                        if random.randint(1, 100)==1:
                            mon1_hp=-999998999999
                            print("OMEGA LUCKY!!!! YOU ROLLED A 1 IN 100 AND ONE-SHOT THE MONSTER!!!!")
                        else:
                            print("LUCKY, dealing massive damage!!")
                    else:
                        if random.randint(1, 3)!=1:
                            mon1_hp-=(random.randint(14*p_lv, 18*p_lv)+p_lv*2)
                            print("Medium Luck.")
                        else:
                            mon1_hp-=(random.randint(6*p_lv, 8*p_lv)+p_lv)
                            print("Unlucky, but still dealt some damage.")
                else:
                    print("You do not have enough mana for Ma8.")
                    p_turn_pt2()
                    return
            elif q=="ma9" and p_classes.count("Mage")>0:
                if p_mana>=p_lv*3+1:
                    p_mana-=p_lv*3+1
                    mon1_perma_effect="Ma9"
                    print("You splashed them with acid, causing them to take DOT!")
                else:
                    print("You do not have enough mana for Ma9.")
                    p_turn_pt2()
                    return
            elif q=="sh1" and p_classes.count("Shaman")>0:
                if p_mana>=p_classes.count("Shaman")*2+1:
                    p_mana-=p_classes.count("Shaman")*2+1
                    p_health+=int(p_classes.count("Shaman")*10+random.randint(p_lv*8, p_lv*14))
                    print("You healed!")
                else:
                    print("You do not have enough mana for Sh1.")
                    p_turn_pt2()
                    return
            elif q=="sh2" and p_classes.count("Shaman")>0:
                if p_mana>=p_lv:
                    p_mana-=p_lv
                    mon1_spd-=random.randint(0, 2)
                    mon1_armor-=random.randint(0, 3)
                    mon1_AB-=1
                    print(f"You debuffed the {mon1_race}!")
                else:
                    print("You do not have enough mana for Sh2.")
                    p_turn_pt2()
                    return
            elif q=="sh3" and p_classes.count("Shaman")>0:
                if p_mana>=p_classes.count("Shaman")*4:
                    p_mana-=p_classes.count("Shaman")*4
                    q=p_classes.count("Shaman")
                    while q>0:
                        q-=1
                        p_energy+=random.randint(3, 5)
                    print("You gained a lot of energy!")
                else:
                    print("You do not have enough mana for Sh3.")
                    p_turn_pt2()
                    return
            elif q=="sh4" and p_classes.count("Shaman")>0:
                if p_mana>=p_classes.count("Shaman")+3+p_lv//3:
                    p_mana-=p_classes.count("Shaman")+3+p_lv//3
                    mon1_hp-=(random.randint((p_energy*3)//2, p_energy*3)*((p_lv//2)+1))
                    print("You used energy blast!")
                else:
                    print("You do not have enough mana for Sh4.")
                    p_turn_pt2()
                    return
            elif q=="cl1" and p_classes.count("Cleric")>0:
                if p_mana>=p_classes.count("Cleric"):
                    p_mana-=p_classes.count("Cleric")
                    p_health+=random.randint(21, 27)*p_classes.count("Cleric")
                    if p_health>p_max_health:
                        p_health=p_max_health
                    print(f"You healed! You have {p_health} health.")
                else:
                    print("You do not have enough mana for Cl1.")
                    p_turn_pt2()
                    return
            elif q=="cl2" and p_classes.count("Cleric")>0:
                if p_mana>=p_classes.count("Cleric")//2+p_lv-1:
                    p_mana-=p_classes.count("Cleric")//2+p_lv-1
                    p_AB_temp+=1
                    print("You gained an AB!")
                    if random.randint(0, 2)!=0:
                        p_AB_temp+=1
                        print("You gained another AB!!")
                    if random.randint(0, 10)>6:
                        p_AB_temp+=1
                        print("You gained another AB!!!!")
                        if random.randint(1, 5)>3:
                            p_AB_temp+=2
                            print("You gained ANOTHER 2 AB!!!!!")
                else:
                    print("You do not have enough mana for Cl2.")
                    p_turn_pt2()
                    return
            elif q=="cl3" and p_classes.count("Cleric")>0:
                if p_mana>=p_classes.count("Cleric")*3-1:
                    p_mana-=p_classes.count("Cleric")*3-1
                    mon1_hp-=random.randint(19*p_lv, 23*p_lv)
                    print("You dealt massive damage!")
                else:
                    print("You do not have enough mana for Cl3.")
                    p_turn_pt2()
                    return
            elif q=="cl4" and p_classes.count("Cleric")>0:
                if p_mana>=p_classes.count("Cleric")*3+1:
                    p_mana-=p_classes.count("Cleric")*3+1
                    p_effect="Cl4"
                    print("You cast regeneration!")
                else:
                    print("You do not have enough mana for Cl4.")
                    p_turn_pt2()
                    return
            elif q=="cl5" and p_classes.count("Cleric")>0:
                if p_mana>=p_classes.count("Cleric")*4-1:
                    input_var=input("You debuffed the monster! Do you want to give the prayer buff to you? The inputs are 'yes' and 'no'.\n>>>")
                    input_var=input_var.lower()
                    if input_var=="yes" or input_var=="y":
                        p_effect="Cl5"
                    elif input_var=="no" or input_var=="n":
                        pass
                    else:
                        print("You didn't answer a correct answer. Rebooting now...")
                        p_turn_pt2()
                        return
                    p_mana-=p_classes.count("Cleric")*4-1
                    mon1_effect="Cl5"
                else:
                    print("You do not have enough mana for Cl5.")
                    p_turn_pt2()
                    return
            elif q=="cl6" and p_classes.count("Cleric")>0:
                if p_mana>=p_lv*5-1-p_classes.count("Cleric")*2:
                    p_mana-=p_lv*5-1-p_classes.count("Cleric")*2
                    p_effect="Cl6"
                    print("You became a celestial!")
                else:
                    print("You do not have enough mana for Cl6.")
                    p_turn_pt2()
                    return
            elif q=="ss1" and p_classes.count("Spellsword")>0:
                if p_mana>=p_lv*3-p_classes.count("Spellsword"):
                    p_mana-=p_lv*3-p_classes.count("Spellsword")
                    p_armor+=random.randint(0, 2+p_lv//3+p_lv//4)
                    p_effect="Ss1"
                    print("You've cast Blur!")
                else:
                    print("You do not have enough mana for Ss1.")
                    p_turn_pt2()
                    return
            elif q=="ss2" and p_classes.count("Spellsword")>0:
                if p_mana>=p_lv+p_classes.count("Spellsword")*3:
                    p_mana-=p_lv+p_classes.count("Spellsword")*3
                    if random.randint(1, 18)==1:#CRIT: also supposed to automatically trip
                        mon1_hp-=(random.randint(13*p_lv, 18*p_lv))
                        mon1_effect="trip"
                        mon1_armor-=2
                        if p_effect=="chrg":
                            mon1_hp-=p_lv*random.randint(5, 9)
                        print("You CRIT! Not only did you automatically hit, but you also dealt much more damage. (And you also automatically tripped.")
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=random.randint(8*p_lv, 13*p_lv)
                            print("You dealt extra damage with your buff!")
                    else:#Not a crit
                        if mon1_armor/random.randint(3, 4)<=random.randint(0, 5) + p_AB_temp/3:
                            mon1_hp-=(random.randint(10*p_lv, 13*p_lv))
                            if random.randint(1, 9)>=4:
                                mon1_effect="trip"
                                print("You tripped it!")
                                mon1_armor-=2
                            else:
                                print("You didn't trip it.")
                            if p_effect=="Cl6" or p_effect=="Ss5":
                                mon1_hp-=(random.randint(4*p_lv, 11*p_lv))
                                print("You dealt extra damage with your buff!")
                        else:
                            print("You missed.")
                else:
                    print("You do not have enough mana for Ss2.")
                    p_turn_pt2()
                    return
            elif q=="ss3" and p_classes.count("Spellsword")>0:
                if p_mana>=p_lv*4-p_classes.count("Spellsword"):
                    p_mana-=p_lv*4-p_classes.count("Spellsword")
                    p_effect="Ss3"
                    print("You cast Imbue: Mana.")
                else:
                    print("You do not have enough mana for Ss3.")
                    p_turn_pt2()
                    return
            elif q=="ss4" and p_classes.count("Spellsword")>0:
                if p_mana>=p_classes.count("Spellsword")+p_lv:
                    p_mana-=p_classes.count("Spellsword")+p_lv
                    if p_effect=="chrg":
                        p_AB_temp+=5
                    if p_effect=="-5 AB":
                        p_AB_temp-=5
                    if random.randint(1, 18)==1:
                        mon1_hp-=(random.randint(14*p_lv, 17*p_lv))
                        if p_effect=="chrg":
                            mon1_hp-=p_lv*random.randint(5, 9)
                        print("You CRIT! Not only did you automatically hit, but you also dealt much more damage.")
                        if "Ss4" in mon1_perma_effect:
                            mon1_perma_effect+="q"
                        else:
                            mon1_perma_effect="Ss4"
                        if random.randint(1, 3)==1:
                            mon1_perma_effect+="q"
                        if p_effect=="Cl6" or p_effect=="Ss5":
                            mon1_hp-=(random.randint(8*p_lv, 13*p_lv))
                            print("You dealt extra damage with your buff!")
                    else:
                        if mon1_armor<=random.randint(-3, 5) + p_AB_temp:
                            mon1_hp-=(random.randint(10*p_lv, 13*p_lv))
                            print("You hit!")
                            if mon1_perma_effect[:3]=="Ss4":
                                mon1_perma_effect+="q"
                            else:
                                mon1_perma_effect="Ss4"
                            if p_effect=="Cl6" or p_effect=="Ss5":
                                mon1_hp-=(random.randint(4*p_lv, 11*p_lv))
                                print("You dealt extra damage with your buff!")
                        else:
                            print("You missed.")
                    if p_effect=="chrg":
                        print("Charge used.")
                        p_AB_temp-=5
                        p_effect="non"
                    if p_effect=="-5 AB":
                        p_AB_temp+=5
                else:
                    print("You do not have enough mana for Ss4.")
                    p_turn_pt2()
                    return
            elif q=="ss5" and p_classes.count("Spellsword")>0:
                if p_mana>=p_classes.count("Spellsword")*3+p_lv*3:
                    p_mana-=p_classes.count("Spellsword")*3+p_lv*3
                    p_effect="Ss5"
                    print("You cast Ss5!")
                else:
                    print("You do not have enough mana for Ss5.")
                    p_turn_pt2()
                    return
            elif q=="py1" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer"):
                    p_mana-=p_classes.count("Pyromancer")
                    if "Fire" in mon1_perma_effect:
                        input_var=random.randint(1, 3)
                        while input_var>0:
                            input_var-=1
                            mon1_perma_effect+="f"
                    else:
                        mon1_perma_effect="Firefff"
                    input_var=len(mon1_perma_effect)-4
                    print(f"You increased it's fire counter! It's up to {input_var} fire!")
                else:
                    print("You do not have enough mana for Py1.")
                    p_turn_pt2()
                    return
            elif q=="py2" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer")+p_lv:
                    p_mana-=p_classes.count("Pyromancer")+p_lv
                    mon1_hp-=(random.randint(3, 4)*mon1_perma_effect.count("f")*p_classes.count("Pyromancer"))
                    print("You hit!")
                else:
                    print("You do not have enough mana for Py2.")
                    p_turn_pt2()
                    return
            elif q=="py3" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer")*2+p_lv-1:
                    p_mana-=p_classes.count("Pyromancer")*2+p_lv-1
                    p_effect="Py3"
                    print("You cast Flame Coating!")
                else:
                    print("You do not have enough mana for Py3.")
                    p_turn_pt2()
                    return
            elif q=="py4" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer")*4+p_lv*2-1:
                    p_mana-=p_classes.count("Pyromancer")*4+p_lv*2-1
                    if "Fire" not in mon1_perma_effect:
                        mon1_perma_effect="Fire"
                    input_var=random.randint(2, 3)
                    while input_var>0:
                        input_var-=1
                        mon1_perma_effect+="f"
                    mon1_hp-=(random.randint(3, 6)*mon1_perma_effect.count("f")*p_classes.count("Pyromancer"))
                    print("You cast FIREBALL!!!")
                else:
                    print("You do not have enough mana for Py4.")
                    p_turn_pt2()
                    return
            elif q=="py5" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer")+p_lv//4:
                    p_mana-=p_classes.count("Pyromancer")+p_lv//4
                    if "Py5" in p_effect:
                        p_effect+="q"
                    else:
                        p_effect="Py5"
                    if int(len(p_effect))-3>0:
                        input_var=" You've cast it "
                        input_var+=str(len(p_effect)-3)
                        input_var+=" times!"
                    else:
                        input_var=""
                    print(f"You cast Fire Shield!{input_var}")
                else:
                    print("You do not have enough mana for Py5.")
                    p_turn_pt2()
                    return
            elif q=="py6" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer")*2+1:
                    p_mana-=p_classes.count("Pyromancer")*2+1
                    p_health+=random.randint(34, 40)*(len(mon1_perma_effect)-4)
                    mon1_perma_effect="non"
                    p_health=int(p_health)
                    print(f"You cast Resurgance! You're up to {p_health} hp/{p_max_health} max hp!")
                else:
                    print("You do not have enough mana for Py6.")
                    p_turn_pt2()
                    return
            elif q=="py7" and p_classes.count("Pyromancer")>0:
                if p_mana>=p_classes.count("Pyromancer"):
                    if "Fire" in mon1_perma_effect and len(mon1_perma_effect)>5:
                        p_mana-=p_classes.count("Pyromancer")
                        mon1_armor-=random.randint(2, 3+p_classes.count("Pyromancer")//random.randint(4, 5))
                    else:
                        print("You have enough mana, but it doesn't have enough fire.")
                        p_turn_pt2()
                        return
                    if mon1_effect=="trip":
                        mon1_armor+=2
                    print(f"Their armor is melted! It has {mon1_armor} armor!")
                    if mon1_effect=="trip":
                        mon1_armor-=2
                else:
                    print("You do not have enough mana for Py7.")
                    p_turn_pt2()
                    return
            else:
                print("You entered a wrong answer. Rebooting now...")
                p_turn_pt2()
                return
            #Fire Blast (Py1): Increase monster's fire counter by a small amount.
            #Flame Strike (Py2): Deal damage to a monster scaling with their fire counter.
            #Flame Coating (Py3): Gives you a buff that allows you to increase it's fire counter every time you attack, and less counters if you trip.
            #Fireball (Py4): It gives the monster some fire counters, then deals damage scaling with their fire counters.
            #Fire Shield (Py5): Increases your DR, and you can stack it. If you do, it gives fire counters scaling with the amount times you cast it.
            #Resurgance (Py6): Remove your opponent's fire counters to heal yourself far past your max hp.
            #Melt Armor (Py7): Reduce it's armor. Also requires a high fire counter on the enemy.
        else:
            print("These are what the actions do:\n-Attack: Just a base attack, a good chance to hit, and a good amount of damage.\n-Trip: This will knock the target prone, effectivally skipping their turn. However, this does have a harder chance to hit, and deals less damage. If they get up,\nthey have a small chance to attack without penalty, but most of the time, they'll get a penalty of 5, so basically, you get +5 armor.\n-Examine: It just displays their stats. It does give your turn back.\n-Charge: This doesn't give extra damage, instead it gives +5 to hit. Keep in mind, this does skip your turn.")
            p_turn_pt2()
            return
        mon1_hp=mon1_hp//1
        if p_effect[:5]=="Rage_":
            p_effect=p_effect[:int(len(p_effect)-1)]
            if len(p_effect)<6:
                p_effect="non"
        if p_effect=='-5 AB':
            p_effect='non'

print("Welcome to Simple RPG! I hope you have a fun time in this adventureful paradise!")
while True:
    input_var=input("Would you like a tutorial? (Most games' tutorials are 'optional', but this one is REQUIRED!)\n>>>")
    input_var=input_var.lower()
    if input_var=="yes" or input_var=="y":
        tutorial()
        break
    elif input_var=="no" or input_var=="n":
        break
    else:
        print("The required inputs are either 'yes' or 'no'.")
settings("First")
choose_a_race()
while False:
    p_max_health=466
    p_max_mana=233
    p_AB=17
    p_max_armor=5
    p_max_DR=142
    p_max_speed=39
    quest="0 Monster -> 2 point(s)"
    p_lv=12
    p_race="High Elf"
    p_classes=["Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer", "Pyromancer"]
    rest()
    while True:
        create_monster()
        fight()
        more_fights=random.uniform(-1, 1+p_lv/random.randint(2, 5))
        if p_lv%12==0:
            more_fights=0
        while more_fights>0:
            more_fights-=1
            create_monster()
            rest()
            fight()
        level_up()
while True:
    level_up()
    create_monster()
    fight()
    more_fights=random.uniform(-1, 1+p_lv/random.randint(2, 5))
    if p_lv%12==0:
        more_fights=0
    while more_fights>0:
        more_fights-=1
        create_monster()
        rest()
        fight()
