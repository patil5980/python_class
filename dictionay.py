keys = ["SRK","Salman","Amir"]
names = {
  "SRH":20,
  "Salman":40,
  "Amir":50,
}
print(names)

for key_labels in names.keys():
   print(key_labels)

for key_labels in names.values():
   print(key_labels)

names['akshay'] = 60
print(names)

names["Salman"] = 80
print(names)

for key_label,value_label in names.items():
  print(key_label+" "+str(value_label))
# output

# {'SRH': 20, 'Salman': 40, 'Amir': 50}
# SRH
# Salman
# Amir
# 20
# 40
# 50
# {'SRH': 20, 'Salman': 40, 'Amir': 50, 'akshay': 60}
# {'SRH': 20, 'Salman': 80, 'Amir': 50, 'akshay': 60}
# SRH 20
# Salman 80
# Amir 50
# akshay 60
