from random import choice

cpu = choice(["ROCK","PAPER","SCISSOR"])

print("ROCK..")
print("PAPER>>")
print("Scissor")

player = input("enter ur move")
for i in range(1,3):
    if player.upper()==cpu.upper():
        print("TIE")
        player = input("enter ur move")
    else:
        if player.upper()=="ROCK":
            if cpu.upper()=="SCISSOR":
                print("Player1 won")
                player = input("enter ur move")
                break
        elif cpu.upper() =="PAPER":
                print("CPU WON")
                player = input("enter ur move")
                break
        if player.upper()=="Paper":
            if cpu.upper()=="SCISSOR":
                print("CPU won")
                player = input("enter ur move")
                break
            elif cpu.upper() =="ROCK":
                print("PLayer won")
                player = input("enter ur move")
                break
        if player.upper()=="SCISSOR":
            if cpu.upper()=="ROCK":
                print("CPU won")
                player = input("enter ur move")
                break
            elif cpu.upper() =="paper":
                print("PLayer won")
                player = input("enter ur move")
                break