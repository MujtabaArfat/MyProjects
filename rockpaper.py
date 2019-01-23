from random import choice


print("Rock...")
print("Paper...")
print("Scissor...")

player1 = input("player1: Enter your move\n")
player2 = choice(["Rock","Paper","Scissor"])

if(player1 == player2):
	print("Its a tie")
elif(player1=="Rock"):
	if(player2==Paper):
		print("Player2 won")
	elif(player2=="Scissor")
		print("Player won")
elif(player1=="Paper"):
	if(player2=="Rock"):	
		print("Player1 won")
	elif(player2=="Scissor"):
		print("Player2 won")
elif(player1=="Scissor"):
	if(player2=="Rock"):
		print("player1 won")
	elif(player2=="Paper")	
		print("")			



