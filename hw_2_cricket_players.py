player_name = []

keys = ["ajinkya","virat","jadeja","bumrah","bhuvaneshvar"]

cricket_players = {
 }
cricket_players["ajinkya"] = 1
cricket_players["virat"] = 7
cricket_players["jadeja"] = 3
cricket_players["bumrah"] = 5
cricket_players["bhuvaneshvar"] = 2
print(cricket_players)

for player_name in cricket_players.keys():
  print(player_name)

for player_name in cricket_players.values():
  print(player_name)

for player_name,player_val in cricket_players.items():
  print(player_name+" "+str(player_val))

if player_name == "bhuvaneshvar" in  cricket_players.keys():
  print("bhuvaneshvar found")

else:
  print("bhuvaneshvar not found")     
  
##############
#{'ajinkya': 1, 'virat': 7, 'jadeja': 3, 'bumrah': 5, 'bhuvaneshvar': 2}
#ajinkya
#virat
#jadeja
#bumrah
#bhuvaneshvar
#1
#7
#3
#5
#2
#ajinkya 1
#virat 7
#jadeja 3
#bumrah 5
#bhuvaneshvar 2
#bhuvaneshvar found
