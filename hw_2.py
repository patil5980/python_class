player_name = []

keys = ["ajinkya","virat","jadeja","bumrah","bhuvaneshvar"]

player_name = {
 
}
player_name["ajinkya"] = 1
player_name["virat"] = 7
player_name["jadeja"] = 3
player_name["bumrah"] = 5
player_name["bhuvaneshvar"] = 2
print(player_name)

for key_labels in player_name.keys():
  print(key_labels)

for key_labels in player_name.values():
  print(key_labels)
for key_label,value_label in player_name.items():
  print(key_label+" "+str(value_label))

if player_name == "bhuvaneshvar" in  player_name.keys():
  print("bhuvaneshvar found")

else:
  print("bhuvaneshvar not found")     

